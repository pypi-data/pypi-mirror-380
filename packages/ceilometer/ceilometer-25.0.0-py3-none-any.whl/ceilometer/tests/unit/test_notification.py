#
# Copyright 2012 New Dream Network, LLC (DreamHost)
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
"""Tests for Ceilometer notify daemon."""

import time
from unittest import mock

from oslo_utils import fileutils
import yaml

from ceilometer import messaging
from ceilometer import notification
from ceilometer.publisher import test as test_publisher
from ceilometer import service
from ceilometer.tests import base as tests_base

TEST_NOTICE_CTXT = {
    'auth_token': '3d8b13de1b7d499587dfc69b77dc09c2',
    'is_admin': True,
    'project_id': '7c150a59fe714e6f9263774af9688f0e',
    'quota_class': None,
    'read_deleted': 'no',
    'remote_address': '10.0.2.15',
    'request_id': 'req-d68b36e0-9233-467f-9afb-d81435d64d66',
    'roles': ['admin'],
    'timestamp': '2012-05-08T20:23:41.425105',
    'user_id': '1e3ce043029547f1a61c1996d1a531a2',
}

TEST_NOTICE_METADATA = {
    'message_id': 'dae6f69c-00e0-41c0-b371-41ec3b7f4451',
    'timestamp': '2012-05-08 20:23:48.028195',
}

TEST_NOTICE_PAYLOAD = {
    'created_at': '2012-05-08 20:23:41',
    'deleted_at': '',
    'disk_gb': 0,
    'display_name': 'testme',
    'fixed_ips': [{'address': '10.0.0.2',
                    'floating_ips': [],
                    'meta': {},
                    'type': 'fixed',
                    'version': 4}],
    'image_ref_url': 'http://10.0.2.15:9292/images/UUID',
    'instance_id': '9f9d01b9-4a58-4271-9e27-398b21ab20d1',
    'instance_type': 'm1.tiny',
    'instance_type_id': 2,
    'launched_at': '2012-05-08 20:23:47.985999',
    'memory_mb': 512,
    'state': 'active',
    'state_description': '',
    'tenant_id': '7c150a59fe714e6f9263774af9688f0e',
    'user_id': '1e3ce043029547f1a61c1996d1a531a2',
    'reservation_id': '1e3ce043029547f1a61c1996d1a531a3',
    'vcpus': 1,
    'root_gb': 0,
    'ephemeral_gb': 0,
    'host': 'compute-host-name',
    'availability_zone': '1e3ce043029547f1a61c1996d1a531a4',
    'os_type': 'linux?',
    'architecture': 'x86',
    'image_ref': 'UUID',
    'kernel_id': '1e3ce043029547f1a61c1996d1a531a5',
    'ramdisk_id': '1e3ce043029547f1a61c1996d1a531a6',
}


class BaseNotificationTest(tests_base.BaseTestCase):
    def run_service(self, srv):
        srv.run()
        self.addCleanup(srv.terminate)


class TestNotification(BaseNotificationTest):

    def setUp(self):
        super().setUp()
        self.CONF = service.prepare_service([], [])
        self.setup_messaging(self.CONF)
        self.srv = notification.NotificationService(0, self.CONF)

    def test_targets(self):
        self.assertEqual(14, len(self.srv.get_targets()))

    def test_start_multiple_listeners(self):
        urls = ["fake://vhost1", "fake://vhost2"]
        self.CONF.set_override("messaging_urls", urls, group="notification")
        self.srv.run()
        self.addCleanup(self.srv.terminate)
        self.assertEqual(2, len(self.srv.listeners))

    @mock.patch('oslo_messaging.get_batch_notification_listener')
    def test_unique_consumers(self, mock_listener):
        self.CONF.set_override('notification_control_exchanges', ['dup'] * 2,
                               group='notification')
        self.run_service(self.srv)
        # 1 target, 1 listener
        self.assertEqual(1, len(mock_listener.call_args_list[0][0][1]))
        self.assertEqual(1, len(self.srv.listeners))

    def test_select_pipelines(self):
        self.CONF.set_override('pipelines', ['event'], group='notification')
        self.srv.run()
        self.addCleanup(self.srv.terminate)
        self.assertEqual(1, len(self.srv.managers))
        self.assertEqual(1, len(self.srv.listeners[0].dispatcher.endpoints))

    @mock.patch('ceilometer.notification.LOG')
    def test_select_pipelines_missing(self, logger):
        self.CONF.set_override('pipelines', ['meter', 'event', 'bad'],
                               group='notification')
        self.srv.run()
        self.addCleanup(self.srv.terminate)
        self.assertEqual(2, len(self.srv.managers))
        logger.error.assert_called_with(
            'Could not load the following pipelines: %s', {'bad'})


class BaseRealNotification(BaseNotificationTest):
    def setup_pipeline(self, counter_names):
        pipeline = yaml.dump({
            'sources': [{
                'name': 'test_pipeline',
                'interval': 5,
                'meters': counter_names,
                'sinks': ['test_sink']
            }],
            'sinks': [{
                'name': 'test_sink',
                'publishers': ['test://']
            }]
        })
        pipeline = pipeline.encode('utf-8')

        pipeline_cfg_file = fileutils.write_to_tempfile(content=pipeline,
                                                        prefix="pipeline",
                                                        suffix="yaml")
        return pipeline_cfg_file

    def setup_event_pipeline(self, event_names):
        ev_pipeline = yaml.dump({
            'sources': [{
                'name': 'test_event',
                'events': event_names,
                'sinks': ['test_sink']
            }],
            'sinks': [{
                'name': 'test_sink',
                'publishers': ['test://']
            }]
        })
        ev_pipeline = ev_pipeline.encode('utf-8')

        ev_pipeline_cfg_file = fileutils.write_to_tempfile(
            content=ev_pipeline, prefix="event_pipeline", suffix="yaml")
        return ev_pipeline_cfg_file

    def setUp(self):
        super().setUp()
        self.CONF = service.prepare_service([], [])
        self.setup_messaging(self.CONF, 'nova')

        pipeline_cfg_file = self.setup_pipeline(['vcpus', 'memory'])
        self.CONF.set_override("pipeline_cfg_file", pipeline_cfg_file)

        self.expected_samples = 2

        ev_pipeline_cfg_file = self.setup_event_pipeline(
            ['compute.instance.*'])
        self.expected_events = 1

        self.CONF.set_override("event_pipeline_cfg_file",
                               ev_pipeline_cfg_file)

        self.publisher = test_publisher.TestPublisher(self.CONF, "")

    def _check_notification_service(self):
        self.run_service(self.srv)
        notifier = messaging.get_notifier(self.transport,
                                          "compute.vagrant-precise")
        notifier.info({}, 'compute.instance.create.end',
                      TEST_NOTICE_PAYLOAD)
        start = time.time()
        while time.time() - start < 60:
            if (len(self.publisher.samples) >= self.expected_samples and
                    len(self.publisher.events) >= self.expected_events):
                break

        resources = list({s.resource_id for s in self.publisher.samples})
        self.assertEqual(self.expected_samples, len(self.publisher.samples))
        self.assertEqual(self.expected_events, len(self.publisher.events))
        self.assertEqual(["9f9d01b9-4a58-4271-9e27-398b21ab20d1"], resources)


class TestRealNotification(BaseRealNotification):

    def setUp(self):
        super().setUp()
        self.srv = notification.NotificationService(0, self.CONF)

    @mock.patch('ceilometer.publisher.test.TestPublisher')
    def test_notification_service(self, fake_publisher_cls):
        fake_publisher_cls.return_value = self.publisher
        self._check_notification_service()

    @mock.patch('ceilometer.publisher.test.TestPublisher')
    def test_notification_service_error_topic(self, fake_publisher_cls):
        fake_publisher_cls.return_value = self.publisher
        self.run_service(self.srv)
        notifier = messaging.get_notifier(self.transport,
                                          'compute.vagrant-precise')
        notifier.error({}, 'compute.instance.error',
                       TEST_NOTICE_PAYLOAD)
        start = time.time()
        while time.time() - start < 60:
            if len(self.publisher.events) >= self.expected_events:
                break
        self.assertEqual(self.expected_events, len(self.publisher.events))
