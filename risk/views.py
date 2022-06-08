from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from risk.Scenarios import Scenario
from risk.forms import ScenarioForm


class ScenarioEdit(LoginRequiredMixin, UpdateView):
    model = Scenario
    form_class = modelform_factory(Scenario, exclude=None, fields='__all__')
    success_url = reverse_lazy('scenario_list')
    template_name_suffix = '_graphical_editor'

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        return context


@login_required(login_url='/login/')
def scenario_editor(request, pk):
    """
    Display for editing scenario data
    """

    scenario = None
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
        # scenario_dict['factor_values'] = json.loads(scenario.factor_values)
        # scenario_dict['scenario_probabilities'] = json.loads(scenario.scenario_probabilities)

        t = loader.get_template('scenario_form_editor.html')
        context = RequestContext(request, {})
        context.update({'scenario': scenario, 'formset': formset})
        return HttpResponse(t.template.render(context))
