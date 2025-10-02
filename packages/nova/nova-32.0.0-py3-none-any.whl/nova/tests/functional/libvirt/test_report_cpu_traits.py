# Copyright (c) 2018 Intel, Inc.
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

import builtins
import contextlib
import os.path
from unittest import mock

import os_resource_classes as orc
import os_traits as ost
from oslo_utils import versionutils

from nova import conf
from nova.db import constants as db_const
from nova import test
from nova.tests.fixtures import libvirt as fakelibvirt
from nova.tests.functional.libvirt import integrated_helpers
from nova.virt.libvirt import host as libvirt_host

CONF = conf.CONF


class LibvirtReportTraitsTestBase(
        integrated_helpers.LibvirtProviderUsageBaseTestCase):

    def assertMemEncryptionSlotsEqual(self, rp_uuid, slots):
        inventory = self._get_provider_inventory(rp_uuid)
        if slots == 0:
            self.assertNotIn(orc.MEM_ENCRYPTION_CONTEXT, inventory)
        else:
            self.assertEqual(
                {
                    'total': slots,
                    'min_unit': 1,
                    'max_unit': 1,
                    'step_size': 1,
                    'allocation_ratio': 1.0,
                    'reserved': 0,
                },
                inventory[orc.MEM_ENCRYPTION_CONTEXT]
            )

    def _get_amd_sev_rps(self):
        root_rp = self._get_resource_provider_by_uuid(self.host_uuid)
        rps = self._get_all_rps_in_a_tree(self.host_uuid)
        return {
            'sev': [rp for rp in rps
                    if rp['name'] == '%s_amd_sev' % root_rp['name']],
            'sev-es': [rp for rp in rps
                       if rp['name'] == '%s_amd_sev_es' % root_rp['name']]
        }

    @contextlib.contextmanager
    def _patch_sev_exists(self, sev, sev_es):
        real_exists = os.path.exists

        def fake_exists(path):
            if path == libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev':
                return sev
            elif path == libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev_es':
                return sev_es
            return real_exists(path)

        with mock.patch('os.path.exists') as mock_exists:
            mock_exists.side_effect = fake_exists
            yield mock_exists

    @contextlib.contextmanager
    def _patch_sev_open(self):
        real_open = builtins.open
        sev_open = mock.mock_open(read_data='1\n')
        sev_es_open = mock.mock_open(read_data='1\n')

        def fake_open(path, *args, **kwargs):
            if path == libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev':
                return sev_open(path)
            elif path == libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev_es':
                return sev_es_open(path)
            return real_open(path, *args, **kwargs)

        with mock.patch('builtins.open') as mock_open:
            mock_open.side_effect = fake_open
            yield mock_open


class LibvirtReportTraitsTests(LibvirtReportTraitsTestBase):
    # These must match the capabilities in
    # nova.virt.libvirt.driver.LibvirtDriver.capabilities
    expected_libvirt_driver_capability_traits = set([
        trait for trait in [
            ost.COMPUTE_ACCELERATORS,
            ost.COMPUTE_DEVICE_TAGGING,
            ost.COMPUTE_NET_ATTACH_INTERFACE,
            ost.COMPUTE_NET_ATTACH_INTERFACE_WITH_TAG,
            ost.COMPUTE_VOLUME_ATTACH_WITH_TAG,
            ost.COMPUTE_VOLUME_EXTEND,
            ost.COMPUTE_VOLUME_MULTI_ATTACH,
            ost.COMPUTE_TRUSTED_CERTS,
            ost.COMPUTE_IMAGE_TYPE_AKI,
            ost.COMPUTE_IMAGE_TYPE_AMI,
            ost.COMPUTE_IMAGE_TYPE_ARI,
            ost.COMPUTE_IMAGE_TYPE_ISO,
            ost.COMPUTE_IMAGE_TYPE_QCOW2,
            ost.COMPUTE_IMAGE_TYPE_RAW,
            ost.COMPUTE_RESCUE_BFV,
        ]
    ])

    def test_report_cpu_traits(self):
        self.assertEqual([], self._get_all_providers())
        self.start_compute()

        # Test CPU traits reported on initial node startup, these specific
        # trait values are coming from fakelibvirt's baselineCPU result.
        # COMPUTE_NODE is always set on the compute node provider.
        traits = self._get_provider_traits(self.host_uuid)
        for trait in (
            'HW_CPU_X86_VMX', 'HW_CPU_X86_INTEL_VMX', 'HW_CPU_X86_AESNI',
            'COMPUTE_NODE',
        ):
            self.assertIn(trait, traits)

        self._create_trait('CUSTOM_TRAITS')
        new_traits = ['CUSTOM_TRAITS', 'HW_CPU_X86_AVX']
        self._set_provider_traits(self.host_uuid, new_traits)
        # The above is an out-of-band placement operation, as if the operator
        # used the CLI. So now we have to "SIGHUP the compute process" to clear
        # the report client cache so the subsequent update picks up the change.
        self.compute.manager.reset()
        self._run_periodics()
        # HW_CPU_X86_AVX is filtered out because nova-compute owns CPU traits
        # and it's not in the baseline for the host.
        traits = set(self._get_provider_traits(self.host_uuid))
        expected_traits = self.expected_libvirt_driver_capability_traits.union(
            [
                'HW_CPU_X86_VMX',
                'HW_CPU_X86_INTEL_VMX',
                'HW_CPU_X86_AESNI',
                'CUSTOM_TRAITS',
                # The periodic restored the COMPUTE_NODE trait.
                'COMPUTE_NODE',
            ])
        for trait in expected_traits:
            self.assertIn(trait, traits)


class LibvirtReportNoSevTraitsTests(LibvirtReportTraitsTestBase):
    STUB_INIT_HOST = False

    def setUp(self):
        with self._patch_sev_exists(False, False):
            super(LibvirtReportNoSevTraitsTests, self).setUp()
            self.start_compute()

    def test_sev_trait_off_on(self):
        """Test that the compute service reports the SEV/SEV-ES trait in
        the list of global traits, but doesn't immediately register it on the
        compute host resource provider in the placement API, due to
        the kvm-amd kernel module's sev/sev-es parameter file being (mocked
        as) absent.

        Then test that if the SEV/SEV-ES capability appears (again via
        mocking), after a restart of the compute service, the trait
        gets registered on the compute host.

        Also test that on both occasions, the inventory of the
        MEM_ENCRYPTION_CONTEXT resource class on the compute host
        corresponds to the absence or presence of the SEV/SEV-ES capability.
        """
        self.assertFalse(self.compute.driver._host.supports_amd_sev)
        self.assertFalse(self.compute.driver._host.supports_amd_sev_es)

        global_traits = self._get_all_traits()
        self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

        traits = self._get_provider_traits(self.host_uuid)
        self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
        self.assertNotIn(ost.HW_CPU_X86_AMD_SEV_ES, traits)
        self.assertMemEncryptionSlotsEqual(self.host_uuid, 0)

        sev_rps = self._get_amd_sev_rps()
        self.assertEqual(0, len(sev_rps['sev']))
        self.assertEqual(0, len(sev_rps['sev-es']))

        # Now simulate the host gaining SEV functionality.  Here we
        # simulate a kernel update or reconfiguration which causes the
        # kvm-amd kernel module's "sev" parameter to become available
        # and set to 1, however it could also happen via a libvirt
        # upgrade, for instance.
        sev_features = (fakelibvirt.virConnect.
                        _domain_capability_features_with_SEV)
        with test.nested(
                self._patch_sev_exists(True, False),
                self._patch_sev_open(),
                mock.patch.object(fakelibvirt.virConnect,
                                  '_domain_capability_features',
                                  new=sev_features)
        ) as (mock_exists, mock_open, mock_features):
            # Retrigger the detection code.  In the real world this
            # would be a restart of the compute service.
            # As we are changing the domain caps we need to clear the
            # cache in the host object.
            self.compute.driver._host._domain_caps = None
            self.compute.driver._host._supports_amd_sev = None
            self.compute.driver._host._supports_amd_sev_es = None
            self.assertTrue(self.compute.driver._host.supports_amd_sev)
            self.assertFalse(self.compute.driver._host.supports_amd_sev_es)

            mock_exists.assert_has_calls([
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev'),
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev_es')
            ])
            mock_open.assert_has_calls([
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev')
            ])

            # However it won't disappear in the provider tree and get synced
            # back to placement until we force a reinventory:
            self.compute.manager.reset()
            # reset cached traits so they are recalculated.
            self.compute.driver._static_traits = None
            self._run_periodics()

            # Sanity check that we've still got the trait globally.
            global_traits = self._get_all_traits()
            self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
            self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

            # sev capabilities are managed by sub rp and are not present in
            # root rp
            traits = self._get_provider_traits(self.host_uuid)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV_ES, traits)
            self.assertMemEncryptionSlotsEqual(self.host_uuid, 0)

            sev_rps = self._get_amd_sev_rps()
            self.assertEqual(1, len(sev_rps['sev']))
            sev_rp_uuid = sev_rps['sev'][0]['uuid']
            sev_rp_traits = self._get_provider_traits(sev_rp_uuid)
            self.assertIn(ost.HW_CPU_X86_AMD_SEV, sev_rp_traits)
            self.assertMemEncryptionSlotsEqual(sev_rp_uuid, db_const.MAX_INT)

            self.assertEqual(0, len(sev_rps['sev-es']))

        # Now simulate the host gaining SEV-ES functionality.  Here we
        # simulate a kernel update or reconfiguration which causes the
        # kvm-amd kernel module's "sev-es" parameter to become available
        # and set to 1
        sev_features = (fakelibvirt.virConnect.
                        _domain_capability_features_with_SEV_max_guests)
        with test.nested(
                self._patch_sev_exists(True, True),
                self._patch_sev_open(),
                mock.patch.object(fakelibvirt.virConnect,
                                  '_domain_capability_features',
                                  new=sev_features),
                mock.patch.object(
                    fakelibvirt.Connection, 'getVersion',
                    return_value=versionutils.convert_version_to_int(
                    libvirt_host.MIN_QEMU_SEV_ES_VERSION))
        ) as (mock_exists, mock_open, mock_features, mock_get_version):
            # Retrigger the detection code.  In the real world this
            # would be a restart of the compute service.
            # As we are changing the domain caps we need to clear the
            # cache in the host object.
            self.compute.driver._host._domain_caps = None
            self.compute.driver._host._supports_amd_sev = None
            self.compute.driver._host._supports_amd_sev_es = None
            self.assertTrue(self.compute.driver._host.supports_amd_sev)
            self.assertTrue(self.compute.driver._host.supports_amd_sev_es)

            mock_exists.assert_has_calls([
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev'),
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev_es')
            ])
            mock_open.assert_has_calls([
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev'),
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev_es')
            ])

            # However it won't disappear in the provider tree and get synced
            # back to placement until we force a reinventory:
            self.compute.manager.reset()
            # reset cached traits so they are recalculated.
            self.compute.driver._static_traits = None
            self._run_periodics()

            # Sanity check that we've still got the trait globally.
            global_traits = self._get_all_traits()
            self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
            self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

            # sev capabilities are managed by sub rp and are not present in
            # root rp
            traits = self._get_provider_traits(self.host_uuid)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV_ES, traits)
            self.assertMemEncryptionSlotsEqual(self.host_uuid, 0)

            sev_rps = self._get_amd_sev_rps()

            self.assertEqual(1, len(sev_rps['sev']))
            sev_rp_uuid = sev_rps['sev'][0]['uuid']
            sev_rp_traits = self._get_provider_traits(sev_rp_uuid)
            self.assertIn(ost.HW_CPU_X86_AMD_SEV, sev_rp_traits)
            self.assertMemEncryptionSlotsEqual(sev_rp_uuid, 100)

            self.assertEqual(1, len(sev_rps['sev-es']))
            sev_es_rp_uuid = sev_rps['sev-es'][0]['uuid']
            sev_es_rp_traits = self._get_provider_traits(sev_es_rp_uuid)
            self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, sev_es_rp_traits)
            self.assertMemEncryptionSlotsEqual(sev_es_rp_uuid, 15)


class LibvirtReportSevTraitsTests(LibvirtReportTraitsTestBase):
    STUB_INIT_HOST = False

    def setUp(self):
        super(LibvirtReportSevTraitsTests, self).setUp()

    def _init_compute(self, sev, sev_es):
        sev_features = (fakelibvirt.virConnect.
                        _domain_capability_features_with_SEV_max_guests)
        with test.nested(
                self._patch_sev_exists(sev, sev_es),
                self._patch_sev_open(),
                mock.patch.object(fakelibvirt.virConnect,
                                  '_domain_capability_features',
                                  new=sev_features),
                mock.patch.object(
                    fakelibvirt.Connection, 'getVersion',
                    return_value=versionutils.convert_version_to_int(
                    libvirt_host.MIN_QEMU_SEV_ES_VERSION))
        ) as (mock_exists, mock_open, mock_features, mock_get_version):
            self.start_compute()

    def test_sev_trait_on_off(self):
        """Test that the compute service reports the SEV trait in
        the list of global traits, and immediately registers it on the compute
        host resource provider in the placement API, due to the SEV
        capability being (mocked as) present.

        Then test that if the SEV capability disappears (again via mocking),
        after a restart of the compute service, the trait gets removed from
        the compute host.

        Also test that on both occasions, the inventory of the
        MEM_ENCRYPTION_CONTEXT resource class on the compute host
        corresponds to the absence or presence of the SEV capability.
        """
        self._init_compute(True, False)

        # Make sure that SEV is enabled but SEV-ES is not enabled
        self.assertTrue(self.compute.driver._host.supports_amd_sev)
        self.assertFalse(self.compute.driver._host.supports_amd_sev_es)

        global_traits = self._get_all_traits()
        self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

        # sev capabilities are managed by sub rp and are not present in root rp
        traits = self._get_provider_traits(self.host_uuid)
        self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
        self.assertMemEncryptionSlotsEqual(self.host_uuid, 0)

        sev_rps = self._get_amd_sev_rps()

        self.assertEqual(1, len(sev_rps['sev']))
        sev_rp_uuid = sev_rps['sev'][0]['uuid']
        sev_rp_traits = self._get_provider_traits(sev_rp_uuid)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV, sev_rp_traits)
        self.assertMemEncryptionSlotsEqual(sev_rp_uuid, 100)

        self.assertEqual(0, len(sev_rps['sev-es']))

        # Now simulate the host losing SEV functionality.  Here we
        # simulate a kernel downgrade or reconfiguration which causes
        # the kvm-amd kernel module's "sev-" parameter to become
        # unavailable.
        sev_features = (fakelibvirt.virConnect.
                        _domain_capability_features_with_SEV)
        with test.nested(
                self._patch_sev_exists(False, False),
                self._patch_sev_open(),
                mock.patch.object(fakelibvirt.virConnect,
                                  '_domain_capability_features',
                                  new=sev_features)
        ) as (mock_exists, mock_open, mock_features):
            # Retrigger the detection code.  In the real world this
            # would be a restart of the compute service.
            self.compute.driver._host._domain_caps = None
            self.compute.driver._host._supports_amd_sev = None
            self.compute.driver._host._supports_amd_sev_es = None
            self.assertFalse(self.compute.driver._host.supports_amd_sev)
            self.assertFalse(self.compute.driver._host.supports_amd_sev_es)

            mock_exists.assert_has_calls([
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev'),
            ])

            # However it won't disappear in the provider tree and get synced
            # back to placement until we force a reinventory:
            self.compute.manager.reset()
            # reset cached traits so they are recalculated.
            self.compute.driver._static_traits = None
            self._run_periodics()

            # Sanity check that we've still got the trait globally.
            global_traits = self._get_all_traits()
            self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
            self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

            traits = self._get_provider_traits(self.host_uuid)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV_ES, traits)

            sev_rps = self._get_amd_sev_rps()
            self.assertEqual(0, len(sev_rps['sev']))
            self.assertEqual(0, len(sev_rps['sev-es']))

    def test_sev_es_trait_on_off(self):
        """Test that the compute service reports the SEV-ES trait in
        the list of global traits, and immediately registers it on the compute
        host resource provider in the placement API, due to the SEV-ES
        capability being (mocked as) present.

        Then test that if the SEV-ES capability disappears (again via
        mocking), after a restart of the compute service, the trait
        gets removed from the compute host.

        Also test that on both occasions, the inventory of the
        MEM_ENCRYPTION_CONTEXT resource class on the compute host
        corresponds to the absence or presence of the SEV-ES capability.
        """
        self._init_compute(True, True)

        # Make sure that both SEV and SEV-ES are enabled
        self.assertTrue(self.compute.driver._host.supports_amd_sev)
        self.assertTrue(self.compute.driver._host.supports_amd_sev_es)

        global_traits = self._get_all_traits()
        self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

        # sev capabilities are managed by sub rp and are not present in root rp
        traits = self._get_provider_traits(self.host_uuid)
        self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
        self.assertMemEncryptionSlotsEqual(self.host_uuid, 0)

        sev_rps = self._get_amd_sev_rps()

        self.assertEqual(1, len(sev_rps['sev']))
        sev_rp_uuid = sev_rps['sev'][0]['uuid']
        sev_rp_traits = self._get_provider_traits(sev_rp_uuid)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV, sev_rp_traits)
        self.assertMemEncryptionSlotsEqual(sev_rp_uuid, 100)

        self.assertEqual(1, len(sev_rps['sev-es']))
        sev_es_rp_uuid = sev_rps['sev-es'][0]['uuid']
        sev_es_rp_traits = self._get_provider_traits(sev_es_rp_uuid)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, sev_es_rp_traits)
        self.assertMemEncryptionSlotsEqual(sev_es_rp_uuid, 15)
        self.assertEqual(1, len(sev_rps['sev']))

        # Now simulate the host losing SEV-ES functionality.  Here we
        # simulate a kernel downgrade or reconfiguration which causes
        # the kvm-amd kernel module's "sev-es" parameter to become
        # unavailable, however it could also happen via a libvirt
        # downgrade, for instance.
        sev_features = (fakelibvirt.virConnect.
                        _domain_capability_features_with_SEV)
        with test.nested(
                self._patch_sev_exists(True, False),
                self._patch_sev_open(),
                mock.patch.object(fakelibvirt.virConnect,
                                  '_domain_capability_features',
                                  new=sev_features)
        ) as (mock_exists, mock_open, mock_features):
            # Retrigger the detection code.  In the real world this
            # would be a restart of the compute service.
            self.compute.driver._host._domain_caps = None
            self.compute.driver._host._supports_amd_sev = None
            self.compute.driver._host._supports_amd_sev_es = None
            self.assertTrue(self.compute.driver._host.supports_amd_sev)
            self.assertFalse(self.compute.driver._host.supports_amd_sev_es)

            mock_exists.assert_has_calls([
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev'),
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev_es')
            ])
            mock_open.assert_has_calls([
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev')
            ])

            # However it won't disappear in the provider tree and get synced
            # back to placement until we force a reinventory:
            self.compute.manager.reset()
            # reset cached traits so they are recalculated.
            self.compute.driver._static_traits = None
            self._run_periodics()

            # Sanity check that we've still got the trait globally.
            global_traits = self._get_all_traits()
            self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
            self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

            traits = self._get_provider_traits(self.host_uuid)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV_ES, traits)

            sev_rps = self._get_amd_sev_rps()
            self.assertEqual(1, len(sev_rps['sev']))
            self.assertEqual(0, len(sev_rps['sev-es']))

    def test_sev_all_trait_on_off(self):
        """Test that the compute service reports the SEV/SEV-ES trait in
        the list of global traits, and immediately registers it on the compute
        host resource provider in the placement API, due to the SEV/SEV-ES
        capability being (mocked as) present.

        Then test that if the SEV/SEV-ES capability disappears (again via
        mocking), after a restart of the compute service, the trait
        gets removed from the compute host.

        Also test that on both occasions, the inventory of the
        MEM_ENCRYPTION_CONTEXT resource class on the compute host
        corresponds to the absence or presence of the SEV/SEV-ES capability.
        """
        self._init_compute(True, True)

        # Make sure that both SEV and SEV-ES are enabled
        self.assertTrue(self.compute.driver._host.supports_amd_sev)
        self.assertTrue(self.compute.driver._host.supports_amd_sev_es)
        global_traits = self._get_all_traits()
        self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

        # sev capabilities are managed by sub rp and are not present in root rp
        traits = self._get_provider_traits(self.host_uuid)
        self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
        self.assertMemEncryptionSlotsEqual(self.host_uuid, 0)

        sev_rps = self._get_amd_sev_rps()

        self.assertEqual(1, len(sev_rps['sev']))
        sev_rp_uuid = sev_rps['sev'][0]['uuid']
        sev_rp_traits = self._get_provider_traits(sev_rp_uuid)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV, sev_rp_traits)
        self.assertMemEncryptionSlotsEqual(sev_rp_uuid, 100)

        self.assertEqual(1, len(sev_rps['sev-es']))
        sev_es_rp_uuid = sev_rps['sev-es'][0]['uuid']
        sev_es_rp_traits = self._get_provider_traits(sev_es_rp_uuid)
        self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, sev_es_rp_traits)
        self.assertMemEncryptionSlotsEqual(sev_es_rp_uuid, 15)
        self.assertEqual(1, len(sev_rps['sev']))

        # Now simulate the host losing SEV/SEV-ES functionality.  Here we
        # simulate a kernel downgrade or reconfiguration which causes
        # the kvm-amd kernel module's "sev" parameter and "sev-es" parameter
        # to become unavailable, however it could also happen via a libvirt
        # downgrade, for instance.
        sev_features = (fakelibvirt.virConnect.
                        _domain_capability_features_with_SEV)
        with test.nested(
                self._patch_sev_exists(False, False),
                self._patch_sev_open(),
                mock.patch.object(fakelibvirt.virConnect,
                                  '_domain_capability_features',
                                  new=sev_features)
        ) as (mock_exists, mock_open, mock_features):
            # Retrigger the detection code.  In the real world this
            # would be a restart of the compute service.
            self.compute.driver._host._domain_caps = None
            self.compute.driver._host._supports_amd_sev = None
            self.compute.driver._host._supports_amd_sev_es = None
            self.assertFalse(self.compute.driver._host.supports_amd_sev)
            self.assertFalse(self.compute.driver._host.supports_amd_sev_es)

            mock_exists.assert_has_calls([
                mock.call(libvirt_host.SEV_KERNEL_PARAM_FILE % 'sev'),
            ])

            # However it won't disappear in the provider tree and get synced
            # back to placement until we force a reinventory:
            self.compute.manager.reset()
            # reset cached traits so they are recalculated.
            self.compute.driver._static_traits = None
            self._run_periodics()

            # Sanity check that we've still got the trait globally.
            global_traits = self._get_all_traits()
            self.assertIn(ost.HW_CPU_X86_AMD_SEV, global_traits)
            self.assertIn(ost.HW_CPU_X86_AMD_SEV_ES, global_traits)

            traits = self._get_provider_traits(self.host_uuid)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV, traits)
            self.assertNotIn(ost.HW_CPU_X86_AMD_SEV_ES, traits)

            sev_rps = self._get_amd_sev_rps()
            self.assertEqual(0, len(sev_rps['sev']))
            self.assertEqual(0, len(sev_rps['sev-es']))
