#
# Copyright 2013 Julien Danjou
# Copyright 2014-2017 Red Hat, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import collections
import glob
import itertools
import logging
import os
import queue
import random
import socket
import threading
import uuid

from concurrent import futures
import cotyledon
from futurist import periodics
from keystoneauth1 import exceptions as ka_exceptions
from oslo_config import cfg
from oslo_log import log
import oslo_messaging
from oslo_utils import netutils
from oslo_utils import timeutils
from stevedore import extension
from tooz import coordination
from urllib import parse as urlparse

from ceilometer import agent
from ceilometer import cache_utils
from ceilometer import declarative
from ceilometer import keystone_client
from ceilometer import messaging
from ceilometer.polling import dynamic_pollster
from ceilometer.polling import plugin_base
from ceilometer.polling import prom_exporter
from ceilometer.publisher import utils as publisher_utils
from ceilometer import utils

LOG = log.getLogger(__name__)

POLLING_OPTS = [
    cfg.StrOpt('cfg_file',
               default="polling.yaml",
               help="Configuration file for polling definition."
               ),
    cfg.StrOpt('heartbeat_socket_dir',
               default=None,
               help="Path to directory where socket file for polling "
                    "heartbeat will be created."),
    cfg.StrOpt('partitioning_group_prefix',
               deprecated_group='central',
               help='Work-load partitioning group prefix. Use only if you '
                    'want to run multiple polling agents with different '
                    'config files. For each sub-group of the agent '
                    'pool with the same partitioning_group_prefix a disjoint '
                    'subset of pollsters should be loaded.'),
    cfg.IntOpt('batch_size',
               default=50,
               help='Batch size of samples to send to notification agent, '
                    'Set to 0 to disable. When prometheus exporter feature '
                    'is used, this should be largered than maximum number of '
                    'samples per metric.'),
    cfg.MultiStrOpt('pollsters_definitions_dirs',
                    default=["/etc/ceilometer/pollsters.d"],
                    help="List of directories with YAML files used "
                         "to created pollsters."),
    cfg.BoolOpt('identity_name_discovery',
                deprecated_name='tenant_name_discovery',
                default=False,
                help='Identify project and user names from polled samples. '
                     'By default, collecting these values is disabled due '
                     'to the fact that it could overwhelm keystone service '
                     'with lots of continuous requests depending upon the '
                     'number of projects, users and samples polled from '
                     'the environment. While using this feature, it is '
                     'recommended that ceilometer be configured with a '
                     'caching backend to reduce the number of calls '
                     'made to keystone.'),
    cfg.BoolOpt('enable_notifications',
                default=True,
                help='Whether the polling service should be sending '
                     'notifications after polling cycles.'),
    cfg.BoolOpt('enable_prometheus_exporter',
                default=False,
                help='Allow this ceilometer polling instance to '
                     'expose directly the retrieved metrics in Prometheus '
                     'format.'),
    cfg.ListOpt('prometheus_listen_addresses',
                default=["127.0.0.1:9101"],
                help='A list of ipaddr:port combinations on which '
                     'the exported metrics will be exposed.'),
    cfg.BoolOpt('ignore_disabled_projects',
                default=False,
                help='Whether the polling service should ignore '
                     'disabled projects or not.'),
    cfg.BoolOpt('prometheus_tls_enable',
                default=False,
                help='Whether it will expose tls metrics or not'),
    cfg.StrOpt('prometheus_tls_certfile',
               default=None,
               help='The certificate file to allow this ceilometer to '
                    'expose tls scrape endpoints'),
    cfg.StrOpt('prometheus_tls_keyfile',
               default=None,
               help='The private key to allow this ceilometer to '
                    'expose tls scrape endpoints'),
    cfg.IntOpt('threads_to_process_pollsters',
               default=1,
               min=0,
               help='The number of threads used to process the pollsters.'
                    'The value one (1) means that the processing is in a'
                    'serial fashion (not ordered!). The value zero (0) means '
                    'that the we will use as much threads as the number of '
                    'pollsters configured in the polling task. Any other'
                    'positive integer can be used to fix an upper bound limit'
                    'to the number of threads used for processing pollsters in'
                    'parallel. One must bear in mind that, using more than one'
                    'thread might not take full advantage of the discovery '
                    'cache and pollsters cache processes; it is possible '
                    'though to improve/use pollsters that synchronize '
                    'themselves in the cache objects.'),
]


def hash_of_set(s):
    return str(hash(frozenset(s)))


class PollingException(agent.ConfigException):
    def __init__(self, message, cfg):
        super().__init__('Polling', message, cfg)


class HeartBeatException(agent.ConfigException):
    def __init__(self, message, cfg):
        super().__init__('Polling', message, cfg)


class Resources:
    def __init__(self, agent_manager):
        self.agent_manager = agent_manager
        self._resources = []
        self._discovery = []
        self.blacklist = []

    def setup(self, source):
        self._resources = source.resources
        self._discovery = source.discovery

    def get(self, discovery_cache=None):
        source_discovery = (self.agent_manager.discover(self._discovery,
                                                        discovery_cache)
                            if self._discovery else [])

        if self._resources:
            static_resources_group = self.agent_manager.construct_group_id(
                hash_of_set(self._resources))
            return [v for v in self._resources if
                    not self.agent_manager.partition_coordinator or
                    self.agent_manager.hashrings[
                        static_resources_group].belongs_to_self(
                        str(v))] + source_discovery

        return source_discovery

    @staticmethod
    def key(source_name, pollster):
        return '{}-{}'.format(source_name, pollster.name)


def iter_random(iterable):
    """Iter over iterable in a random fashion."""
    lst = list(iterable)
    random.shuffle(lst)
    return iter(lst)


class PollingTask:
    """Polling task for polling samples and notifying.

    A polling task can be invoked periodically or only once.
    """

    def __init__(self, agent_manager):
        self.manager = agent_manager

        # elements of the Cartesian product of sources X pollsters
        # with a common interval
        self.pollster_matches = collections.defaultdict(set)

        # we relate the static resources and per-source discovery to
        # each combination of pollster and matching source
        resource_factory = lambda: Resources(agent_manager)  # noqa: E731
        self.resources = collections.defaultdict(resource_factory)

        conf = self.manager.conf
        self._batch_size = conf.polling.batch_size
        self._telemetry_secret = conf.publisher.telemetry_secret
        self.ks_client = self.manager.keystone
        self._name_discovery = conf.polling.identity_name_discovery
        self._cache = cache_utils.get_client(conf)

        # element that provides a map between source names and source object
        self.sources_map = dict()

    def add(self, pollster, source):
        self.sources_map[source.name] = source

        self.pollster_matches[source.name].add(pollster)
        key = Resources.key(source.name, pollster)
        self.resources[key].setup(source)

    def poll_and_notify(self):
        """Polling sample and notify."""
        cache = {}
        discovery_cache = {}
        poll_history = {}
        for source_name, pollsters in iter_random(
                self.pollster_matches.items()):
            self.execute_polling_task_processing(cache, discovery_cache,
                                                 poll_history, pollsters,
                                                 source_name)

    def execute_polling_task_processing(self, cache, discovery_cache,
                                        poll_history, pollsters, source_name):
        all_pollsters = list(pollsters)
        number_workers_for_pollsters =\
            self.manager.conf.polling.threads_to_process_pollsters

        if number_workers_for_pollsters < 0:
            raise RuntimeError("The configuration "
                               "'threads_to_process_pollsters' has a negative "
                               "value [%s], which should not be allowed.",
                               number_workers_for_pollsters)

        if number_workers_for_pollsters == 0:
            number_workers_for_pollsters = len(all_pollsters)

        if number_workers_for_pollsters < len(all_pollsters):
            LOG.debug("The number of pollsters in source [%s] is bigger "
                      "than the number of worker threads to execute them. "
                      "Therefore, one can expect the process to be longer "
                      "than the expected.", source_name)

        all_pollster_scheduled = []
        with futures.ThreadPoolExecutor(
                thread_name_prefix="Pollster-executor",
                max_workers=number_workers_for_pollsters) as executor:
            LOG.debug("Processing pollsters for [%s] with [%s] threads.",
                      source_name, number_workers_for_pollsters)

            for pollster in all_pollsters:
                all_pollster_scheduled.append(
                    self.register_pollster_execution(
                        cache, discovery_cache, executor, poll_history,
                        pollster, source_name))

        for s in all_pollster_scheduled:
            LOG.debug(s.result())

    def register_pollster_execution(self, cache, discovery_cache, executor,
                                    poll_history, pollster, source_name):
        LOG.debug("Registering pollster [%s] from source [%s] to be executed "
                  "via executor [%s] with cache [%s], pollster history [%s], "
                  "and discovery cache [%s].", pollster, source_name, executor,
                  cache, poll_history, discovery_cache)

        def _internal_function():
            self._internal_pollster_run(cache, discovery_cache, poll_history,
                                        pollster, source_name)
            return "Finished processing pollster [%s]." % pollster.name

        return executor.submit(_internal_function)

    def _internal_pollster_run(self, cache, discovery_cache, poll_history,
                               pollster, source_name):
        key = Resources.key(source_name, pollster)
        candidate_res = list(
            self.resources[key].get(discovery_cache))
        if not candidate_res and pollster.obj.default_discovery:
            LOG.debug("Executing discovery process for pollsters [%s] "
                      "and discovery method [%s] via process [%s].",
                      pollster.obj, pollster.obj.default_discovery,
                      self.manager.discover)

            candidate_res = self.manager.discover(
                [pollster.obj.default_discovery], discovery_cache)

        # Remove duplicated resources and black resources. Using
        # set() requires well defined __hash__ for each resource.
        # Since __eq__ is defined, 'not in' is safe here.
        polling_resources = []
        black_res = self.resources[key].blacklist
        history = poll_history.get(pollster.name, [])
        for x in candidate_res:
            if x not in history:
                history.append(x)
                if x not in black_res:
                    polling_resources.append(x)
        poll_history[pollster.name] = history

        # If no resources, skip for this pollster
        if not polling_resources:
            p_context = 'new' if history else ''
            LOG.debug("Skip pollster %(name)s, no %(p_context)s "
                      "resources found this cycle",
                      {'name': pollster.name, 'p_context': p_context})
            return

        LOG.info("Polling pollster %(poll)s in the context of "
                 "%(src)s",
                 dict(poll=pollster.name, src=source_name))
        try:
            source_obj = self.sources_map[source_name]
            coordination_group_name = source_obj.group_for_coordination

            LOG.debug("Checking if we need coordination for pollster "
                      "[%s] with coordination group name [%s].",
                      pollster, coordination_group_name)
            if self.manager.hashrings and self.manager.hashrings.get(
                    coordination_group_name):
                LOG.debug("The pollster [%s] is configured in a "
                          "source for polling that requires "
                          "coordination under name [%s].", pollster,
                          coordination_group_name)
                group_coordination = self.manager.hashrings[
                    coordination_group_name].belongs_to_self(
                    str(pollster.name))

                LOG.debug("Pollster [%s] is configured with "
                          "coordination [%s] under name [%s].",
                          pollster.name, group_coordination,
                          coordination_group_name)
                if not group_coordination:
                    LOG.info("The pollster [%s] should be processed "
                             "by other node.", pollster.name)
                    return
            else:
                LOG.debug("The pollster [%s] is not configured in a "
                          "source for polling that requires "
                          "coordination. The current hashrings are "
                          "the following [%s].", pollster,
                          self.manager.hashrings)

            polling_timestamp = timeutils.utcnow().isoformat()
            samples = pollster.obj.get_samples(
                manager=self.manager,
                cache=cache,
                resources=polling_resources
            )
            sample_batch = []

            self.manager.heartbeat(pollster.name, polling_timestamp)

            for sample in samples:
                # Note(yuywz): Unify the timestamp of polled samples
                sample.set_timestamp(polling_timestamp)

                if self._name_discovery and self._cache:

                    # Try to resolve project UUIDs from cache first,
                    # and then keystone
                    LOG.debug("Ceilometer is configured to resolve "
                              "project IDs to name; loading the "
                              "project name for project ID [%s] in "
                              "sample [%s].", sample.project_id,
                              sample)
                    if sample.project_id:
                        sample.project_name = \
                            self._cache.resolve_uuid_from_cache(
                                "projects",
                                sample.project_id
                            )

                    # Try to resolve user UUIDs from cache first,
                    # and then keystone
                    LOG.debug("Ceilometer is configured to resolve "
                              "user IDs to name; loading the "
                              "user name for user ID [%s] in "
                              "sample [%s].", sample.user_id,
                              sample)

                    if sample.user_id:
                        sample.user_name = \
                            self._cache.resolve_uuid_from_cache(
                                "users",
                                sample.user_id
                            )

                    LOG.debug("Final sample generated after loading "
                              "the project and user names bases on "
                              "the IDs [%s].", sample)

                sample_dict = (
                    publisher_utils.meter_message_from_counter(
                        sample, self._telemetry_secret
                    ))
                if self._batch_size:
                    if len(sample_batch) >= self._batch_size:
                        self._send_notification(sample_batch)
                        sample_batch = []
                    sample_batch.append(sample_dict)
                else:
                    self._send_notification([sample_dict])

            if sample_batch:
                self._send_notification(sample_batch)

            LOG.info("Finished polling pollster %(poll)s in the "
                     "context of %(src)s", dict(poll=pollster.name,
                                                src=source_name))
        except plugin_base.PollsterPermanentError as err:
            LOG.error(
                'Prevent pollster %(name)s from '
                'polling %(res_list)s on source %(source)s anymore!',
                dict(name=pollster.name,
                     res_list=str(err.fail_res_list),
                     source=source_name))
            self.resources[key].blacklist.extend(err.fail_res_list)
        except Exception as err:
            LOG.error(
                'Continue after error from %(name)s: %(error)s',
                {'name': pollster.name, 'error': err},
                exc_info=True)

    def _send_notification(self, samples):
        if self.manager.conf.polling.enable_notifications:
            self.manager.notifier.sample(
                {},
                'telemetry.polling',
                {'samples': samples}
            )
        if self.manager.conf.polling.enable_prometheus_exporter:
            prom_exporter.collect_metrics(samples)


class AgentHeartBeatManager(cotyledon.Service):
    def __init__(self, worker_id, conf, namespaces=None, queue=None):
        super().__init__(worker_id)
        self.conf = conf

        if conf.polling.heartbeat_socket_dir is None:
            raise HeartBeatException("path to a directory containing "
                                     "heart beat sockets is required", conf)

        if type(namespaces) is not list:
            if namespaces is None:
                namespaces = ""
            namespaces = [namespaces]

        self._lock = threading.Lock()
        self._queue = queue
        self._status = dict()
        self._sock_pth = os.path.join(
            conf.polling.heartbeat_socket_dir,
            f"ceilometer-{'-'.join(sorted(namespaces))}.socket"
        )

        self._delete_socket()
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            self._sock.bind(self._sock_pth)
            self._sock.listen(1)
        except OSError as err:
            raise HeartBeatException("Failed to open socket file "
                                     f"({self._sock_pth}): {err}", conf)

        LOG.info("Starting heartbeat child service. Listening"
                 f" on {self._sock_pth}")

    def _delete_socket(self):
        try:
            os.remove(self._sock_pth)
        except OSError:
            pass

    def terminate(self):
        self._tpe.shutdown(wait=False, cancel_futures=True)
        self._sock.close()
        self._delete_socket()

    def _update_status(self):
        hb = self._queue.get()
        with self._lock:
            self._status[hb['pollster']] = hb['timestamp']
        LOG.debug(f"Updated heartbeat for {hb['pollster']} "
                  f"({hb['timestamp']})")

    def _send_heartbeat(self):
        s, addr = self._sock.accept()
        LOG.debug("Heartbeat status report requested "
                  f"at {self._sock_pth}")
        with self._lock:
            out = '\n'.join([f"{k} {v}"
                             for k, v in self._status.items()])
        s.sendall(out.encode('utf-8'))
        s.close()
        LOG.debug(f"Reported heartbeat status:\n{out}")

    def run(self):
        super().run()

        LOG.debug("Started heartbeat child process.")

        def _read_queue():
            LOG.debug("Started heartbeat update thread")
            while True:
                self._update_status()

        def _report_status():
            LOG.debug("Started heartbeat reporting thread")
            while True:
                self._send_heartbeat()

        with futures.ThreadPoolExecutor(max_workers=2) as executor:
            self._tpe = executor
            executor.submit(_read_queue)
            executor.submit(_report_status)


class AgentManager(cotyledon.Service):

    def __init__(self, worker_id, conf, namespaces=None, queue=None):
        namespaces = namespaces or ['compute', 'central']
        group_prefix = conf.polling.partitioning_group_prefix

        super().__init__(worker_id)

        self.conf = conf
        self._queue = queue

        if type(namespaces) is not list:
            namespaces = [namespaces]

        # we'll have default ['compute', 'central'] here if no namespaces will
        # be passed
        extensions = (self._extensions('poll', namespace, self.conf).extensions
                      for namespace in namespaces)
        extensions = list(itertools.chain(*list(extensions)))

        # get the extensions from pollster builder
        extensions_fb = (self._extensions_from_builder('poll', namespace)
                         for namespace in namespaces)
        extensions_fb = list(itertools.chain(*list(extensions_fb)))

        # NOTE(tkajinam): Remove this after 2026.1 release
        if extensions_fb:
            LOG.warning('Support for pollster build has been deprecated')

        # Create dynamic pollsters
        extensions_dynamic_pollsters = self.create_dynamic_pollsters(
            namespaces)
        extensions_dynamic_pollsters = list(extensions_dynamic_pollsters)

        self.extensions = (
            extensions + extensions_fb + extensions_dynamic_pollsters)

        if not self.extensions:
            LOG.warning('No valid pollsters can be loaded from %s '
                        'namespaces', namespaces)

        discoveries = (self._extensions('discover', namespace,
                                        self.conf).extensions
                       for namespace in namespaces)
        self.discoveries = list(itertools.chain(*list(discoveries)))
        self.polling_periodics = None

        self.hashrings = None
        self.partition_coordinator = None
        if self.conf.coordination.backend_url:
            # XXX uuid4().bytes ought to work, but it requires ascii for now
            coordination_id = str(uuid.uuid4()).encode('ascii')
            self.partition_coordinator = coordination.get_coordinator(
                self.conf.coordination.backend_url, coordination_id)

        # Compose coordination group prefix.
        # We'll use namespaces as the basement for this partitioning.
        namespace_prefix = '-'.join(sorted(namespaces))
        self.group_prefix = ('{}-{}'.format(namespace_prefix, group_prefix)
                             if group_prefix else namespace_prefix)

        if self.conf.polling.enable_notifications:
            self.notifier = oslo_messaging.Notifier(
                messaging.get_transport(self.conf),
                driver=self.conf.publisher_notifier.telemetry_driver,
                publisher_id="ceilometer.polling")

        if self.conf.polling.enable_prometheus_exporter:
            for addr in self.conf.polling.prometheus_listen_addresses:
                address = netutils.parse_host_port(addr)
                if address[0] is None or address[1] is None:
                    LOG.warning('Ignoring invalid address: %s', addr)
                certfile = self.conf.polling.prometheus_tls_certfile
                keyfile = self.conf.polling.prometheus_tls_keyfile
                if self.conf.polling.prometheus_tls_enable:
                    if not certfile or not keyfile:
                        raise ValueError(
                            "Certfile and keyfile must be provided."
                        )
                else:
                    certfile = keyfile = None
                prom_exporter.export(
                    address[0],
                    address[1],
                    certfile,
                    keyfile)

        self._keystone = None
        self._keystone_last_exception = None

    def heartbeat(self, name, timestamp):
        """Send heartbeat data if the agent is configured to do so."""
        if self._queue is not None:
            try:
                hb = {
                    'timestamp': timestamp,
                    'pollster': name
                }
                self._queue.put_nowait(hb)
                LOG.debug(f"Polster heartbeat update: {name}")
            except queue.Full:
                LOG.warning(f"Heartbeat queue full. Update failed: {hb}")

    def create_dynamic_pollsters(self, namespaces):
        """Creates dynamic pollsters

        This method Creates dynamic pollsters based on configurations placed on
        'pollsters_definitions_dirs'

        :param namespaces: The namespaces we are running on to validate if
                           the pollster should be instantiated or not.
        :return: a list with the dynamic pollsters defined by the operator.
        """

        namespaces_set = set(namespaces)
        pollsters_definitions_dirs = self.conf.pollsters_definitions_dirs
        if not pollsters_definitions_dirs:
            LOG.info("Variable 'pollsters_definitions_dirs' not defined.")
            return []

        LOG.info("Looking for dynamic pollsters configurations at [%s].",
                 pollsters_definitions_dirs)
        pollsters_definitions_files = []
        for directory in pollsters_definitions_dirs:
            files = glob.glob(os.path.join(directory, "*.yaml"))
            if not files:
                LOG.info("No dynamic pollsters found in folder [%s].",
                         directory)
                continue
            for filepath in sorted(files):
                if filepath is not None:
                    pollsters_definitions_files.append(filepath)

        if not pollsters_definitions_files:
            LOG.info("No dynamic pollsters file found in dirs [%s].",
                     pollsters_definitions_dirs)
            return []

        pollsters_definitions = {}
        for pollsters_definitions_file in pollsters_definitions_files:
            pollsters_cfg = declarative.load_definitions(
                self.conf, {}, pollsters_definitions_file)

            LOG.info("File [%s] has [%s] dynamic pollster configurations.",
                     pollsters_definitions_file, len(pollsters_cfg))

            for pollster_cfg in pollsters_cfg:
                pollster_name = pollster_cfg['name']
                pollster_namespaces = pollster_cfg.get(
                    'namespaces', ['central'])
                if isinstance(pollster_namespaces, list):
                    pollster_namespaces = set(pollster_namespaces)
                else:
                    pollster_namespaces = {pollster_namespaces}

                if not bool(namespaces_set & pollster_namespaces):
                    LOG.info("The pollster [%s] is not configured to run in "
                             "these namespaces %s, the configured namespaces "
                             "for this pollster are %s. Therefore, we are "
                             "skipping it.", pollster_name, namespaces_set,
                             pollster_namespaces)
                    continue

                if pollster_name not in pollsters_definitions:
                    LOG.info("Loading dynamic pollster [%s] from file [%s].",
                             pollster_name, pollsters_definitions_file)
                    try:
                        pollsters_definitions[pollster_name] =\
                            dynamic_pollster.DynamicPollster(
                                pollster_cfg, self.conf)
                    except Exception as e:
                        LOG.error(
                            "Error [%s] while loading dynamic pollster [%s].",
                            e, pollster_name)

                else:
                    LOG.info(
                        "Dynamic pollster [%s] is already defined."
                        "Therefore, we are skipping it.", pollster_name)

        LOG.debug("Total of dynamic pollsters [%s] loaded.",
                  len(pollsters_definitions))
        return pollsters_definitions.values()

    @staticmethod
    def _get_ext_mgr(namespace, *args, **kwargs):
        def _catch_extension_load_error(mgr, ep, exc):
            # Extension raising ExtensionLoadError can be ignored,
            # and ignore anything we can't import as a safety measure.
            if isinstance(exc, plugin_base.ExtensionLoadError):
                LOG.debug("Skip loading extension for %s: %s",
                          ep.name, exc.msg)
                return

            show_exception = (LOG.isEnabledFor(logging.DEBUG)
                              and isinstance(exc, ImportError))
            LOG.error("Failed to import extension for %(name)r: "
                      "%(error)s",
                      {'name': ep.name, 'error': exc},
                      exc_info=show_exception)
            if isinstance(exc, ImportError):
                return
            raise exc

        return extension.ExtensionManager(
            namespace=namespace,
            invoke_on_load=True,
            invoke_args=args,
            invoke_kwds=kwargs,
            on_load_failure_callback=_catch_extension_load_error,
        )

    def _extensions(self, category, agent_ns=None, *args, **kwargs):
        namespace = ('ceilometer.{}.{}'.format(category, agent_ns) if agent_ns
                     else 'ceilometer.%s' % category)
        return self._get_ext_mgr(namespace, *args, **kwargs)

    def _extensions_from_builder(self, category, agent_ns=None):
        ns = ('ceilometer.builder.{}.{}'.format(category, agent_ns) if agent_ns
              else 'ceilometer.builder.%s' % category)
        mgr = self._get_ext_mgr(ns, self.conf)

        def _build(ext):
            return ext.plugin.get_pollsters_extensions(self.conf)

        # NOTE: this seems a stevedore bug. if no extensions are found,
        # map will raise runtimeError which is not documented.
        if mgr.names():
            return list(itertools.chain(*mgr.map(_build)))
        else:
            return []

    def join_partitioning_groups(self):
        groups = set()
        for d in self.discoveries:
            generated_group_id = self.construct_group_id(d.obj.group_id)
            LOG.debug("Adding discovery [%s] with group ID [%s] to build the "
                      "coordination partitioning via constructed group ID "
                      "[%s].", d.__dict__, d.obj.group_id, generated_group_id)
            groups.add(generated_group_id)

        # let each set of statically-defined resources have its own group
        static_resource_groups = set()
        for p in self.polling_manager.sources:
            if p.resources:
                generated_group_id = self.construct_group_id(
                    hash_of_set(p.resources))
                LOG.debug("Adding pollster group [%s] with resources [%s] to "
                          "build the coordination partitioning via "
                          "constructed group ID [%s].", p, p.resources,
                          generated_group_id)
                static_resource_groups.add(generated_group_id)
            else:
                LOG.debug("Pollster group [%s] does not have resources defined"
                          "to build the group ID for coordination.", p)

        groups.update(static_resource_groups)

        # (rafaelweingartner) here we will configure the dynamic
        # coordination process. It is useful to sync pollster that do not rely
        # on discovery process, such as the dynamic pollster on compute nodes.
        dynamic_pollster_groups_for_coordination = set()
        for p in self.polling_manager.sources:
            if p.group_id_coordination_expression:
                if p.resources:
                    LOG.warning("The pollster group [%s] has resources to "
                                "execute coordination. Therefore, we do not "
                                "add it via the dynamic coordination process.",
                                p.name)
                    continue
                group_prefix = p.name
                generated_group_id = eval(p.group_id_coordination_expression)

                group_for_coordination = "{}-{}".format(
                    group_prefix, generated_group_id)
                dynamic_pollster_groups_for_coordination.add(
                    group_for_coordination)

                p.group_for_coordination = group_for_coordination
                LOG.debug("Adding pollster group [%s] with dynamic "
                          "coordination to build the coordination "
                          "partitioning via constructed group ID [%s].",
                          p, dynamic_pollster_groups_for_coordination)
            else:
                LOG.debug("Pollster group [%s] does not have an expression to "
                          "dynamically use in the coordination process.", p)

        groups.update(dynamic_pollster_groups_for_coordination)

        self.hashrings = {
            group: self.partition_coordinator.join_partitioned_group(group)
            for group in groups}

        LOG.debug("Hashrings [%s] created for pollsters definition.",
                  self.hashrings)

    def setup_polling_tasks(self):
        polling_tasks = {}
        for source in self.polling_manager.sources:
            for pollster in self.extensions:
                if source.support_meter(pollster.name):
                    polling_task = polling_tasks.get(source.get_interval())
                    if not polling_task:
                        polling_task = PollingTask(self)
                        polling_tasks[source.get_interval()] = polling_task
                    polling_task.add(pollster, source)
        return polling_tasks

    def construct_group_id(self, discovery_group_id):
        return '{}-{}'.format(self.group_prefix, discovery_group_id)

    def start_polling_tasks(self):
        data = self.setup_polling_tasks()

        # Don't start useless threads if no task will run
        if not data:
            return

        # One thread per polling tasks is enough
        self.polling_periodics = periodics.PeriodicWorker.create(
            [], executor_factory=lambda:
            futures.ThreadPoolExecutor(max_workers=len(data)))

        for interval, polling_task in data.items():
            @periodics.periodic(spacing=interval, run_immediately=True)
            def task(running_task):
                self.interval_task(running_task)

            self.polling_periodics.add(task, polling_task)

        utils.spawn_thread(self.polling_periodics.start, allow_empty=True)

    def run(self):
        super().run()
        self.polling_manager = PollingManager(self.conf)
        if self.partition_coordinator:
            self.partition_coordinator.start(start_heart=True)
            self.join_partitioning_groups()
        self.start_polling_tasks()

    def terminate(self):
        self.stop_pollsters_tasks()
        if self.partition_coordinator:
            self.partition_coordinator.stop()
        super().terminate()

    def interval_task(self, task):
        # NOTE(sileht): remove the previous keystone client
        # and exception to get a new one in this polling cycle.
        self._keystone = None
        self._keystone_last_exception = None

        # Note(leehom): if coordinator enabled call run_watchers to
        # update group member info before collecting
        if self.partition_coordinator:
            self.partition_coordinator.run_watchers()

        task.poll_and_notify()

    @property
    def keystone(self):
        # FIXME(sileht): This lazy loading of keystone client doesn't
        # look concurrently safe, we never see issue because once we have
        # connected to keystone everything is fine, and because all pollsters
        # are delayed during startup. But each polling task creates a new
        # client and overrides it which has been created by other polling
        # tasks. During this short time bad thing can occur.
        #
        # I think we must not reset keystone client before
        # running a polling task, but refresh it periodically instead.

        # NOTE(sileht): we do lazy loading of the keystone client
        # for multiple reasons:
        # * don't use it if no plugin need it
        # * use only one client for all plugins per polling cycle
        if self._keystone is None and self._keystone_last_exception is None:
            try:
                self._keystone = keystone_client.get_client(self.conf)
                self._keystone_last_exception = None
            except ka_exceptions.ClientException as e:
                self._keystone = None
                self._keystone_last_exception = e
        if self._keystone is not None:
            return self._keystone
        else:
            raise self._keystone_last_exception

    @staticmethod
    def _parse_discoverer(url):
        s = urlparse.urlparse(url)
        return (s.scheme or s.path), (s.netloc + s.path if s.scheme else None)

    def _discoverer(self, name):
        for d in self.discoveries:
            if d.name == name:
                return d.obj
        return None

    def discover(self, discovery=None, discovery_cache=None):
        resources = []
        discovery = discovery or []
        for url in discovery:
            if discovery_cache is not None and url in discovery_cache:
                resources.extend(discovery_cache[url])
                continue
            name, param = self._parse_discoverer(url)
            discoverer = self._discoverer(name)
            if discoverer:
                try:
                    if discoverer.KEYSTONE_REQUIRED_FOR_SERVICE:
                        service_type = getattr(
                            self.conf.service_types,
                            discoverer.KEYSTONE_REQUIRED_FOR_SERVICE)
                        if not keystone_client.\
                                get_service_catalog(self.keystone).\
                                get_endpoints(service_type=service_type):
                            LOG.warning(
                                'Skipping %(name)s, %(service_type)s service '
                                'is not registered in keystone',
                                {'name': name, 'service_type': service_type})
                            continue

                    discovered = discoverer.discover(self, param)

                    if self.partition_coordinator:
                        discovered = [
                            v for v in discovered if self.hashrings[
                                self.construct_group_id(discoverer.group_id)
                            ].belongs_to_self(str(v))]

                    resources.extend(discovered)
                    if discovery_cache is not None:
                        discovery_cache[url] = discovered
                except ka_exceptions.ClientException as e:
                    LOG.error('Skipping %(name)s, keystone issue: '
                              '%(exc)s', {'name': name, 'exc': e})
                except Exception as err:
                    LOG.exception('Unable to discover resources: %s', err)
            else:
                LOG.warning('Unknown discovery extension: %s', name)
        return resources

    def stop_pollsters_tasks(self):
        if self.polling_periodics:
            self.polling_periodics.stop()
            self.polling_periodics.wait()
        self.polling_periodics = None


class PollingManager(agent.ConfigManagerBase):
    """Polling Manager to handle polling definition"""

    def __init__(self, conf):
        """Setup the polling according to config.

        The configuration is supported as follows:

        {"sources": [{"name": source_1,
                      "interval": interval_time,
                      "meters" : ["meter_1", "meter_2"],
                      "resources": ["resource_uri1", "resource_uri2"],
                     },
                     {"name": source_2,
                      "interval": interval_time,
                      "meters" : ["meter_3"],
                     },
                    ]}
        }

        The interval determines the cadence of sample polling

        Valid meter format is '*', '!meter_name', or 'meter_name'.
        '*' is wildcard symbol means any meters; '!meter_name' means
        "meter_name" will be excluded; 'meter_name' means 'meter_name'
        will be included.

        Valid meters definition is all "included meter names", all
        "excluded meter names", wildcard and "excluded meter names", or
        only wildcard.

        The resources is list of URI indicating the resources from where
        the meters should be polled. It's optional and it's up to the
        specific pollster to decide how to use it.

        """
        super().__init__(conf)
        cfg = self.load_config(conf.polling.cfg_file)
        self.sources = []
        if 'sources' not in cfg:
            raise PollingException("sources required", cfg)
        for s in cfg.get('sources'):
            self.sources.append(PollingSource(s))


class PollingSource(agent.Source):
    """Represents a source of pollsters

    In effect it is a set of pollsters emitting
    samples for a set of matching meters. Each source encapsulates meter name
    matching, polling interval determination, optional resource enumeration or
    discovery.
    """

    def __init__(self, cfg):
        try:
            super().__init__(cfg)
        except agent.SourceException as err:
            raise PollingException(err.msg, cfg)
        try:
            self.meters = cfg['meters']
        except KeyError:
            raise PollingException("Missing meters value", cfg)
        try:
            self.interval = int(cfg['interval'])
        except ValueError:
            raise PollingException("Invalid interval value", cfg)
        except KeyError:
            raise PollingException("Missing interval value", cfg)
        if self.interval <= 0:
            raise PollingException("Interval value should > 0", cfg)

        self.resources = cfg.get('resources') or []
        if not isinstance(self.resources, list):
            raise PollingException("Resources should be a list", cfg)

        self.discovery = cfg.get('discovery') or []
        if not isinstance(self.discovery, list):
            raise PollingException("Discovery should be a list", cfg)
        try:
            self.check_source_filtering(self.meters, 'meters')
        except agent.SourceException as err:
            raise PollingException(err.msg, cfg)

        self.group_id_coordination_expression = cfg.get(
            'group_id_coordination_expression')

        # This value is configured when coordination is enabled.
        self.group_for_coordination = None

    def get_interval(self):
        return self.interval

    def support_meter(self, meter_name):
        return self.is_supported(self.meters, meter_name)
