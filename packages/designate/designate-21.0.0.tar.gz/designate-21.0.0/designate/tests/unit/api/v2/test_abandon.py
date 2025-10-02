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


from unittest import mock

import oslotest.base

from designate.api.v2.controllers.zones.tasks import abandon
from designate.central import rpcapi
from designate import objects


class TestAbandonAPI(oslotest.base.BaseTestCase):
    def setUp(self):
        super().setUp()
        self.central_api = mock.Mock()
        self.zone = objects.Zone(
            id='1e8952a5-e5a4-426a-afab-4cd10131a351',
            name='example.com.',
            email='example@example.com'
        )
        mock.patch.object(rpcapi.CentralAPI, 'get_instance',
                          return_value=self.central_api).start()

        self.controller = abandon.AbandonController()

    @mock.patch('pecan.response')
    @mock.patch('pecan.request')
    def test_post_all_move_error(self, mock_request, mock_response):
        mock_request.environ = {'context': mock.Mock()}
        mock_delete_zone = mock.Mock()
        mock_delete_zone.deleted_at = None

        self.central_api.delete_zone.return_value = mock_delete_zone

        self.controller.post_all(self.zone.id)

        self.assertEqual(500, mock_response.status_int)
