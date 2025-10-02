# Copyright 2012 OpenStack Foundation
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

import webob

from nova.api.openstack import common
from nova.api.openstack.compute.schemas import remote_consoles as schema
from nova.api.openstack import wsgi
from nova.api import validation
from nova.compute import api as compute
from nova import exception
from nova.policies import remote_consoles as rc_policies

_rdp_console_removal_reason = """\
RDP consoles are only available when using the Hyper-V driver, which was
removed from Nova in the 29.0.0 (Caracal) release.
"""


@validation.validated
class RemoteConsolesController(wsgi.Controller):
    def __init__(self):
        super(RemoteConsolesController, self).__init__()
        self.compute_api = compute.API()
        self.handlers = {'vnc': self.compute_api.get_vnc_console,
                         'spice': self.compute_api.get_spice_console,
                         'serial': self.compute_api.get_serial_console,
                         'mks': self.compute_api.get_mks_console}

    @wsgi.api_version("2.1", "2.5")
    @wsgi.expected_errors((400, 404, 409, 501))
    @wsgi.action('os-getVNCConsole')
    @validation.schema(schema.get_vnc_console)
    @validation.response_body_schema(schema.get_vnc_console_response)
    def get_vnc_console(self, req, id, body):
        """Get text console output."""
        context = req.environ['nova.context']
        context.can(rc_policies.BASE_POLICY_NAME)

        # If type is not supplied or unknown, get_vnc_console below will cope
        console_type = body['os-getVNCConsole'].get('type')

        instance = common.get_instance(self.compute_api, context, id)
        try:
            output = self.compute_api.get_vnc_console(context,
                                                      instance,
                                                      console_type)
        except exception.ConsoleTypeUnavailable as e:
            raise webob.exc.HTTPBadRequest(explanation=e.format_message())
        except exception.InstanceNotFound as e:
            raise webob.exc.HTTPNotFound(explanation=e.format_message())
        except exception.InstanceNotReady as e:
            raise webob.exc.HTTPConflict(explanation=e.format_message())
        except exception.InstanceInvalidState as e:
            common.raise_http_conflict_for_instance_invalid_state(
                e, 'get_vnc_console', id)
        except NotImplementedError:
            common.raise_feature_not_supported()

        return {'console': {'type': console_type, 'url': output['url']}}

    @wsgi.api_version("2.1", "2.5")
    @wsgi.expected_errors((400, 404, 409, 501))
    @wsgi.action('os-getSPICEConsole')
    @validation.schema(schema.get_spice_console)
    @validation.response_body_schema(schema.get_spice_console_response)
    def get_spice_console(self, req, id, body):
        """Get text console output."""
        context = req.environ['nova.context']
        context.can(rc_policies.BASE_POLICY_NAME)

        # If type is not supplied or unknown, get_spice_console below will cope
        console_type = body['os-getSPICEConsole'].get('type')

        instance = common.get_instance(self.compute_api, context, id)
        try:
            output = self.compute_api.get_spice_console(context,
                                                        instance,
                                                        console_type)
        except exception.ConsoleTypeUnavailable as e:
            raise webob.exc.HTTPBadRequest(explanation=e.format_message())
        except exception.InstanceNotFound as e:
            raise webob.exc.HTTPNotFound(explanation=e.format_message())
        except exception.InstanceNotReady as e:
            raise webob.exc.HTTPConflict(explanation=e.format_message())
        except NotImplementedError:
            common.raise_feature_not_supported()

        return {'console': {'type': console_type, 'url': output['url']}}

    @wsgi.api_version("2.1", "2.5")
    @wsgi.expected_errors((400, 404, 409, 501))
    @wsgi.action('os-getRDPConsole')
    @wsgi.removed('29.0.0', _rdp_console_removal_reason)
    @validation.schema(schema.get_rdp_console)
    @validation.response_body_schema(schema.get_rdp_console_response)
    def get_rdp_console(self, req, id, body):
        """RDP console was available only for HyperV driver which has been
        removed from Nova in 29.0.0 (Caracal) release.
        """
        raise webob.exc.HTTPBadRequest()

    @wsgi.api_version("2.1", "2.5")
    @wsgi.expected_errors((400, 404, 409, 501))
    @wsgi.action('os-getSerialConsole')
    @validation.schema(schema.get_serial_console)
    @validation.response_body_schema(schema.get_serial_console_response)
    def get_serial_console(self, req, id, body):
        """Get connection to a serial console."""
        context = req.environ['nova.context']
        context.can(rc_policies.BASE_POLICY_NAME)

        # If type is not supplied or unknown get_serial_console below will cope
        console_type = body['os-getSerialConsole'].get('type')
        instance = common.get_instance(self.compute_api, context, id)
        try:
            output = self.compute_api.get_serial_console(context,
                                                         instance,
                                                         console_type)
        except exception.InstanceNotFound as e:
            raise webob.exc.HTTPNotFound(explanation=e.format_message())
        except exception.InstanceNotReady as e:
            raise webob.exc.HTTPConflict(explanation=e.format_message())
        except (exception.ConsoleTypeUnavailable,
                exception.ImageSerialPortNumberInvalid,
                exception.ImageSerialPortNumberExceedFlavorValue,
                exception.SocketPortRangeExhaustedException) as e:
            raise webob.exc.HTTPBadRequest(explanation=e.format_message())
        except NotImplementedError:
            common.raise_feature_not_supported()

        return {'console': {'type': console_type, 'url': output['url']}}

    @wsgi.api_version("2.6")
    @wsgi.expected_errors((400, 404, 409, 501))
    @validation.schema(schema.create_v26, "2.6", "2.7")
    @validation.schema(schema.create_v28, "2.8", "2.98")
    @validation.schema(schema.create_v299, "2.99")
    @validation.response_body_schema(schema.create_response, "2.6", "2.7")
    @validation.response_body_schema(schema.create_response_v28, "2.8", "2.98")
    @validation.response_body_schema(schema.create_response_v299, "2.99")
    def create(self, req, server_id, body):
        context = req.environ['nova.context']
        instance = common.get_instance(self.compute_api, context, server_id)
        context.can(rc_policies.BASE_POLICY_NAME,
                    target={'project_id': instance.project_id})
        protocol = body['remote_console']['protocol']
        console_type = body['remote_console']['type']

        # handle removed console types
        if protocol in ('rdp',):
            raise webob.exc.HTTPBadRequest(
                'Unavailable console type %s.' % protocol
            )

        try:
            # this should never fail in the real world since our schema
            # prevents unsupported types getting through
            handler = self.handlers[protocol]
            output = handler(context, instance, console_type)
            return {'remote_console': {'protocol': protocol,
                                       'type': console_type,
                                       'url': output['url']}}
        except exception.InstanceNotFound as e:
            raise webob.exc.HTTPNotFound(explanation=e.format_message())
        except exception.InstanceNotReady as e:
            raise webob.exc.HTTPConflict(explanation=e.format_message())
        except (exception.ConsoleTypeInvalid,
                exception.ConsoleTypeUnavailable,
                exception.ImageSerialPortNumberInvalid,
                exception.ImageSerialPortNumberExceedFlavorValue,
                exception.SocketPortRangeExhaustedException) as e:
            raise webob.exc.HTTPBadRequest(explanation=e.format_message())
        except (NotImplementedError, KeyError):
            common.raise_feature_not_supported()
