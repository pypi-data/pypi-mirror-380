#
# Copyright 2025 Red Hat, Inc
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

import json

from oslo_log import log
import pecan
from wsme import exc

from aetos.controllers.api.v1 import base
from aetos import rbac

LOG = log.getLogger(__name__)


class DeleteSeriesController(base.Base):
    # NOTE(jwysogla): the delete_series/ endpoint expects a `match[]` argument,
    # which is making the use of wsexpose difficult, so a plain
    # pecan.expose is used instead, with handling of the arguments
    # as a dictionary inside the function.
    @pecan.expose(content_type='application/json')
    def post(self, *args, **kwargs):
        """Delete_series endpoint"""
        # TODO(jwysogla):
        # - handle unknown, missing and optional parameters
        # - handle unsuccessful calls to prometheus

        target = {"project_id": pecan.request.headers.get('X-Project-Id')}
        rbac.enforce('admin_delete_metrics', pecan.request.headers,
                     pecan.request.enforcer, target)

        if len(args) != 0:
            pecan.response.status = 404
            return json.dumps("page not found")

        self.create_prometheus_client(pecan.request.cfg)
        matches = kwargs.get('match[]', [])
        start = kwargs.get('start', None)
        end = kwargs.get('end', None)
        try:
            self.prometheus_post("admin/tsdb/delete_series",
                                 {"match[]": matches,
                                  "start": start,
                                  "end": end})
        except exc.ClientSideError as e:
            # NOTE(jwysogla): We need a special handling of the exceptions,
            # because we don't use wsexpose as with most of other endpoints.
            pecan.response.status = e.code
            return e.msg
        # On success don't return anything
