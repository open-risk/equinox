# Copyright (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)
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

from django.contrib import admin
from django.db.models import JSONField
from prettyjson.widgets import PrettyJSONWidget

from policy.models import DashBoardParams
from policy.models import DataFlow
from policy.models import DataSeries
from policy.models import GeoSlice


class DataSeriesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget(attrs={'initiaĺ': 'parsed'})},
    }
    save_as = True


class DataFlowAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget(attrs={'initiaĺ': 'parsed'})},
    }
    search_fields = ['name', 'short_desc', 'long_desc']
    list_display = (
        'name', 'identifier', 'short_desc', 'oxford_n', 'dashboard_n', 'live_n')
    list_filter = ('tracked', 'menu_category')
    save_as = True
    view_on_site = False


class GeoSliceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget(attrs={'initiaĺ': 'parsed'})},
    }
    save_as = True


class DashboardParamsAdmin(admin.ModelAdmin):
    save_as = True


admin.site.register(DataSeries, DataSeriesAdmin)
admin.site.register(DataFlow, DataFlowAdmin)
admin.site.register(GeoSlice, GeoSliceAdmin)
admin.site.register(DashBoardParams, DashboardParamsAdmin)
