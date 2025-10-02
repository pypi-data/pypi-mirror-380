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

import copy
import io
from unittest import mock

import os_traits
from oslo_config import cfg
from oslo_log import log as logging
from oslo_utils.fixture import uuidsentinel

from nova import context
from nova import objects
from nova.tests.fixtures import libvirt as fakelibvirt
from nova.tests.functional.libvirt import base
from nova.virt.libvirt import utils


CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class VGPUReshapeTests(base.ServersTestBase):

    def test_create_servers_with_vgpu(self):
        """Verify that vgpu reshape works with libvirt driver

        1) create two servers with an old tree where the VGPU resource is on
           the compute provider
        2) trigger a reshape
        3) check that the allocations of the servers are still valid
        4) create another server now against the new tree
        """
        self.mock_file_open.side_effect = [
            io.BytesIO(b''), io.BytesIO(b''), io.BytesIO(b'')]
        # NOTE(gibi): We cannot simply ask the virt driver to create an old
        # RP tree with vgpu on the root RP as that code path does not exist
        # any more. So we have to hack a "bit". We will create a compute
        # service without vgpu support to have the compute RP ready then we
        # manually add the VGPU resources to that RP in placement. Also we make
        # sure that during the instance claim the virt driver does not detect
        # the old tree as that would be a bad time for reshape. Later when the
        # compute service is restarted the driver will do the reshape.

        mdevs = {
            'mdev_4b20d080_1b54_4048_85b3_a6a62d165c01':
                fakelibvirt.FakeMdevDevice(
                    dev_name='mdev_4b20d080_1b54_4048_85b3_a6a62d165c01',
                    type_id=fakelibvirt.NVIDIA_11_VGPU_TYPE,
                    parent=fakelibvirt.MDEVCAP_DEV1_PCI_ADDR),
            'mdev_4b20d080_1b54_4048_85b3_a6a62d165c02':
                fakelibvirt.FakeMdevDevice(
                    dev_name='mdev_4b20d080_1b54_4048_85b3_a6a62d165c02',
                    type_id=fakelibvirt.NVIDIA_11_VGPU_TYPE,
                    parent=fakelibvirt.MDEVCAP_DEV2_PCI_ADDR),
            'mdev_4b20d080_1b54_4048_85b3_a6a62d165c03':
                fakelibvirt.FakeMdevDevice(
                    dev_name='mdev_4b20d080_1b54_4048_85b3_a6a62d165c03',
                    type_id=fakelibvirt.NVIDIA_11_VGPU_TYPE,
                    parent=fakelibvirt.MDEVCAP_DEV3_PCI_ADDR),
        }

        # start a compute with vgpu support disabled so the driver will
        # ignore the content of the above HostMdevDeviceInfo
        self.flags(enabled_mdev_types='', group='devices')

        self.hostname = self.start_compute(
            hostname='compute1',
            mdev_info=fakelibvirt.HostMdevDevicesInfo(devices=mdevs),
        )
        self.compute = self.computes[self.hostname]

        # create the VGPU resource in placement manually
        compute_rp_uuid = self.placement.get(
            '/resource_providers?name=compute1').body[
            'resource_providers'][0]['uuid']
        inventories = self.placement.get(
            '/resource_providers/%s/inventories' % compute_rp_uuid).body
        inventories['inventories']['VGPU'] = {
            'allocation_ratio': 1.0,
            'max_unit': 3,
            'min_unit': 1,
            'reserved': 0,
            'step_size': 1,
            'total': 3}
        self.placement.put(
            '/resource_providers/%s/inventories' % compute_rp_uuid,
            inventories)

        # enabled vgpu support
        self.flags(
            enabled_mdev_types=fakelibvirt.NVIDIA_11_VGPU_TYPE,
            group='devices')
        # We don't want to restart the compute service or it would call for
        # a reshape but we still want to accept some vGPU types so we call
        # directly the needed method
        self.compute.driver.supported_vgpu_types = (
            self.compute.driver._get_supported_vgpu_types())

        # now we boot two servers with vgpu
        extra_spec = {"resources:VGPU": 1}
        flavor_id = self._create_flavor(extra_spec=extra_spec)

        server_req = self._build_server(flavor_id=flavor_id)

        # NOTE(gibi): during instance_claim() there is a
        # driver.update_provider_tree() call that would detect the old tree and
        # would fail as this is not a good time to reshape. To avoid that we
        # temporarily mock update_provider_tree here.
        with mock.patch('nova.virt.libvirt.driver.LibvirtDriver.'
                        'update_provider_tree'):
            created_server1 = self.api.post_server({'server': server_req})
            server1 = self._wait_for_state_change(created_server1, 'ACTIVE')
            created_server2 = self.api.post_server({'server': server_req})
            server2 = self._wait_for_state_change(created_server2, 'ACTIVE')

        # Determine which device is associated with which instance
        # { inst.uuid: pgpu_name }
        inst_to_pgpu = {}
        ctx = context.get_admin_context()
        for server in (server1, server2):
            inst = objects.Instance.get_by_uuid(ctx, server['id'])
            mdevs = list(
                self.compute.driver._get_all_assigned_mediated_devices(inst))
            self.assertEqual(1, len(mdevs))
            mdev_uuid = mdevs[0]
            mdev_info = self.compute.driver._get_mediated_device_information(
                utils.mdev_uuid2name(mdev_uuid))
            inst_to_pgpu[inst.uuid] = mdev_info['parent']
        # The VGPUs should have come from different pGPUs
        self.assertNotEqual(*list(inst_to_pgpu.values()))

        # verify that the inventory, usages and allocation are correct before
        # the reshape
        compute_inventory = self.placement.get(
            '/resource_providers/%s/inventories' % compute_rp_uuid).body[
            'inventories']
        self.assertEqual(3, compute_inventory['VGPU']['total'])
        compute_usages = self.placement.get(
            '/resource_providers/%s/usages' % compute_rp_uuid).body[
            'usages']
        self.assertEqual(2, compute_usages['VGPU'])

        for server in (server1, server2):
            allocations = self.placement.get(
                '/allocations/%s' % server['id']).body['allocations']
            # the flavor has disk=10 and ephemeral=10
            self.assertEqual(
                {'DISK_GB': 20, 'MEMORY_MB': 2048, 'VCPU': 2, 'VGPU': 1},
                allocations[compute_rp_uuid]['resources'])

        # restart compute which will trigger a reshape
        self.compute = self.restart_compute_service(self.hostname)

        # verify that the inventory, usages and allocation are correct after
        # the reshape
        compute_inventory = self.placement.get(
            '/resource_providers/%s/inventories' % compute_rp_uuid).body[
            'inventories']
        self.assertNotIn('VGPU', compute_inventory)

        # NOTE(sbauza): The two instances will use two different pGPUs
        # That said, we need to check all the pGPU inventories for knowing
        # which ones are used.
        usages = {}
        pgpu_uuid_to_name = {}
        for pci_device in [fakelibvirt.MDEVCAP_DEV1_PCI_ADDR,
                           fakelibvirt.MDEVCAP_DEV2_PCI_ADDR,
                           fakelibvirt.MDEVCAP_DEV3_PCI_ADDR]:
            gpu_rp_uuid = self.placement.get(
                '/resource_providers?name=compute1_%s' % pci_device).body[
                'resource_providers'][0]['uuid']
            pgpu_uuid_to_name[gpu_rp_uuid] = pci_device
            gpu_inventory = self.placement.get(
                '/resource_providers/%s/inventories' % gpu_rp_uuid).body[
                'inventories']
            self.assertEqual(1, gpu_inventory['VGPU']['total'])

            gpu_usages = self.placement.get(
                '/resource_providers/%s/usages' % gpu_rp_uuid).body[
                'usages']
            usages[pci_device] = gpu_usages['VGPU']
        # Make sure that both instances are using different pGPUs
        used_devices = [dev for dev, usage in usages.items() if usage == 1]
        avail_devices = list(set(usages.keys()) - set(used_devices))
        self.assertEqual(2, len(used_devices))
        # Make sure that both instances are using the correct pGPUs
        for server in [server1, server2]:
            allocations = self.placement.get(
                '/allocations/%s' % server['id']).body[
                'allocations']
            self.assertEqual(
                {'DISK_GB': 20, 'MEMORY_MB': 2048, 'VCPU': 2},
                allocations[compute_rp_uuid]['resources'])
            rp_uuids = list(allocations.keys())
            # We only have two RPs, the compute RP (the root) and the child
            # pGPU RP
            gpu_rp_uuid = (rp_uuids[1] if rp_uuids[0] == compute_rp_uuid
                           else rp_uuids[0])
            self.assertEqual(
                {'VGPU': 1},
                allocations[gpu_rp_uuid]['resources'])
            # The pGPU's RP name contains the pGPU name
            self.assertIn(inst_to_pgpu[server['id']],
                          pgpu_uuid_to_name[gpu_rp_uuid])

        # now create one more instance with vgpu against the reshaped tree
        created_server = self.api.post_server({'server': server_req})
        server3 = self._wait_for_state_change(created_server, 'ACTIVE')

        # find the pGPU that wasn't used before we created the third instance
        # It should have taken the previously available pGPU
        device = avail_devices[0]
        gpu_rp_uuid = self.placement.get(
            '/resource_providers?name=compute1_%s' % device).body[
            'resource_providers'][0]['uuid']
        gpu_usages = self.placement.get(
            '/resource_providers/%s/usages' % gpu_rp_uuid).body[
            'usages']
        self.assertEqual(1, gpu_usages['VGPU'])

        allocations = self.placement.get(
            '/allocations/%s' % server3['id']).body[
            'allocations']
        self.assertEqual(
            {'DISK_GB': 20, 'MEMORY_MB': 2048, 'VCPU': 2},
            allocations[compute_rp_uuid]['resources'])
        self.assertEqual(
            {'VGPU': 1},
            allocations[gpu_rp_uuid]['resources'])


class SevResphapeTests(base.ServersTestBase):

    def setUp(self):
        super().setUp()
        admin_context = context.get_admin_context()
        hw_mem_enc_image = copy.deepcopy(self.glance.image1)
        hw_mem_enc_image['id'] = uuidsentinel.mem_enc_image_id
        hw_mem_enc_image['properties']['hw_machine_type'] = 'q35'
        hw_mem_enc_image['properties']['hw_firmware_type'] = 'uefi'
        hw_mem_enc_image['properties']['hw_mem_encryption'] = True
        self.glance.create(admin_context, hw_mem_enc_image)

    def _delete_server(self, server):
        with mock.patch('nova.virt.libvirt.driver.LibvirtDriver.'
                        'update_provider_tree'):
            super()._delete_server(server)

    @mock.patch('nova.virt.libvirt.driver.LibvirtDriver.'
                '_guest_configure_mem_encryption')
    def test_create_servers_with_amd_sev(self, mock_configure_me):
        """Verify that SEV reshape works with libvirt driver

        1) create one server with an old tree where the MEM_ENCRYPTION_CONTEXT
           resource is on the compute provider
        2) trigger a reshape
        3) check that the allocation of the server is still valid
        4) create another server now against the new tree
        """
        self.hostname = self.start_compute(
            hostname='compute1',
        )
        self.compute = self.computes[self.hostname]
        self.flags(num_memory_encrypted_guests=16, group='libvirt')

        # create the MEM_ENCRYPTION_CONTEXT resource in placement manually,
        # to simulate the old layout.
        compute_rp_uuid = self._get_provider_uuid_by_name('compute1')
        inventories = self.placement.get(
            '/resource_providers/%s/inventories' % compute_rp_uuid).body
        # MEM_ENCRYPTION_CONTEXT inventory was added to compute RP
        inventories['inventories']['MEM_ENCRYPTION_CONTEXT'] = {
            'allocation_ratio': 1.0,
            'max_unit': 1,
            'min_unit': 1,
            'reserved': 0,
            'step_size': 1,
            'total': 16}
        self.placement.put(
            '/resource_providers/%s/inventories' % compute_rp_uuid,
            inventories)
        # SEV trait was also added to compute RP
        traits = self._get_provider_traits(compute_rp_uuid)
        traits.append(os_traits.HW_CPU_X86_AMD_SEV)
        self._set_provider_traits(compute_rp_uuid, traits)

        # create a server before reshape
        with mock.patch('nova.virt.libvirt.driver.LibvirtDriver.'
                        'update_provider_tree'):
            pre_server = self._create_server(
                image_uuid=uuidsentinel.mem_enc_image_id)
        self.addCleanup(self._delete_server, pre_server)

        # verify that the inventory, usages and allocation are correct before
        # the reshape
        compute_inventories = self._get_provider_inventory(compute_rp_uuid)
        self.assertEqual(
            16, compute_inventories['MEM_ENCRYPTION_CONTEXT']['total'])
        compute_usages = self._get_provider_usages(compute_rp_uuid)
        self.assertEqual(1, compute_usages['MEM_ENCRYPTION_CONTEXT'])

        # restart the compute service to trigger reshape
        with mock.patch('nova.virt.libvirt.host.Host.supports_amd_sev',
                        return_value=True), \
                mock.patch('nova.virt.libvirt.host.Host.supports_amd_sev_es',
                           return_value=False):
            self.compute = self.restart_compute_service(self.hostname)

        # verify that the inventory, usages and allocation are correct after
        # the reshape
        compute_inventories = self._get_provider_inventory(compute_rp_uuid)
        self.assertNotIn('MEM_ENCRYPTION_CONTEXT', compute_inventories)
        compute_usages = self._get_provider_usages(compute_rp_uuid)
        self.assertNotIn('MEM_ENCRYPTION_CONTEXT', compute_usages)
        # MEM_ENCRYPTION_CONTEXT inventory/usage should be moreved to child RP
        sev_rp_uuid = self._get_provider_uuid_by_name('compute1_amd_sev')
        sev_inventories = self._get_provider_inventory(sev_rp_uuid)
        self.assertEqual(
            16, sev_inventories['MEM_ENCRYPTION_CONTEXT']['total'])
        sev_usages = self._get_provider_usages(sev_rp_uuid)
        self.assertEqual(1, sev_usages['MEM_ENCRYPTION_CONTEXT'])
        # SEV trait should be also moved to child RP
        sev_traits = self._get_provider_traits(sev_rp_uuid)
        self.assertIn(os_traits.HW_CPU_X86_AMD_SEV, sev_traits)

        # create a new server after reshape
        with mock.patch('nova.virt.libvirt.host.Host.supports_amd_sev',
                        return_value=True), \
                mock.patch('nova.virt.libvirt.host.Host.supports_amd_sev_es',
                           return_value=False):
            post_server = self._create_server(
                image_uuid=uuidsentinel.mem_enc_image_id)
        self.addCleanup(self._delete_server, post_server)

        sev_usages = self._get_provider_usages(sev_rp_uuid)
        self.assertEqual(2, sev_usages['MEM_ENCRYPTION_CONTEXT'])

    @mock.patch('nova.virt.libvirt.driver.LibvirtDriver.'
                '_guest_configure_mem_encryption')
    def test_create_servers_with_amd_sev_mixed(self, mock_configure_me):
        """Verify that SEV reshape supports upgrade sceario

        1) prepare two compute nodes with old tree
        2) trigger a reshape in one compute node
        3) create one server against the new tree and another against the old
           tree
        """
        self.hostname1 = self.start_compute(
            hostname='compute1',
        )
        self.hostname2 = self.start_compute(
            hostname='compute2',
        )
        self.compute1 = self.computes[self.hostname1]
        self.compute2 = self.computes[self.hostname2]
        self.flags(num_memory_encrypted_guests=16, group='libvirt')

        # create the MEM_ENCRYPTION_CONTEXT resource in placement manually,
        # to simulate the old layout.
        for name in ('compute1', 'compute2'):
            compute_rp_uuid = self._get_provider_uuid_by_name(name)
            inventories = self.placement.get(
                '/resource_providers/%s/inventories' % compute_rp_uuid).body
            # MEM_ENCRYPTION_CONTEXT inventory was added to compute RP
            inventories['inventories']['MEM_ENCRYPTION_CONTEXT'] = {
                'allocation_ratio': 1.0,
                'max_unit': 1,
                'min_unit': 1,
                'reserved': 0,
                'step_size': 1,
                'total': 16}
            self.placement.put(
                '/resource_providers/%s/inventories' % compute_rp_uuid,
                inventories)
            # SEV trait was also added to compute root RP
            traits = self._get_provider_traits(compute_rp_uuid)
            traits.append(os_traits.HW_CPU_X86_AMD_SEV)
            self._set_provider_traits(compute_rp_uuid, traits)

        # verify that the inventory, usages and allocation are correct before
        # the reshape
        for name in ('compute1', 'compute2'):
            compute_rp_uuid = self._get_provider_uuid_by_name(name)
            compute_inventories = self._get_provider_inventory(compute_rp_uuid)
            self.assertEqual(
                16, compute_inventories['MEM_ENCRYPTION_CONTEXT']['total'])
            compute_usages = self._get_provider_usages(compute_rp_uuid)
            self.assertEqual(0, compute_usages['MEM_ENCRYPTION_CONTEXT'])

        # restart the compute service in compute1 to trigger reshape
        with mock.patch('nova.virt.libvirt.host.Host.supports_amd_sev',
                        return_value=True), \
                mock.patch('nova.virt.libvirt.host.Host.supports_amd_sev_es',
                           return_value=False):
            self.compute1 = self.restart_compute_service(self.hostname1)

        # compute1 should have its RP reshaped
        compute_rp_uuid = self._get_provider_uuid_by_name('compute1')
        compute_inventories = self._get_provider_inventory(compute_rp_uuid)
        self.assertNotIn('MEM_ENCRYPTION_CONTEXT', compute_inventories)

        sev_rp_uuid = self._get_provider_uuid_by_name('compute1_amd_sev')
        sev_inventories = self._get_provider_inventory(sev_rp_uuid)
        self.assertEqual(
            16, sev_inventories['MEM_ENCRYPTION_CONTEXT']['total'])
        sev_usages = self._get_provider_usages(sev_rp_uuid)
        self.assertEqual(0, sev_usages['MEM_ENCRYPTION_CONTEXT'])

        # compute2 should have old RP
        compute_rp_uuid = self._get_provider_uuid_by_name('compute2')
        compute_inventories = self._get_provider_inventory(compute_rp_uuid)
        self.assertEqual(
            16, compute_inventories['MEM_ENCRYPTION_CONTEXT']['total'])
        compute_usages = self._get_provider_usages(compute_rp_uuid)
        self.assertEqual(0, compute_usages['MEM_ENCRYPTION_CONTEXT'])

        # create new servers to both compute nodes
        with mock.patch('nova.virt.libvirt.host.Host.supports_amd_sev',
                        return_value=True), \
                mock.patch('nova.virt.libvirt.host.Host.supports_amd_sev_es',
                           return_value=False):
            post_server1 = self._create_server(
                host='compute1', networks='none',
                image_uuid=uuidsentinel.mem_enc_image_id)
        self.addCleanup(self._delete_server, post_server1)
        # NOTE(tkajinam): compute2 has old SEV RP so we should avoid
        # update_provider_tree here
        with mock.patch('nova.virt.libvirt.driver.LibvirtDriver.'
                        'update_provider_tree'):
            post_server2 = self._create_server(
                host='compute2', networks='none',
                image_uuid=uuidsentinel.mem_enc_image_id)
        self.addCleanup(self._delete_server, post_server2)

        # server1 should allocate M_E_C from SEV RP
        sev_rp_uuid = self._get_provider_uuid_by_name('compute1_amd_sev')
        sev_usages = self._get_provider_usages(sev_rp_uuid)
        self.assertEqual(1, sev_usages['MEM_ENCRYPTION_CONTEXT'])

        # server2 should allocate M_E_C from compute root RP
        compute_rp_uuid = self._get_provider_uuid_by_name('compute2')
        compute_usages = self._get_provider_usages(compute_rp_uuid)
        self.assertEqual(1, compute_usages['MEM_ENCRYPTION_CONTEXT'])
