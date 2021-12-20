import json
from itertools import chain

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms import Textarea
from django.forms.models import modelform_factory
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from equinox.serializers import WorkflowDetailSerializer
from rest_framework_jwt.settings import api_settings
from risk_analysis.forms import PlaybookBatchForm
from risk_analysis.forms import WorkflowDebugForm, WorkflowInteractiveForm, WorkflowBatchForm
from risk_analysis.forms import creditNetInteractiveForm
from risk_analysis.Objectives import OBJECTIVE_CHOICE, Playbook
from risk_analysis.Workflows import Workflow, Limitflow
from risk_analysis.playbook_run_loop import run_loop

root_view = settings.ROOT_VIEW
cgi_url = settings.CGI_URL
cgi_path = settings.CGI_PATH


class About(LoginRequiredMixin, TemplateView):
    template_name = 'workflow_explorer/about.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context.update({'root_view': root_view})
        return context


class WorkflowList(LoginRequiredMixin, ListView):
    model = Workflow
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class PlaybookList(LoginRequiredMixin, ListView):
    model = Playbook
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class PublishedWorkflowList(LoginRequiredMixin, ListView):
    """
    We are only showing published (or published but broken workflows)

    """
    model = Workflow
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'workflow_explorer/workflow_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Workflow.objects.filter(Q(workflow_status=1) & Q(workflow_type=2))
        return queryset


class BatchWorkflowList(LoginRequiredMixin, ListView):
    """
    We are only showing batch workflows

    """
    model = Workflow
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'workflow_explorer/workflow_batch_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Workflow.objects.filter(Q(workflow_type=1))
        return queryset


# List the interactive workflows
class WorkflowObjectiveList(LoginRequiredMixin, ListView):
    """
    We are only showing published (or published but broken workflows)
    Sorted by Objective into Tabbed lists

    """
    model = Workflow
    template_name = 'workflow_explorer/workflow_objective_list.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self, *args, **kwargs):
        queryset1 = Workflow.objects.filter(Q(workflow_status=1) | Q(workflow_status=2))
        queryset2 = Limitflow.objects.all()
        print(len(queryset1))
        print(len(queryset2))
        print(type(queryset1))
        queryset = list(chain(queryset1, queryset2))
        print(len(queryset))
        print(type(queryset))
        return queryset

    def get_context_data(self, **kwargs):
        objectives = []
        for choice in OBJECTIVE_CHOICE:
            objectives.append(choice[1])

        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'objectives': objectives})
        return context


class WorkflowClone(LoginRequiredMixin, UpdateView):
    model = Workflow
    form_class = modelform_factory(Workflow, fields=('name', 'workflow_model',
                                                     'model_configuration', 'user_id'), exclude=None)
    success_url = reverse_lazy('DataEndPoint_list')
    template_name_suffix = '_clone'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class WorkflowView(LoginRequiredMixin, UpdateView):
    model = Workflow
    form_class = modelform_factory(Workflow, fields=('name', 'workflow_type', 'workflow_model',
                                                     'model_configuration', 'user_id'),
                                   exclude=None)
    success_url = reverse_lazy('workflow_list')
    template_name_suffix = '_view'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class WorkflowCreate(LoginRequiredMixin, CreateView):
    model = Workflow
    template_name = 'workflow_explorer/workflow_create.html'
    form_class = modelform_factory(Workflow, fields=('name', 'workflow_model', 'model_configuration'), exclude=None,
                                   widgets={"model_configuration": Textarea(attrs={'cols': 40, 'rows': 10})})
    success_url = reverse_lazy('workflow_list')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class WorkflowDelete(LoginRequiredMixin, DeleteView):
    model = Workflow
    success_url = reverse_lazy('workflow_list')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class WorkflowCalculate(LoginRequiredMixin, DetailView):
    model = Workflow
    template_name_suffix = '_calculate'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context.update({'root_view': root_view})
        return context


class WorkflowDebug(LoginRequiredMixin, DetailView):
    model = Workflow
    template_name = 'workflow_explorer/workflow_debug.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        workflow = super(WorkflowDebug, self).get_object()

        serializer = WorkflowDetailSerializer(workflow, context={'request': self.request})
        workflow_data = json.dumps(serializer.data)
        print("WORKFLOW DATA", workflow_data)
        model_url = workflow.workflow_model.model_server_url
        # construct header
        headers = {'Content-Type': 'application/json'}
        response = requests.post(model_url, data=workflow_data, headers=headers, verify=False)
        print("RESPONSE TEXT", response.text)

        file = open("/var/www/cgi-bin/workflow.log", 'r')
        results_data = response.text
        log_data = file.read()

        context = super(DetailView, self).get_context_data(**kwargs)
        context.update({'results_data': results_data})
        context.update({'log_data': log_data})
        return context


class WorkflowInteractive(LoginRequiredMixin, DetailView):
    model = Workflow
    template_name = 'workflow_explorer/workflow_interactive.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        workflow = super(WorkflowInteractive, self).get_object()

        # Python based client to execute Open Risk API model calculation
        # Construct and post the calculation workflow_data from workflow information (and context)
        # workflow_data = {}
        # # 0 "Authentication step"
        # # workflow_data["user_id"] = "User001"
        # # 1 Select which portfolio to use (based on URI + filtering)
        # workflow_data["input_set"] = json.loads(workflow.input_set)
        # # 2 Select where to store output (here: we take the server suggestion)
        # workflow_data["output_set"] = json.loads(workflow.output_set)
        # # 3 Send model configuration
        # workflow_data["model_configuration"] = json.loads(workflow.model_configuration)
        # # 4 Send model data
        # workflow_data["model_data"] = json.loads(workflow.model_data)
        #
        # model_url = workflow.model_url
        # print("WORKFLOW-DATA", workflow_data)
        # # construct header
        # headers = {'Content-Type': 'application/json'}
        # response = requests.post(model_url, data=json.dumps(workflow_data), headers=headers)
        # print("RESPONSE TEXT", response.text)
        # results = response.json()
        # results_json = json.dumps(results)
        # workflow_json = json.dumps(workflow_data)
        #
        context = super(DetailView, self).get_context_data(**kwargs)
        # context.update({'workflow_data': workflow_json})
        # context.update({'results_data': results_json})
        # context.update({'model_url': model_url})
        return context


@login_required(login_url='/login/')
def workflow_interactive(request, pk):
    """
    Interactive modification / calculation of workflows using Ajax calls

    **Context**

    ``Workflow``
        An instance of :model:`workflow_explorer.Workflow`.

    **Template:**

    :template:`workflow_explorer/workflow_interactive.html`
    """

    # POST request holds complete and valid workflow_data.json
    # hide any calculation specifics into the model server (server.py file)

    print("REQUEST META ", request.META)
    # if post is done internally via Django Authenticated User
    try:
        print("------  USER BASED AUTHENTICATION   ------")
        auth = request.META['HTTP_AUTHORIZATION']
    except:
        # if post is done externally via JWT Authentication
        print("------  EXTERNAL JWT AUTHENTICATION   ------")
        print(request.user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        user = User.objects.get(username=request.user.username)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        auth = 'JWT {}'.format(token)
        # data = {'username': request.user.username, 'password': request.user.password}
        # response = requests.post(API_TOKEN_URL, data=data)
        print('AUTHENTICATION', auth)
        # auth = response.json()['token']

    # get the desired workflow object
    workflow = Workflow.objects.get(pk=pk)
    # figure out which model (server) we will be calling
    model_url = workflow.workflow_model.model_server_url
    # serialize the workflow
    serializer = WorkflowDetailSerializer(workflow, context={'request': request})
    workflow_data = serializer.data
    print('SERIALIZING WORKFLOW DATA: ', workflow_data)

    # prepare the ticket
    headers = {'Content-Type': 'application/json', 'Authorization': auth}
    formset = None

    results_data = [{'Message': 'None', 'Type': 'None', 'ID': 0, 'Data': {}}]

    if request.method == 'GET':
        print("GET REQUEST IN VIEW")
        # display the workflow in a form
        if workflow.workflow_model.model_server.model_server_name == 'creditNet':
            formset = creditNetInteractiveForm(instance=workflow)
            # formset = WorkflowInteractiveForm(instance=workflow)
            print('SELECTING CREDITNET FORMSET')
        else:
            formset = WorkflowInteractiveForm(instance=workflow)

    elif request.method == 'POST':
        if workflow.workflow_model.model_server.model_server_name == 'creditNet':
            formset = creditNetInteractiveForm(request.POST)
        else:
            formset = WorkflowInteractiveForm(request.POST)

        # creditNet interactive form
        if workflow.workflow_model.model_server.model_server_name == 'creditNet':
            # Fetch the new selections
            run_level = formset['run_level'].value()
            # verbose_level = formset['verbose_level'].value()
            reporting_mode = formset['reporting_mode'].value()
            portfolio = formset['portfolio'].value()
            liabilities = formset['liabilities'].value()

            results_list = formset['results_list'].value()
            results_list = json.loads(results_list)

            # Update the JSON ticket
            workflow_data['input_set']['Portfolio'] = portfolio
            workflow_data['input_set']['Liabilities'] = liabilities
            # workflow_data['output_set']['Verbose_Level'] = verbose_level
            workflow_data['output_set']['Reporting_mode'] = reporting_mode
            workflow_data['output_set']['Results_list'] = results_list
            workflow_data['run_level'] = run_level
        else:
            portfolio = formset['portfolio'].value()
            results_list = formset['results_list'].value()
            results_list = json.loads(results_list)
            workflow_data['input_set']['Portfolio'] = portfolio
            workflow_data['output_set']['Results_list'] = results_list

        print("POST CALCULATION IN VIEW")

        workflow_data = json.dumps(workflow_data)
        print("WORKFLOW DATA IN VIEW: ", workflow_data)
        print("MODEL URL IN VIEW: ", model_url)

        response = None
        results_data = '{"You should not ever see this!"}'

        # post to internal model server at API endpoint
        try:
            response = requests.post(model_url, data=workflow_data, headers=headers, verify=False)
            print("0: RESPONSE STATUS IN VIEW: ", response.status_code)
            print("1: RESPONSE CONTENT IN VIEW: ", response.headers)
            print("2: RESPONSE CONTENT IN VIEW: ", response.text)
        except:
            results_data = '{"No Valid Server Response"}'

        # try to decode and parse the result send back by the model server
        try:
            response_decoded = response.json()
            print("3: DECODED JSON IN VIEW (RAW): ", )
            if 'results_data' in response_decoded:
                results_data = response_decoded['results_data']
            elif 'Run Level' in response_decoded:
                results_data = response_decoded['Timestamp']
            else:
                results_data = '{"No Valid Run Mode"}'
        except:
            results_data = {"No Parsable JSON in Server Response"}

        print("4: DECODED JSON IN VIEW (RESULTS_DATA): ", results_data)
        print("4: DECODED JSON IN VIEW (RESULTS_DATA): ", workflow_data)
        print("4: DECODED JSON IN VIEW (RESULTS_DATA): ", model_url)

    t = loader.get_template('workflow_explorer/workflow_interactive.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'object': workflow, 'formset': formset})
    context.update({'workflow_data': workflow_data})
    context.update({'results_data': results_data})
    context.update({'model_url': model_url})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def workflow_batch(request, pk):
    """
    Batch calculation of workflows using Ajax calls
    The view renders a page with

    **Context**

    ``Workflow``
        An instance of :model:`workflow_explorer.Workflow`.

    **Template:**

    :template:`workflow_explorer/workflow_calculate.html`
    """

    # get the workflow object
    workflow = Workflow.objects.get(pk=pk)
    model_url = workflow.workflow_model.model_server_url
    # serialize the workflow (including related objects like portfolio)
    serializer = WorkflowDetailSerializer(workflow, context={'request': request})
    workflow_data = json.dumps(serializer.data)
    # display the workflow in a custom form
    formset = WorkflowBatchForm(instance=workflow)
    t = loader.get_template('workflow_explorer/workflow_calculate.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'object': workflow, 'formset': formset})
    # pass the workflow data into the template for AJAX access
    context.update({'workflow_data': workflow_data})
    # pass the model server url to the template for AJAX access
    context.update({'model_url': model_url})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def playbook_calculate(request, pk):
    """
    Batch calculation of playbooks

    **Context**

    ``Playbook``
        An instance of :model:`workflow_explorer.Playbook`.

    **Template:**

    :template:`workflow_explorer/playbook_calculate.html`
    """

    print("REQUEST META ", request.META)
    # if post is done internally via Django Authenticated User
    try:
        print("------  USER BASED AUTHENTICATION   ------")
        auth = request.META['HTTP_AUTHORIZATION']
    except:
        # if post is done externally via JWT Authentication
        print("------  EXTERNAL JWT AUTHENTICATION   ------")
        print(request.user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        user = User.objects.get(username=request.user.username)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        auth = 'JWT {}'.format(token)
        # data = {'username': request.user.username, 'password': request.user.password}
        # response = requests.post(API_TOKEN_URL, data=data)
        print('AUTHENTICATION', auth)
        # auth = response.json()['token']

    # get the playbook object

    playbook = Playbook.objects.get(pk=pk)
    # serializer = PlaybookDetailSerializer(playbook, context={'request': request})
    # playbook_data = serializer.data

    context = RequestContext(request, {})
    # prepare the ticket
    headers = {'Content-Type': 'application/json', 'Authorization': auth}
    formset = None

    if request.method == 'GET':
        formset = PlaybookBatchForm(instance=playbook)
        # print('PLAYBOOK DATA IN GET VIEW', playbook_data)
        t = loader.get_template('workflow_explorer/playbook_calculate.html')
        context.update({'root_view': root_view, 'object': playbook, 'formset': formset})
        # # pass the workflow data into the template for AJAX access
        # context.update({'workflow_data': workflow_data})
        # # pass the model server url to the template for AJAX access
        # context.update({'model_url': model_url})
        return HttpResponse(t.template.render(context))

    # TODO Placeholder
    elif request.method == 'POST':
        formset = WorkflowInteractiveForm(request.POST)
        # print('PLAYBOOK DATA IN POST VIEW', playbook_data)
        current_user = request.user
        calculation_output = run_loop(playbook, auth, current_user)
        context.update({'root_view': root_view})
        t = loader.get_template('results_explorer/calculation_list.html')
        return HttpResponse(t.template.render(context))
        # return HttpResponseRedirect(reverse("results_explorer:results_view", args=[calculation_output['result_pk']]))


from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import modelform_factory
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from scenario_explorer.forms import ScenarioForm
from scenario_explorer.models import Scenario

root_view = settings.ROOT_VIEW


class ScenarioList(LoginRequiredMixin, ListView):
    model = Scenario
    template_name = 'scenario_explorer/scenario_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'root_view': root_view})
        return context


class ScenarioEdit(LoginRequiredMixin, UpdateView):
    model = Scenario
    form_class = modelform_factory(Scenario, exclude=None, fields='__all__')
    success_url = reverse_lazy('scenario_list')
    template_name_suffix = '_graphical_editor'

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context.update({'root_view': root_view})
        return context


@login_required(login_url='/login/')
def scenario_editor(request, pk):
    """
    Display for editing scenario data
    """

    if request.method == 'POST':
        formset = ScenarioForm(request.POST)
        if formset.is_valid():
            formset.save()
            scenario = Scenario.objects.get(pk=pk)
            return HttpResponseRedirect(scenario.get_absolute_url())
    else:
        try:
            scenario = Scenario.objects.get(pk=pk)
        except scenario.DoesNotExist:
            raise Http404("Scenario does not exist")

        formset = ScenarioForm(instance=scenario)

        # scenario_dict = {}
        # scenario_dict['name'] = scenario.name
        # scenario_dict['description'] = scenario.description
        # scenario_no = scenario.scenario_no
        # scenario_dict['factor_data'] = json.loads(scenario.factor_data)
        # scenario_dict['scenario_probabilities'] = json.loads(scenario.scenario_probabilities)

        t = loader.get_template('scenario_explorer/scenario_form_editor.html')
        context = RequestContext(request, {})
        context.update({'root_view': root_view, 'scenario': scenario, 'formset': formset})
        return HttpResponse(t.template.render(context))
