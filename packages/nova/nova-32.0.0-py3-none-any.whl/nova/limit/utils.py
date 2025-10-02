# Copyright 2022 StackHPC
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

import typing as ty

if ty.TYPE_CHECKING:
    from openstack import proxy

from oslo_limit import exception as limit_exceptions
from oslo_log import log as logging

import nova.conf
from nova import utils as nova_utils

LOG = logging.getLogger(__name__)
CONF = nova.conf.CONF

UNIFIED_LIMITS_DRIVER = "nova.quota.UnifiedLimitsDriver"
IDENTITY_CLIENT = None


def use_unified_limits():
    return CONF.quota.driver == UNIFIED_LIMITS_DRIVER


class IdentityClient:
    connection: 'proxy.Proxy'
    service_id: str
    region_id: str

    def __init__(self, connection, service_id, region_id):
        self.connection = connection
        self.service_id = service_id
        self.region_id = region_id

    def registered_limits(self):
        return list(self.connection.registered_limits(
            service_id=self.service_id, region_id=self.region_id))


def _identity_client():
    global IDENTITY_CLIENT
    if not IDENTITY_CLIENT:
        connection = nova_utils.get_sdk_adapter(
            'identity', True, conf_group='oslo_limit')
        service_id = None
        region_id = None
        # Prefer the endpoint_id if present, same as oslo.limit.
        if CONF.oslo_limit.endpoint_id is not None:
            endpoint = connection.get_endpoint(CONF.oslo_limit.endpoint_id)
            service_id = endpoint.service_id
            region_id = endpoint.region_id
        elif 'endpoint_service_type' in CONF.oslo_limit:
            # This must be oslo.limit >= 2.6.0 and this block is more or less
            # copied from there.
            if (not CONF.oslo_limit.endpoint_service_type and not
                    CONF.oslo_limit.endpoint_service_name):
                raise ValueError(
                    'Either endpoint_service_type or endpoint_service_name '
                    'must be set')
            # Get the service_id for registered limits calls.
            services = connection.services(
                type=CONF.oslo_limit.endpoint_service_type,
                name=CONF.oslo_limit.endpoint_service_name)
            if len(services) > 1:
                raise ValueError('Multiple services found')
            service_id = services[0].id
            # Get the region_id if region name is configured.
            # endpoint_region_name was added in oslo.limit 2.6.0.
            if CONF.oslo_limit.endpoint_region_name:
                regions = connection.regions(
                    name=CONF.oslo_limit.endpoint_region_name)
                if len(regions) > 1:
                    raise ValueError('Multiple regions found')
                region_id = regions[0].id
        IDENTITY_CLIENT = IdentityClient(connection, service_id, region_id)
    return IDENTITY_CLIENT


def should_enforce(exc: limit_exceptions.ProjectOverLimit) -> bool:
    """Whether the exceeded resource limit should be enforced.

    Given a ProjectOverLimit exception from oslo.limit, check whether the
    involved limit(s) should be enforced. This is needed if we need more logic
    than is available by default in oslo.limit.

    :param exc: An oslo.limit ProjectOverLimit exception instance, which
        contains a list of OverLimitInfo. Each OverLimitInfo includes a
        resource_name, limit, current_usage, and delta.
    """
    # If any exceeded limit is greater than zero, it means an explicitly set
    # limit has been enforced. And if any explicitly set limit has gone over
    # quota, the enforcement should be upheld and there is no need to consider
    # the potential for unset limits.
    if any(info.limit > 0 for info in exc.over_limit_info_list):
        return True

    # Next, if all of the exceeded limits are -1, we don't need to enforce and
    # we can avoid calling Keystone for the list of registered limits.
    #
    # A value of -1 is documented in Keystone as meaning unlimited:
    #
    # "Note
    #  The default limit of registered limit and the resource limit of project
    #  limit now are limited from -1 to 2147483647 (integer). -1 means no limit
    #  and 2147483647 is the max value for user to define limits."
    #
    # https://docs.openstack.org/keystone/latest/admin/unified-limits.html#what-is-a-limit
    #
    # but oslo.limit enforce does not treat -1 as unlimited at this time and
    # instead uses its literal integer value. We will consider any negative
    # limit value as unlimited.
    if all(info.limit < 0 for info in exc.over_limit_info_list):
        return False

    # Only resources with exceeded limits of "0" are candidates for
    # enforcement.
    #
    # A limit of "0" in the over_limit_info_list means that oslo.limit is
    # telling us the limit is 0. But oslo.limit returns 0 for two cases:
    # a) it found a limit of 0 in Keystone or b) it did not find a limit in
    # Keystone at all.
    #
    # We will need to query the list of registered limits from Keystone in
    # order to determine whether each "0" limit is case a) or case b).
    enforce_candidates = {
        info.resource_name for info in exc.over_limit_info_list
            if info.limit == 0}

    # Get a list of all the registered limits. There is not a way to filter by
    # resource names however this will do one API call whereas the alternative
    # is calling GET /registered_limits/{registered_limit_id} for each resource
    # name.
    registered_limits = _identity_client().registered_limits()

    # Make a set of resource names of the registered limits.
    have_limits_set = {limit.resource_name for limit in registered_limits}

    # If any candidates have limits set, enforce. It means at least one limit
    # has been explicitly set to 0.
    if enforce_candidates & have_limits_set:
        return True

    # The resource list will be either a require list or an ignore list.
    require_or_ignore = CONF.quota.unified_limits_resource_list

    strategy = CONF.quota.unified_limits_resource_strategy
    enforced = enforce_candidates
    if strategy == 'require':
        # Resources that are in both the candidate list and in the require list
        # should be enforced.
        enforced = enforce_candidates & set(require_or_ignore)
    elif strategy == 'ignore':
        # Resources that are in the candidate list but are not in the ignore
        # list should be enforced.
        enforced = enforce_candidates - set(require_or_ignore)
    else:
        LOG.error(
            f'Invalid strategy value: {strategy} is specified in the '
            '[quota]unified_limits_resource_strategy config option, so '
            f'enforcing for resources {enforced}')
    # Log in case we need to debug unexpected enforcement or non-enforcement.
    msg = (
        f'enforcing for resources {enforced}' if enforced else 'not enforcing')
    LOG.debug(
        f'Resources {enforce_candidates} have no registered limits set in '
        f'Keystone. [quota]unified_limits_resource_strategy is {strategy} and '
        f'[quota]unified_limits_resource_list is {require_or_ignore}, '
        f'so {msg}')
    return bool(enforced)
