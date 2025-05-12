# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
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

import re

import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView

# Front View
from start.models import DocPage, ORMKeyword


class Front(TemplateView):
    template_name = 'start/front.html'

    def get(self, request, *args, **kwargs):
        request.current_app = 'equinox'
        context = super(TemplateView, self).get_context_data(**kwargs)
        return self.render_to_response(context)


# Feedback View (for public endpoint)
# class Feedback(ListView):
#     template_name = 'start/feedback.html'


class DocList(LoginRequiredMixin, TemplateView):
    template_name = 'start/doclist.html'

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


class Concepts(LoginRequiredMixin, TemplateView):
    template_name = 'start/concepts.html'

    def get_context_data(self, **kwargs):
        concepts = ORMKeyword.objects.all()
        keywordlist = []
        for concept in concepts:
            keywordlist.append((concept.keyword, concept.link + '/' + concept.slug, concept.tooltip))

        context = super(TemplateView, self).get_context_data(**kwargs)
        context.update({'keywordlist': keywordlist})
        return context
