# Copyright 2011 OpenStack Foundation
# Copyright 2013 IBM Corp.
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

from nova.api.openstack.compute import pause_server
from nova.tests.unit.api.openstack.compute import admin_only_action_common


class PauseServerTests(admin_only_action_common.CommonTests):

    def setUp(self):
        super().setUp()
        self.controller = pause_server.PauseServerController()
        self.compute_api = self.controller.compute_api

    def test_pause_unpause(self):
        self._test_actions(
            ['_pause', '_unpause'],
            body_map={'_pause': {'pause': None}, '_unpause': {'unpause': None}}
        )

    def test_actions_raise_on_not_implemented(self):
        self._test_not_implemented_state('_pause', {'pause': None})
        self._test_not_implemented_state('_unpause', {'unpause': None})

    def test_pause_unpause_with_non_existed_instance(self):
        self._test_actions_with_non_existed_instance(
            ['_pause', '_unpause'],
            body_map={'_pause': {'pause': None}, '_unpause': {'unpause': None}}
        )

    def test_pause_unpause_with_non_existed_instance_in_compute_api(self):
        self._test_actions_instance_not_found_in_compute_api(
            ['_pause', '_unpause'],
            body_map={'_pause': {'pause': None}, '_unpause': {'unpause': None}}
        )

    def test_pause_unpause_raise_conflict_on_invalid_state(self):
        self._test_actions_raise_conflict_on_invalid_state(
            ['_pause', '_unpause'],
            body_map={'_pause': {'pause': None}, '_unpause': {'unpause': None}}
        )

    def test_actions_with_locked_instance(self):
        self._test_actions_with_locked_instance(
            ['_pause', '_unpause'],
            body_map={'_pause': {'pause': None}, '_unpause': {'unpause': None}}
        )
