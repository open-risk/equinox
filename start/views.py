import re

import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView

# Front View
from start.models import DocPage


class Front(TemplateView):
    template_name = 'start/front.html'

    def get(self, request, *args, **kwargs):
        request.current_app = 'equinox'
        context = super(TemplateView, self).get_context_data(**kwargs)
        return self.render_to_response(context)


# Documentation View
class Documentation(LoginRequiredMixin, TemplateView):
    template_name = 'start/documentation.html'

    def get_context_data(self, **kwargs):
        docpages = DocPage.objects.all()
        doclist = []
        for page in docpages:
            # print(page.title, page.get_absolute_url())
            doclist.append((page.title, page.get_absolute_url(), page.get_category_display()))

        context = super(TemplateView, self).get_context_data(**kwargs)
        context.update({'doclist': doclist})
        return context


@login_required(login_url='/login/')
def documentation(request, slug):
    context = RequestContext(request, {})
    page = DocPage.objects.get(slug=slug)

    if page.doc_type == 1:
        page.content = markdown.markdown(page.content)
    # parse content page for url's and replace
    page.content = re.sub(r'{% url \'workflow_about\' %}', 'LINK', page.content)

    context.update({'page': page})

    t = loader.get_template('start/documentation_page.html')
    return HttpResponse(t.template.render(context))
