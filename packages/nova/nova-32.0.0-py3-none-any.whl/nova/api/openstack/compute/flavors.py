# Copyright 2010 OpenStack Foundation
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

from oslo_utils import strutils
import webob

from nova.api.openstack import api_version_request
from nova.api.openstack import common
from nova.api.openstack.compute.schemas import flavors as schema
from nova.api.openstack.compute.views import flavors as flavors_view
from nova.api.openstack import wsgi
from nova.api import validation
from nova.compute import flavors
from nova import exception
from nova.i18n import _
from nova import objects
from nova.policies import flavor_extra_specs as fes_policies
from nova.policies import flavor_manage as fm_policies
from nova import utils


@validation.validated
class FlavorsController(wsgi.Controller):
    """Flavor controller for the OpenStack API."""

    _view_builder_class = flavors_view.ViewBuilder

    # NOTE(oomichi): Return 202 for backwards compatibility but should be
    # 204 as this operation complete the deletion of aggregate resource and
    # return no response body.
    @wsgi.response(202)
    @wsgi.expected_errors(404)
    @validation.response_body_schema(schema.delete_response)
    def delete(self, req, id):
        context = req.environ['nova.context']
        context.can(fm_policies.POLICY_ROOT % 'delete', target={})

        flavor = objects.Flavor(context=context, flavorid=id)
        try:
            flavor.destroy()
        except exception.FlavorNotFound as e:
            raise webob.exc.HTTPNotFound(explanation=e.format_message())

    # NOTE(oomichi): Return 200 for backwards compatibility but should be 201
    # as this operation complete the creation of flavor resource.
    @wsgi.expected_errors((400, 409))
    @validation.schema(schema.create_v20, '2.0', '2.0')
    @validation.schema(schema.create, '2.1', '2.54')
    @validation.schema(schema.create_v255, '2.55')
    @validation.response_body_schema(schema.create_response, '2.0', '2.54')
    @validation.response_body_schema(schema.create_response_v255, '2.55', '2.60')  # noqa: E501
    @validation.response_body_schema(schema.create_response_v261, '2.61', '2.74')  # noqa: E501
    @validation.response_body_schema(schema.create_response_v275, '2.75')
    def create(self, req, body):
        context = req.environ['nova.context']
        context.can(fm_policies.POLICY_ROOT % 'create', target={})

        vals = body['flavor']

        name = vals['name']
        flavorid = vals.get('id')
        memory = vals['ram']
        vcpus = vals['vcpus']
        root_gb = vals['disk']
        ephemeral_gb = vals.get('OS-FLV-EXT-DATA:ephemeral', 0)
        swap = vals.get('swap', 0)
        rxtx_factor = vals.get('rxtx_factor', 1.0)
        is_public = vals.get('os-flavor-access:is_public', True)

        # The user can specify a description starting with microversion 2.55.
        include_description = api_version_request.is_supported(req, '2.55')
        description = vals.get('description') if include_description else None

        try:
            flavor = flavors.create(name, memory, vcpus, root_gb,
                                    ephemeral_gb=ephemeral_gb,
                                    flavorid=flavorid, swap=swap,
                                    rxtx_factor=rxtx_factor,
                                    is_public=is_public,
                                    description=description)
            # NOTE(gmann): For backward compatibility, non public flavor
            # access is not being added for created tenant. Ref -bug/1209101
        except (exception.FlavorExists,
                exception.FlavorIdExists) as err:
            raise webob.exc.HTTPConflict(explanation=err.format_message())

        include_extra_specs = False
        if api_version_request.is_supported(req, '2.61'):
            include_extra_specs = context.can(
                fes_policies.POLICY_ROOT % 'index', fatal=False)
            # NOTE(yikun): This empty extra_specs only for keeping consistent
            # with PUT and GET flavor APIs. extra_specs in flavor is added
            # after creating the flavor so to avoid the error in _view_builder
            # flavor.extra_specs is populated with the empty string.
            flavor.extra_specs = {}

        return self._view_builder.show(req, flavor, include_description,
                                       include_extra_specs=include_extra_specs)

    @wsgi.api_version('2.55')
    @wsgi.expected_errors((400, 404))
    @validation.schema(schema.update, '2.55')
    @validation.response_body_schema(schema.update_response, '2.55', '2.60')
    @validation.response_body_schema(schema.update_response_v261, '2.61', '2.74')  # noqa: E501
    @validation.response_body_schema(schema.update_response_v275, '2.75')
    def update(self, req, id, body):
        # Validate the policy.
        context = req.environ['nova.context']
        context.can(fm_policies.POLICY_ROOT % 'update', target={})

        # Get the flavor and update the description.
        try:
            flavor = objects.Flavor.get_by_flavor_id(context, id)
            flavor.description = body['flavor']['description']
            flavor.save()
        except exception.FlavorNotFound as e:
            raise webob.exc.HTTPNotFound(explanation=e.format_message())

        include_extra_specs = False
        if api_version_request.is_supported(req, '2.61'):
            include_extra_specs = context.can(
                fes_policies.POLICY_ROOT % 'index', fatal=False)
        return self._view_builder.show(req, flavor, include_description=True,
                                       include_extra_specs=include_extra_specs)

    @wsgi.expected_errors(400)
    @validation.query_schema(schema.index_query, '2.0', '2.74')
    @validation.query_schema(schema.index_query_275, '2.75')
    @validation.response_body_schema(schema.index_response, '2.0', '2.54')
    @validation.response_body_schema(schema.index_response_v255, '2.55')
    def index(self, req):
        """Return all flavors in brief."""
        limited_flavors = self._get_flavors(req)
        return self._view_builder.index(req, limited_flavors)

    @wsgi.expected_errors(400)
    @validation.query_schema(schema.index_query, '2.0', '2.74')
    @validation.query_schema(schema.index_query_275, '2.75')
    @validation.response_body_schema(schema.detail_response, '2.0', '2.54')
    @validation.response_body_schema(schema.detail_response_v255, '2.55', '2.60')  # noqa: E501
    @validation.response_body_schema(schema.detail_response_v261, '2.61')
    def detail(self, req):
        """Return all flavors in detail."""
        context = req.environ['nova.context']
        limited_flavors = self._get_flavors(req)

        include_extra_specs = False
        if api_version_request.is_supported(req, '2.61'):
            include_extra_specs = context.can(
                fes_policies.POLICY_ROOT % 'index', fatal=False)

        return self._view_builder.detail(
            req, limited_flavors, include_extra_specs=include_extra_specs)

    @wsgi.expected_errors(404)
    @validation.query_schema(schema.show_query)
    @validation.response_body_schema(schema.show_response, '2.0', '2.54')
    @validation.response_body_schema(schema.show_response_v255, '2.55', '2.60')
    @validation.response_body_schema(schema.show_response_v261, '2.61', '2.74')
    @validation.response_body_schema(schema.show_response_v275, '2.75')
    def show(self, req, id):
        """Return data about the given flavor id."""
        context = req.environ['nova.context']
        try:
            flavor = flavors.get_flavor_by_flavor_id(id, ctxt=context)
        except exception.FlavorNotFound as e:
            raise webob.exc.HTTPNotFound(explanation=e.format_message())

        include_extra_specs = False
        if api_version_request.is_supported(req, '2.61'):
            include_extra_specs = context.can(
                fes_policies.POLICY_ROOT % 'index', fatal=False)

        include_description = api_version_request.is_supported(req, '2.55')

        return self._view_builder.show(
            req, flavor, include_description=include_description,
            include_extra_specs=include_extra_specs)

    def _parse_is_public(self, is_public):
        """Parse is_public into something usable."""

        if is_public is None:
            # preserve default value of showing only public flavors
            return True
        elif utils.is_none_string(is_public):
            return None
        else:
            try:
                return strutils.bool_from_string(is_public, strict=True)
            except ValueError:
                msg = _('Invalid is_public filter [%s]') % is_public
                raise webob.exc.HTTPBadRequest(explanation=msg)

    def _get_flavors(self, req):
        """Helper function that returns a list of flavor dicts."""
        filters = {}
        sort_key = req.params.get('sort_key') or 'flavorid'
        sort_dir = req.params.get('sort_dir') or 'asc'
        limit, marker = common.get_limit_and_marker(req)

        context = req.environ['nova.context']
        if context.is_admin:
            # Only admin has query access to all flavor types
            filters['is_public'] = self._parse_is_public(
                    req.params.get('is_public', None))
        else:
            filters['is_public'] = True
            filters['disabled'] = False

        if 'minRam' in req.params:
            try:
                filters['min_memory_mb'] = int(req.params['minRam'])
            except ValueError:
                msg = _('Invalid minRam filter [%s]') % req.params['minRam']
                raise webob.exc.HTTPBadRequest(explanation=msg)

        if 'minDisk' in req.params:
            try:
                filters['min_root_gb'] = int(req.params['minDisk'])
            except ValueError:
                msg = (_('Invalid minDisk filter [%s]') %
                       req.params['minDisk'])
                raise webob.exc.HTTPBadRequest(explanation=msg)

        try:
            limited_flavors = objects.FlavorList.get_all(
                context, filters=filters, sort_key=sort_key, sort_dir=sort_dir,
                limit=limit, marker=marker)
        except exception.MarkerNotFound:
            msg = _('marker [%s] not found') % marker
            raise webob.exc.HTTPBadRequest(explanation=msg)

        return limited_flavors
