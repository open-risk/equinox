# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
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


"""Equinox URL Configuration. The `urlpatterns` list routes URLs to views.

"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views, settings

schema_view = get_schema_view(
    openapi.Info(
        title="equinox API",
        default_version='v1',
        description="equinox is an open source platform for the holistic management of sustainable finance projects.",
        terms_of_service="https://www.openriskmanagement.com/",
        contact=openapi.Contact(email="info@openriskmanagement.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('', include('start.urls')),  # Equinox Start Page URLS
                  path('reporting/', include('reporting.urls')),  # Results Explorer URLS
                  path('policy/', include('policy.urls')),  # Results Explorer URLS
                  path('reference/', include('reference.urls')),  # Results Explorer URLS
                  path('risk/', include('risk.urls')),  # Risk Analysis URLS
                  path('admin/doc/', include('django.contrib.admindocs.urls')),  #
                  path('admin/', admin.site.urls),  # Equinox Admin URL's
                  path(r'api/', views.api_root, name='api_root'),  # API root
                  path(r'api/portfolio_data/', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),
                  # Portfolio Data API
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This is the optional debug toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
