# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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

from django.urls import path
from django.urls import re_path

from . import views

app_name = 'start'

""" Custom URL's in addition to the admin url's

"""

urlpatterns = [
    path('', views.Front.as_view(), name='Front'),
    re_path(r'^documentation/(?P<slug>[-\w]+)$', views.documentation, name='Documentation'),
    re_path(r'^doclist$', views.DocList.as_view(), name='DocList'),
    re_path(r'^concepts$', views.Concepts.as_view(), name='Concepts'),
]

# url(r'^generic$', views.Generic.as_view(), name='Generic'),
# url(r'^not_implemented$', views.Not_Implemented.as_view(), name='Not Implemented'),
# url(r'^about$', views.About.as_view(), name='About'),
# url(r'^get_started$', views.GetStarted.as_view(), name='Get Started'),
# url(r'^overview$', views.Overview.as_view(), name='Overview'),
# url(r'^latest$', views.Latest.as_view(), name='Latest Releases'),
# url(r'^help$', views.Help.as_view(), name='Help'),

# url(r'^user_profile$', views.user_profile, name='User Profile'),
