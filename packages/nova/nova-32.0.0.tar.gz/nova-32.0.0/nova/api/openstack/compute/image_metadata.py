# Copyright 2011 OpenStack Foundation
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


from webob import exc

from nova.api.openstack import common
from nova.api.openstack.compute.schemas import image_metadata as schema
from nova.api.openstack import wsgi
from nova.api import validation
from nova import exception
from nova.i18n import _
from nova.image import glance


@validation.validated
class ImageMetadataController(wsgi.Controller):
    """The image metadata API controller for the OpenStack API."""

    def __init__(self):
        super().__init__()
        self.image_api = glance.API()

    def _get_image(self, context, image_id):
        try:
            return self.image_api.get(context, image_id)
        except exception.ImageNotAuthorized as e:
            raise exc.HTTPForbidden(explanation=e.format_message())
        except exception.ImageNotFound:
            msg = _("Image not found.")
            raise exc.HTTPNotFound(explanation=msg)

    @wsgi.api_version('2.1', '2.38')
    @wsgi.expected_errors((403, 404))
    @validation.query_schema(schema.index_query)
    @validation.response_body_schema(schema.index_response)
    def index(self, req, image_id):
        """Returns the list of metadata for a given instance."""
        context = req.environ['nova.context']
        metadata = self._get_image(context, image_id)['properties']
        return {'metadata': metadata}

    @wsgi.api_version('2.1', '2.38')
    @wsgi.expected_errors((403, 404))
    @validation.query_schema(schema.show_query)
    @validation.response_body_schema(schema.show_response)
    def show(self, req, image_id, id):
        context = req.environ['nova.context']
        metadata = self._get_image(context, image_id)['properties']
        if id in metadata:
            return {'meta': {id: metadata[id]}}
        else:
            raise exc.HTTPNotFound()

    @wsgi.api_version('2.1', '2.38')
    @wsgi.expected_errors((400, 403, 404))
    @validation.schema(schema.create)
    @validation.response_body_schema(schema.create_response)
    def create(self, req, image_id, body):
        context = req.environ['nova.context']
        image = self._get_image(context, image_id)
        for key, value in body['metadata'].items():
            image['properties'][key] = value
        common.check_img_metadata_properties_quota(context,
                                                   image['properties'])
        try:
            image = self.image_api.update(context, image_id, image, data=None,
                                          purge_props=True)
        except exception.ImageNotAuthorized as e:
            raise exc.HTTPForbidden(explanation=e.format_message())
        return {'metadata': image['properties']}

    @wsgi.api_version('2.1', '2.38')
    @wsgi.expected_errors((400, 403, 404))
    @validation.schema(schema.update)
    @validation.response_body_schema(schema.update_response)
    def update(self, req, image_id, id, body):
        context = req.environ['nova.context']

        meta = body['meta']

        if id not in meta:
            expl = _('Request body and URI mismatch')
            raise exc.HTTPBadRequest(explanation=expl)

        image = self._get_image(context, image_id)
        image['properties'][id] = meta[id]
        common.check_img_metadata_properties_quota(context,
                                                   image['properties'])
        try:
            self.image_api.update(context, image_id, image, data=None,
                                  purge_props=True)
        except exception.ImageNotAuthorized as e:
            raise exc.HTTPForbidden(explanation=e.format_message())
        return {'meta': meta}

    @wsgi.api_version('2.1', '2.38')
    @wsgi.expected_errors((400, 403, 404))
    @validation.schema(schema.update_all)
    @validation.response_body_schema(schema.update_all_response)
    def update_all(self, req, image_id, body):
        context = req.environ['nova.context']
        image = self._get_image(context, image_id)
        metadata = body['metadata']
        common.check_img_metadata_properties_quota(context, metadata)
        image['properties'] = metadata
        try:
            self.image_api.update(context, image_id, image, data=None,
                                  purge_props=True)
        except exception.ImageNotAuthorized as e:
            raise exc.HTTPForbidden(explanation=e.format_message())
        return {'metadata': metadata}

    @wsgi.api_version('2.1', '2.38')
    @wsgi.expected_errors((403, 404))
    @wsgi.response(204)
    @validation.response_body_schema(schema.delete_response)
    def delete(self, req, image_id, id):
        context = req.environ['nova.context']
        image = self._get_image(context, image_id)
        if id not in image['properties']:
            msg = _("Invalid metadata key")
            raise exc.HTTPNotFound(explanation=msg)
        image['properties'].pop(id)
        try:
            self.image_api.update(context, image_id, image, data=None,
                                  purge_props=True)
        except exception.ImageNotAuthorized as e:
            raise exc.HTTPForbidden(explanation=e.format_message())
