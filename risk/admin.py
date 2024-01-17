# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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

from django.contrib.gis import admin
from django.core import serializers
from django.db import models
from django.http import HttpResponse
from django_json_widget.widgets import JSONEditorWidget

from risk.ActivityBarrier import ActivityBarrier
from risk.Scenarios import Scenario
from risk.Scorecard import Scorecard
from risk.Workflows import Limitflow

actions = ['export2json', 'export2xml']


@admin.action(description='Export Selected Entries as JSON')
def export2json(self, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


@admin.action(description='Export Selected Entries as XML')
def export2xml(self, request, queryset):
    response = HttpResponse(content_type="application/xml")
    serializers.serialize("xml", queryset, stream=response)
    return response


class ScenarioAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(attrs={'initiaĺ': 'parsed'})},
    }
    list_display = ('name', 'scenario_no', 'factor_no', 'timepoint_no', 'scenario_type')
    save_as = True
    view_on_site = True


admin.site.register(Scenario, ScenarioAdmin)


@admin.register(Scorecard)
class ScorecardAdmin(admin.ModelAdmin):
    """Scorecard admin"""
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(ActivityBarrier)
class ActivityBarrierAdmin(admin.ModelAdmin):
    """Activity Barrier admin"""
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


class LimitflowAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # JSONField: {'widget': JSONEditor},
        models.JSONField: {'widget': JSONEditorWidget(attrs={'initial': 'parsed'})}
    }
    #
    # Searchable fields
    #
    search_fields = ['workflow_description']
    list_display = ('workflow_id', 'name', 'workflow_description', 'last_change_date',)
    list_filter = ('workflow_type', 'workflow_status')
    save_as = True
    view_on_site = False
    date_hierarchy = ('creation_date')


admin.site.register(Limitflow, LimitflowAdmin)
