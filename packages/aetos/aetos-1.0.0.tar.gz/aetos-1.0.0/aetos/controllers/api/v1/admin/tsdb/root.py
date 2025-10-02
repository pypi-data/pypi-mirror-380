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

from aetos.controllers.api.v1.admin.tsdb import clean_tombstones
from aetos.controllers.api.v1.admin.tsdb import delete_series
from aetos.controllers.api.v1.admin.tsdb import snapshot


class TsdbController:
    """v1/admin/tsdb API controller root."""

    clean_tombstones = clean_tombstones.CleanTombstonesController()
    delete_series = delete_series.DeleteSeriesController()
    snapshot = snapshot.SnapshotController()
