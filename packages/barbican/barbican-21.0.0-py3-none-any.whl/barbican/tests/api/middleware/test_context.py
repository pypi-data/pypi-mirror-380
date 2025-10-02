# Copyright (c) 2015 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from unittest import mock

from barbican.api.middleware import context
from barbican.tests import utils


class TestUnauthenticatedContextMiddleware(utils.BaseTestCase):

    def setUp(self):
        super(TestUnauthenticatedContextMiddleware, self).setUp()
        self.app = mock.MagicMock()
        self.middleware = context.UnauthenticatedContextMiddleware(self.app)

    def test_role_defaults_to_admin(self):
        request = mock.MagicMock()
        request.headers = {'X-Project-Id': 'trace'}
        request.environ = {}

        with mock.patch('barbican.context.RequestContext') as rc:
            self.middleware.process_request(request)
            rc.assert_called_with(
                project_id='trace',
                is_admin=True,
                user_id=None,
                roles=['admin'],
                request_id=request.request_id,
                project_domain_id=None,
                domain_id=None,
                user_domain_id=None
            )

    def test_role_used_from_header(self):
        request = mock.MagicMock()
        request.headers = {'X-Project-Id': 'trace', 'X-Roles': 'something'}
        request.environ = {}

        with mock.patch('barbican.context.RequestContext') as rc:
            self.middleware.process_request(request)
            rc.assert_called_with(
                project_id='trace',
                is_admin=False,
                user_id=None,
                roles=['something'],
                request_id=request.request_id,
                project_domain_id=None,
                domain_id=None,
                user_domain_id=None
            )
