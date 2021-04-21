from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Front View
class Front(TemplateView):
    template_name = 'start/front.html'

    def get(self, request, *args, **kwargs):
        request.current_app = 'equinox'
        context = super(TemplateView, self).get_context_data(**kwargs)
        return self.render_to_response(context)
