#
# Copyright 2012 eNovance <licensing@enovance.com>
# Copyright 2012 Red Hat, Inc
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

import time

from ceilometer.compute.pollsters import instance_stats
from ceilometer.compute.virt import inspector as virt_inspector
from ceilometer.polling import manager
from ceilometer.tests.unit.compute.pollsters import base


class TestCPUPollster(base.TestPollsterBase):

    def test_get_samples(self):
        self._mock_inspect_instance(
            virt_inspector.InstanceStats(cpu_time=1 * (10 ** 6), cpu_number=2),
            virt_inspector.InstanceStats(cpu_time=3 * (10 ** 6), cpu_number=2),
            # cpu_time resets on instance restart
            virt_inspector.InstanceStats(cpu_time=2 * (10 ** 6), cpu_number=2),
        )

        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.CPUPollster(self.CONF)

        def _verify_cpu_metering(expected_time):
            cache = {}
            samples = list(pollster.get_samples(mgr, cache, [self.instance]))
            self.assertEqual(1, len(samples))
            self.assertEqual({'cpu'}, {s.name for s in samples})
            self.assertEqual(expected_time, samples[0].volume)
            self.assertEqual(2, samples[0].resource_metadata.get('cpu_number'))
            # ensure elapsed time between polling cycles is non-zero
            time.sleep(0.001)

        _verify_cpu_metering(1 * (10 ** 6))
        _verify_cpu_metering(3 * (10 ** 6))
        _verify_cpu_metering(2 * (10 ** 6))

    # the following apply to all instance resource pollsters but are tested
    # here alone.

    def test_get_metadata(self):
        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.CPUPollster(self.CONF)
        samples = list(pollster.get_samples(mgr, {}, [self.instance]))
        self.assertEqual(1, len(samples))
        self.assertEqual(1, samples[0].resource_metadata['vcpus'])
        self.assertEqual(512, samples[0].resource_metadata['memory_mb'])
        self.assertEqual(20, samples[0].resource_metadata['disk_gb'])
        self.assertEqual(20, samples[0].resource_metadata['root_gb'])
        self.assertEqual(0, samples[0].resource_metadata['ephemeral_gb'])
        self.assertEqual('active', samples[0].resource_metadata['status'])
        self.assertEqual('active', samples[0].resource_metadata['state'])
        self.assertIsNone(samples[0].resource_metadata['task_state'])
        self.assertEqual(self.instance.flavor,
                         samples[0].resource_metadata['flavor'])
        self.assertEqual(self.instance.image['id'],
                         samples[0].resource_metadata['image_ref'])
        self.assertEqual(self.instance.image_meta,
                         samples[0].resource_metadata['image_meta'])

    def test_get_reserved_metadata_with_keys(self):
        self.CONF.set_override('reserved_metadata_keys', ['fqdn'])

        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.CPUPollster(self.CONF)
        samples = list(pollster.get_samples(mgr, {}, [self.instance]))
        self.assertEqual({'fqdn': 'vm_fqdn',
                          'stack': '2cadc4b4-8789-123c-b4eg-edd2f0a9c128'},
                         samples[0].resource_metadata['user_metadata'])

    def test_get_reserved_metadata_with_namespace(self):
        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.CPUPollster(self.CONF)
        samples = list(pollster.get_samples(mgr, {}, [self.instance]))
        self.assertEqual({'stack': '2cadc4b4-8789-123c-b4eg-edd2f0a9c128'},
                         samples[0].resource_metadata['user_metadata'])

        self.CONF.set_override('reserved_metadata_namespace', [])
        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.CPUPollster(self.CONF)
        samples = list(pollster.get_samples(mgr, {}, [self.instance]))
        self.assertNotIn('user_metadata', samples[0].resource_metadata)

    def test_get_flavor_name_as_metadata_instance_type(self):
        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.CPUPollster(self.CONF)
        samples = list(pollster.get_samples(mgr, {}, [self.instance]))
        self.assertEqual(1, len(samples))
        self.assertEqual('m1.small',
                         samples[0].resource_metadata['instance_type'])


class TestVCPUsPollster(base.TestPollsterBase):

    def test_get_samples(self):
        self._mock_inspect_instance(
            virt_inspector.InstanceStats(cpu_time=1 * (10 ** 6), cpu_number=1),
            virt_inspector.InstanceStats(cpu_time=3 * (10 ** 6), cpu_number=1),
            # cpu_time resets on instance restart
            virt_inspector.InstanceStats(cpu_time=2 * (10 ** 6), cpu_number=2),
        )

        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.VCPUsPollster(self.CONF)

        def _verify_cpu_metering(expected_cpu_number):
            cache = {}
            samples = list(pollster.get_samples(mgr, cache, [self.instance]))
            self.assertEqual(1, len(samples))
            self.assertEqual({'vcpus'}, {s.name for s in samples})
            self.assertEqual(expected_cpu_number, samples[0].volume)
            # ensure elapsed time between polling cycles is non-zero
            time.sleep(0.001)

        _verify_cpu_metering(1)
        _verify_cpu_metering(1)
        _verify_cpu_metering(2)
