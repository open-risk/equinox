import json

import numpy as np
import pandas as pd
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import modelform_factory
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from results_explorer.models import Calculation, ResultGroup, Visualization
from results_explorer.forms import VisualizationInteractiveForm

root_view = settings.ROOT_VIEW

from model_server.models import ReportingModeDescription, ReportingModeMatch, \
    ReportingModeName, ModelModes, ModelModesShort


class ResultsList(LoginRequiredMixin, ListView):
    model = Calculation
    template_name = 'results_explorer/calculation_list.html'

    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'root_view': root_view})
        return context


class ResultGroupList(LoginRequiredMixin, ListView):
    model = ResultGroup
    template_name = 'results_explorer/result_group_list.html'

    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'root_view': root_view})
        return context


@login_required(login_url='/login/')
def result_types(request):
    t = loader.get_template('results_explorer/result_types.html')
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
def loss_distribution_1p_view(request):
    t = loader.get_template('results_explorer/loss_distribution_1p.html')
    context = RequestContext(request, {})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def loss_distribution_mp_view(request):
    t = loader.get_template('results_explorer/loss_distribution_mp.html')
    context = RequestContext(request, {})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def results_directory_view(request):
    t = loader.get_template('results_explorer/index.html')
    context = RequestContext(request, {})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def results_view(request, pk):
    try:
        R = Calculation.objects.get(pk=pk)
    except Calculation.DoesNotExist:
        raise Http404("Calculation does not exist")

    t = loader.get_template('results_explorer/result_view.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'Result': json.dumps(R.results_data)})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def result_group_view(request, pk):
    """
    Raw Display of All content in a result group
    :param request:
    :param pk:
    :return:
    """
    try:
        # Select our result group
        RG = ResultGroup.objects.get(pk=pk)
        # Get all results with foreign key to this group
        R = RG.calculation_set.all()
    except ResultGroup.DoesNotExist:
        raise Http404("Result Group does not exist")

    print(type(RG))
    print(type(R))
    result_collection = []
    # Collect and collate all results_data from each Result
    for entry in R:
        print(type(entry))
        print(entry)
        result_collection.append(entry.results_data)

    t = loader.get_template('results_explorer/result_group_view.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'Result': json.dumps(result_collection)})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def result_group_logfiles(request, pk):
    """
    Raw Display of All logfiles of a result group
    :param request:
    :param pk:
    :return:
    """
    try:
        # Select our result group
        RG = ResultGroup.objects.get(pk=pk)
        # Get all results with foreign key to this group
        R = RG.calculation_set.all()
    except ResultGroup.DoesNotExist:
        raise Http404("Result Group does not exist")

    print(type(RG))
    print(type(R))
    logfile_collection = []
    # Collect and collate all results_data from each Result
    for entry in R:
        print(type(entry))
        print(entry)
        logfile_collection.append(entry.logfile)

    t = loader.get_template('results_explorer/result_group_logfiles.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'logfile_collection': logfile_collection})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def single_period_metrics(request, pk):
    """
    Display table with single period metrics
    :param request:
    :param pk:
    :return:
    """
    try:
        # Select our result group
        RG = ResultGroup.objects.get(pk=pk)
        print(type(RG))
        # Get all results with foreign key to this group
        R = RG.calculation_set.all()
        print(type(R))
        # Get the playbook that produced the result group
        PB = RG.playbook
        print(type(PB))
    except ResultGroup.DoesNotExist:
        raise Http404("Result Group does not exist")

    # Convert portfolio parametric survey to pandasframe
    # ATTN Only single timepoint results

    run_number = len(PB.parameter_range)
    values = PB.parameter_range
    print("RUN NUMBER ", run_number)
    print("VALUES ", values)

    all_run_results = []
    for entry in R:
        print(type(entry))
        all_run_results.append(entry.results_data)

    print("ALL RUN RESULTS: ", all_run_results)

    # TODO Hardwired metric names and result_id
    # Get the result_id as parameter to the view
    # Get the metric keys from the results_data (use the first result object)

    simulated_metrics = ['ECL Mean', 'ECL1YR Mean', 'Provision Mean', 'Loss Mean', 'PnL_1 Mean', 'PnL_2 Mean',
                         'ECL Std', 'ECL1YR Std', 'Provision Std', 'Loss Std', 'PnL_1 Std', 'PnL_2 Std']

    result_id = 14
    metric_number = len(simulated_metrics)

    simulated_values = np.zeros((metric_number, run_number))

    # insert frame header (run number, parameter value, benchmark metrics, simulated metrics, difference, % difference)
    header_list = ['Run Number', 'Value']
    data_frame = pd.DataFrame(columns=header_list)

    # FOR ALL PARAMETRIC RUNS
    for r in range(1, run_number + 1):
        print("> Simulation Run Number: ", r)
        # Select the r-th result object and fetch the data
        # all_run_results = R[r]['result_data']
        # FIND CORRECT RESULT ID IN RUN RESULTS
        for run_results in all_run_results:
            # print("RUN RESULTS: ", run_results)
            for result in run_results:
                print("RESULT ID: ", result['ID'])
                print("RESULT: ", result)
                print("DATA: ", result['Data'])
                if result['ID'] == result_id:
                    for m in range(0, metric_number):
                        print(">> Metric: ", simulated_metrics[m])
                        simulated = result['Data'][simulated_metrics[m]]
                        simulated_values[m, r - 1] = simulated

    # Augment header list
    for m in range(len(simulated_metrics)):
        header_list += [simulated_metrics[m]]

    # Augment result rows
    for r in range(1, run_number + 1):
        row = {'Run Number': r, 'Value': values[r - 1]}
        for m in range(len(simulated_metrics)):
            row.update({simulated_metrics[m]: simulated_values[m, r - 1]})
        print(row)
        data_frame = data_frame.append(row, ignore_index=True)

    table_view = data_frame.to_html(index=False)

    t = loader.get_template('results_explorer/single_period_metrics.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'table_view': table_view})
    return HttpResponse(t.template.render(context))


class VisualizationList(LoginRequiredMixin, ListView):
    model = Visualization
    login_url = '/login/'
    template_name = 'results_explorer/visualization_list.html'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'root_view': root_view})
        return context


class VisualizationObjectiveList(LoginRequiredMixin, ListView):
    model = Visualization
    template_name = 'results_explorer/visualization_objective_list.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        objectives = []
        for choice in Visualization.OBJECTIVE_CHOICE:
            objectives.append(choice[1])

        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'objectives': objectives})
        return context


class VisualizationClone(LoginRequiredMixin, UpdateView):
    model = Visualization
    form_class = modelform_factory(Visualization, fields=(
        'name', 'user_id'), exclude=None)
    success_url = reverse_lazy('DataEndPoint_list')
    template_name_suffix = '_clone'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class VisualizationCreate(LoginRequiredMixin, CreateView):
    model = Visualization
    template_name = 'results_explorer/visualization_create.html'
    form_class = modelform_factory(Visualization, fields=('name', 'user_id'), exclude=None)
    success_url = reverse_lazy('Visualization_list')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class VisualizationDelete(LoginRequiredMixin, DeleteView):
    model = Visualization
    success_url = reverse_lazy('Visualization_list')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class VisualizationInteractive(LoginRequiredMixin, DetailView):
    model = Visualization
    template_name = 'results_explorer/visualization_interactive.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        visualization = super(VisualizationInteractive, self).get_object()
        context = super(DetailView, self).get_context_data(**kwargs)
        return context


@login_required(login_url='/login/')
def Visualization_interactive(request, pk):
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
    model_url = Visualization.model_url
    # serialize the Visualization
    Visualization_data = []
    response_data = ''
    log_data = ''
    results_data = ''
    # display the Visualization in a form
    formset = VisualizationInteractiveForm(instance=visualization)
    t = loader.get_template('results_explorer/visualization_interactive.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'object': Visualization, 'formset': formset})
    context.update({'Visualization_data': Visualization_data})
    context.update({'results_data': results_data})
    context.update({'log_data': log_data})
    context.update({'model_url': model_url})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def Visualization_view(request, pk):
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
    # model_url = Visualization.model_url
    # # serialize the Visualization
    # Visualization_data = []
    # response_data = ''
    # log_data = ''
    # results_data = ''
    # # display the Visualization in a form
    # formset = VisualizationInteractiveForm(instance=visualization)
    t = loader.get_template('results_explorer/visualization.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'object': visualization})
    # context.update({'Visualization_data': Visualization_data})
    # context.update({'results_data': results_data})
    # context.update({'log_data': log_data})
    # context.update({'model_url': model_url})
    return HttpResponse(t.template.render(context))
