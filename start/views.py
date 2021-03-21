from django.shortcuts import render
from django.views.generic import TemplateView


# Front View
class Front(TemplateView):
    template_name = 'start/front.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return context
