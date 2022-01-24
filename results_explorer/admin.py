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
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_json_widget.widgets import JSONEditorWidget

from results_explorer.models import Calculation, ResultGroup, Visualization


#
# TODO display of calculation timestamp interferes with JSON editor
#
class CalculationAdmin(admin.ModelAdmin):
    fields = ('user', 'workflow', 'workflow_data', 'results_data', 'logfile', 'result_group')
    search_fields = ['results_data', 'workflow_data']
    list_filter = ('user',)
    list_display = ('workflow', 'result_group', 'creation_date', 'user')
    date_hierarchy = ('creation_date')

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(attrs={'initiaĺ': 'parsed'})},
    }
    save_as = False
    view_on_site = False


class ResultGroupAdmin(admin.ModelAdmin):
    fields = ('user', 'group_type',)
    list_filter = ('user', 'group_type')
    list_display = ('group_type', 'creation_date', 'user')
    date_hierarchy = ('creation_date')

    save_as = False
    view_on_site = False


class VisualizationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(attrs={'initiaĺ': 'parsed'})},
    }
    #
    # Searchable fields
    #
    search_fields = ['description']
    list_display = ('name', 'objective', 'description', 'last_change_date',)
    list_filter = ('objective',)
    save_as = True
    date_hierarchy = ('creation_date')

    # view_on_site = False

    def response_change(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        return HttpResponseRedirect(reverse("results_explorer:Visualization_list"))


admin.site.register(Calculation, CalculationAdmin)
admin.site.register(ResultGroup, ResultGroupAdmin)
admin.site.register(Visualization, VisualizationAdmin)

