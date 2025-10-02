# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
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

from oslo_config import fixture as config_fixture
from oslo_policy import opts as policy_opts

from nova.conf import devices
from nova.conf import neutron
from nova.conf import paths
from nova import config


class ConfFixture(config_fixture.Config):
    """Fixture to manage global conf settings."""

    def setUp(self):
        super(ConfFixture, self).setUp()

        # default group
        self.conf.set_default('compute_driver', 'fake.SmallFakeDriver')
        self.conf.set_default('host', 'fake-mini')
        self.conf.set_default('periodic_enable', False)

        # api_database group
        self.conf.set_default('connection', "sqlite://", group='api_database')
        self.conf.set_default('sqlite_synchronous', False,
                              group='api_database')

        # database group
        self.conf.set_default('connection', "sqlite://", group='database')
        self.conf.set_default('sqlite_synchronous', False, group='database')

        # key_manager group
        self.conf.set_default('backend',
                              'nova.keymgr.conf_key_mgr.ConfKeyManager',
                              group='key_manager')

        # wsgi group
        self.conf.set_default('api_paste_config',
                              paths.state_path_def('etc/nova/api-paste.ini'),
                              group='wsgi')

        # api group
        self.conf.set_default('response_validation', 'error', group='api')

        # many tests synchronizes on the reception of versioned notifications
        self.conf.set_default(
            'notification_format', "both", group="notifications")

        # oslo.limit requires endpoint_id since 2.3.0
        self.conf.set_default('endpoint_id', 'ENDPOINT_ID', group='oslo_limit')

        config.parse_args([], default_config_files=[], configure_db=False,
                          init_rpc=False)
        policy_opts.set_defaults(self.conf)
        neutron.register_dynamic_opts(self.conf)
        devices.register_dynamic_opts(self.conf)
