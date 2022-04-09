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
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from risk.ActivityBarrier import ActivityBarrier
from risk.Scorecard import Scorecard
from risk.Objectives import Playbook, Objective
from risk.Workflows import Workflow, Limitflow

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from risk.Scenarios import Scenario


class ScenarioAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(attrs={'initiaĺ': 'parsed'})},
    }
    list_display = ('name', 'scenario_no', 'description')
    save_as = True
    view_on_site = False
    date_hierarchy = ('creation_date')

    # def response_change(self, request, obj, post_url_continue=None):
    #     """This makes the response after adding go to another apps changelist for some model"""
    #     return HttpResponseRedirect(reverse("risk:scenario_list"))


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


class WorkflowAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(attrs={'initial': 'parsed'})}
    }
    #
    # Searchable fields
    #
    search_fields = ['workflow_description']
    list_display = ('workflow_id', 'name', 'objective', 'workflow_description', 'last_change_date',)
    list_filter = ('objective', 'workflow_type', 'workflow_status', 'single_asset_flag')
    save_as = True
    view_on_site = False
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


class PlaybookAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(attrs={'initial': 'parsed'})}
    }
    #
    # Searchable fields
    #
    search_fields = ['description']
    list_display = ('pk', 'name', 'type', 'last_change_date',)
    list_filter = ('type',)
    save_as = True
    view_on_site = False
    date_hierarchy = ('creation_date')


class ObjectiveAdmin(admin.ModelAdmin):
    #
    # Searchable fields
    #
    search_fields = ['description']
    list_display = ('pk', 'name', 'category', 'last_change_date',)
    list_filter = ('category',)
    save_as = True
    view_on_site = False
    date_hierarchy = ('creation_date')


admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(Limitflow, LimitflowAdmin)
admin.site.register(Playbook, PlaybookAdmin)
admin.site.register(Objective, ObjectiveAdmin)
