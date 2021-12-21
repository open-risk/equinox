import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import DetailView

from results_explorer.models import Calculation, Visualization

root_view = settings.ROOT_VIEW

from model_server.models import ReportingModeDescription, ReportingModeMatch, \
    ReportingModeName, ModelModes, ModelModesShort

from portfolio.ProjectActivity import ProjectActivity


@login_required(login_url='/login/')
def ghg_reduction(request):
    t = loader.get_template('ghg_reduction.html')
    context = RequestContext(request, {})

    table_header = []
    table_header.append('Project')
    table_header.append('Project Activity')
    table_header.append('Activity Emissions')
    table_header.append('Baseline Emissions')
    table_header.append('GHG Reduction')

    table_rows = {}
    key = 0
    for pa in ProjectActivity.objects.all():
        value = []
        value.append(pa.project.project_identifier)
        value.append(pa.project_activity_identifier)
        value.append(pa.project_activity_emissions)
        value.append(pa.baseline_activity_emissions)
        value.append(pa.baseline_activity_emissions - pa.project_activity_emissions)
        table_rows[key] = value
        key += 1
        print(key, value)

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def result_types(request):
    t = loader.get_template('result_types.html')
    context = RequestContext(request, {})

    # create a table with model result mode information
    # header row
    table_header = []
    table_header.append('Result Type ID')
    table_header.append('Name')
    for key, entry in ModelModesShort.items():
        table_header.append(entry)
    table_header.append('Description')

    table_rows = {}
    for key, entry in ReportingModeName.items():
        value = []
        value.append(key)
        value.append(ReportingModeName[key])
        matched_modes = ReportingModeMatch[key]
        for i in range(len(matched_modes)):
            if matched_modes[i] == 0:
                value.append('N')
            elif matched_modes[i] == 1:
                value.append('Y')
            else:
                print('ERROR in MODE')
        value.append(ReportingModeDescription[key])
        table_rows[key] = value

    context.update({'ModelModes': ModelModes})
    context.update({'TableRows': table_rows})
    context.update({'TableHeader': table_header})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def results_view(request, pk):
    try:
        R = Calculation.objects.get(pk=pk)
    except Calculation.DoesNotExist:
        raise Http404("Calculation does not exist")

    t = loader.get_template('result_view.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'Result': json.dumps(R.results_data)})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def visualization_view(request, pk):
    """
    Interactive modification / calculation of Visualizations using Ajax calls

    **Context**

    ``Visualization``
        An instance of :model:`results_explorer.Visualization`.

    **Template:**

    :template:`results_explorer/Visualization_interactive.html`
    """

    # get the Visualization object
    visualization = Visualization.objects.get(pk=pk)
    t = loader.get_template('visualization.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'object': visualization})
    return HttpResponse(t.template.render(context))
