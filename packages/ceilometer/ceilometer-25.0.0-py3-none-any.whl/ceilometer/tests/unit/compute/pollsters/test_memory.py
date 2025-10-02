# Copyright (c) 2014 VMware, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from unittest import mock

from ceilometer.compute.pollsters import instance_stats
from ceilometer.compute.virt import inspector as virt_inspector
from ceilometer.polling import manager
from ceilometer.tests.unit.compute.pollsters import base


class TestMemoryPollster(base.TestPollsterBase):

    def test_get_samples(self):
        self._mock_inspect_instance(
            virt_inspector.InstanceStats(memory_actual=1024.0),
            virt_inspector.InstanceStats(memory_actual=2048.0),
            virt_inspector.InstanceStats(),
            virt_inspector.InstanceShutOffException(),
        )

        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.MemoryPollster(self.CONF)

        @mock.patch('ceilometer.compute.pollsters.LOG')
        def _verify_memory_metering(expected_count, expected_memory_mb,
                                    expected_warnings, mylog):
            samples = list(pollster.get_samples(mgr, {}, [self.instance]))
            self.assertEqual(expected_count, len(samples))
            if expected_count > 0:
                self.assertEqual({'memory'},
                                 {s.name for s in samples})
                self.assertEqual(expected_memory_mb, samples[0].volume)
            else:
                self.assertEqual(expected_warnings, mylog.warning.call_count)
            self.assertEqual(0, mylog.exception.call_count)

        _verify_memory_metering(1, 1024.0, 0)
        _verify_memory_metering(1, 2048.0, 0)
        _verify_memory_metering(0, 0, 1)
        _verify_memory_metering(0, 0, 0)

    def test_get_samples_with_empty_stats(self):

        self._mock_inspect_instance(virt_inspector.NoDataException())
        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.MemoryPollster(self.CONF)

        def all_samples():
            return list(pollster.get_samples(mgr, {}, [self.instance]))


class TestMemoryAvailablePollster(base.TestPollsterBase):

    def test_get_samples(self):
        self._mock_inspect_instance(
            virt_inspector.InstanceStats(memory_available=1024.0),
            virt_inspector.InstanceStats(memory_available=2048.0),
            virt_inspector.InstanceStats(),
            virt_inspector.InstanceShutOffException(),
        )

        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.MemoryAvailablePollster(self.CONF)

        @mock.patch('ceilometer.compute.pollsters.LOG')
        def _verify_memory_available_metering(expected_count,
                                              expected_memory_mb,
                                              expected_warnings,
                                              mylog):
            samples = list(pollster.get_samples(mgr, {}, [self.instance]))
            self.assertEqual(expected_count, len(samples))
            if expected_count > 0:
                self.assertEqual({'memory.available'},
                                 {s.name for s in samples})
                self.assertEqual(expected_memory_mb, samples[0].volume)
            else:
                self.assertEqual(expected_warnings, mylog.warning.call_count)
            self.assertEqual(0, mylog.exception.call_count)

        _verify_memory_available_metering(1, 1024.0, 0)
        _verify_memory_available_metering(1, 2048.0, 0)
        _verify_memory_available_metering(0, 0, 1)
        _verify_memory_available_metering(0, 0, 0)

    def test_get_samples_with_empty_stats(self):

        self._mock_inspect_instance(virt_inspector.NoDataException())
        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.MemoryPollster(self.CONF)

        def all_samples():
            return list(pollster.get_samples(mgr, {}, [self.instance]))


class TestMemoryUsagePollster(base.TestPollsterBase):

    def test_get_samples(self):
        self._mock_inspect_instance(
            virt_inspector.InstanceStats(memory_usage=1.0),
            virt_inspector.InstanceStats(memory_usage=2.0),
            virt_inspector.InstanceStats(),
            virt_inspector.InstanceShutOffException(),
        )

        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.MemoryUsagePollster(self.CONF)

        @mock.patch('ceilometer.compute.pollsters.LOG')
        def _verify_memory_usage_metering(expected_count, expected_memory_mb,
                                          expected_warnings, mylog):
            samples = list(pollster.get_samples(mgr, {}, [self.instance]))
            self.assertEqual(expected_count, len(samples))
            if expected_count > 0:
                self.assertEqual({'memory.usage'},
                                 {s.name for s in samples})
                self.assertEqual(expected_memory_mb, samples[0].volume)
            else:
                self.assertEqual(expected_warnings, mylog.warning.call_count)
            self.assertEqual(0, mylog.exception.call_count)

        _verify_memory_usage_metering(1, 1.0, 0)
        _verify_memory_usage_metering(1, 2.0, 0)
        _verify_memory_usage_metering(0, 0, 1)
        _verify_memory_usage_metering(0, 0, 0)

    def test_get_samples_with_empty_stats(self):

        self._mock_inspect_instance(virt_inspector.NoDataException())
        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.MemoryUsagePollster(self.CONF)

        def all_samples():
            return list(pollster.get_samples(mgr, {}, [self.instance]))


class TestResidentMemoryPollster(base.TestPollsterBase):

    def test_get_samples(self):
        self._mock_inspect_instance(
            virt_inspector.InstanceStats(memory_resident=1.0),
            virt_inspector.InstanceStats(memory_resident=2.0),
            virt_inspector.InstanceStats(),
            virt_inspector.InstanceShutOffException(),
        )

        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.MemoryResidentPollster(self.CONF)

        @mock.patch('ceilometer.compute.pollsters.LOG')
        def _verify_resident_memory_metering(expected_count,
                                             expected_resident_memory_mb,
                                             expected_warnings, mylog):
            samples = list(pollster.get_samples(mgr, {}, [self.instance]))
            self.assertEqual(expected_count, len(samples))
            if expected_count > 0:
                self.assertEqual({'memory.resident'},
                                 {s.name for s in samples})
                self.assertEqual(expected_resident_memory_mb,
                                 samples[0].volume)
            else:
                self.assertEqual(expected_warnings, mylog.warning.call_count)
            self.assertEqual(0, mylog.exception.call_count)

        _verify_resident_memory_metering(1, 1.0, 0)
        _verify_resident_memory_metering(1, 2.0, 0)
        _verify_resident_memory_metering(0, 0, 1)
        _verify_resident_memory_metering(0, 0, 0)


class TestMemorySwapPollster(base.TestPollsterBase):

    def test_get_samples(self):
        self._mock_inspect_instance(
            virt_inspector.InstanceStats(memory_swap_in=1.0,
                                         memory_swap_out=2.0),
            virt_inspector.InstanceStats(memory_swap_in=3.0,
                                         memory_swap_out=4.0),
        )

        mgr = manager.AgentManager(0, self.CONF)

        def _check_memory_swap_in(expected_swap_in):
            pollster = instance_stats.MemorySwapInPollster(self.CONF)

            samples = list(pollster.get_samples(mgr, {}, [self.instance]))
            self.assertEqual(1, len(samples))
            self.assertEqual({'memory.swap.in'},
                             {s.name for s in samples})
            self.assertEqual(expected_swap_in, samples[0].volume)

        def _check_memory_swap_out(expected_swap_out):
            pollster = instance_stats.MemorySwapOutPollster(self.CONF)

            samples = list(pollster.get_samples(mgr, {}, [self.instance]))
            self.assertEqual(1, len(samples))
            self.assertEqual({'memory.swap.out'},
                             {s.name for s in samples})
            self.assertEqual(expected_swap_out, samples[0].volume)

        _check_memory_swap_in(1.0)
        _check_memory_swap_out(4.0)

    def test_get_samples_with_empty_stats(self):
        self._mock_inspect_instance(virt_inspector.NoDataException())
        mgr = manager.AgentManager(0, self.CONF)
        pollster = instance_stats.MemorySwapInPollster(self.CONF)

        def all_samples():
            return list(pollster.get_samples(mgr, {}, [self.instance]))
