# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase

"""
    re_path(r'^scenario_graphical_editor/(?P<pk>\d+)$', ScenarioEdit.as_view(), name='scenario_graphical_editor'),
    re_path(r'^scenario_form_editor/(?P<pk>\d+)$', scenario_editor, name='scenario_form_editor'),
"""


class SimpleTest(TestCase):

    def create_user(self):
        self.username = "admin"
        self.password = "admin"
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def test_not_logged(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_logged_admin(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/admin', follow=True)
        self.assertEqual(response.status_code, 200)

    # TODO
    # def test_risk_urls(self):
    #     self.create_user()
    #     client = Client()
    #     client.login(username=self.username, password=self.password)
    #     risk_pages = [
    #         "/risk/scenario_graphical_editor",
    #         "/risk/scenario_form_editor"
    #     ]
    #     for page in risk_pages:
    #         resp = client.get(page)
    #         self.assertEqual(resp.status_code, 200, msg=page)
