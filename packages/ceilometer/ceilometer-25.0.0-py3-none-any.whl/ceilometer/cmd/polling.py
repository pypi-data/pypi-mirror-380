#
# Copyright 2014-2015 OpenStack Foundation
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

import multiprocessing
import shlex

import cotyledon
from cotyledon import oslo_config_glue
from oslo_config import cfg
from oslo_log import log
from oslo_privsep import priv_context

from ceilometer.polling import manager
from ceilometer import service
from ceilometer import utils

LOG = log.getLogger(__name__)


class MultiChoicesOpt(cfg.Opt):
    def __init__(self, name, choices=None, **kwargs):
        super().__init__(
            name, type=DeduplicatedCfgList(choices), **kwargs)
        self.choices = choices

    def _get_argparse_kwargs(self, group, **kwargs):
        """Extends the base argparse keyword dict for multi choices options."""
        kwargs = super()._get_argparse_kwargs(group)
        kwargs['nargs'] = '+'
        choices = kwargs.get('choices', self.choices)
        if choices:
            kwargs['choices'] = choices
        return kwargs


class DeduplicatedCfgList(cfg.types.List):
    def __init__(self, choices=None, **kwargs):
        super().__init__(**kwargs)
        self.choices = choices or []

    def __call__(self, *args, **kwargs):
        result = super().__call__(*args, **kwargs)
        result_set = set(result)
        if len(result) != len(result_set):
            LOG.warning("Duplicated values: %s found in CLI options, "
                        "auto de-duplicated", result)
            result = list(result_set)
        if self.choices and not (result_set <= set(self.choices)):
            raise Exception('Valid values are %s, but found %s'
                            % (self.choices, result))
        return result


CLI_OPTS = [
    MultiChoicesOpt('polling-namespaces',
                    default=['compute', 'central'],
                    dest='polling_namespaces',
                    help='Polling namespace(s) to be used while '
                         'resource polling')
]


def _prepare_config():
    conf = cfg.ConfigOpts()
    conf.register_cli_opts(CLI_OPTS)
    service.prepare_service(conf=conf)
    return conf


def create_polling_service(worker_id, conf=None, queue=None):
    if conf is None:
        conf = _prepare_config()
        conf.log_opt_values(LOG, log.DEBUG)
    return manager.AgentManager(worker_id, conf,
                                conf.polling_namespaces, queue)


def create_heartbeat_service(worker_id, conf, queue=None):
    if conf is None:
        conf = _prepare_config()
        conf.log_opt_values(LOG, log.DEBUG)
    return manager.AgentHeartBeatManager(worker_id, conf,
                                         conf.polling_namespaces, queue)


def main():
    sm = cotyledon.ServiceManager()
    conf = _prepare_config()
    priv_context.init(root_helper=shlex.split(utils.get_root_helper(conf)))
    oslo_config_glue.setup(sm, conf)

    if conf.polling.heartbeat_socket_dir is not None:
        queue = multiprocessing.Queue()
        sm.add(create_heartbeat_service, args=(conf, queue))
    else:
        queue = None
    sm.add(create_polling_service, args=(conf, queue))
    sm.run()
