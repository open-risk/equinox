# Copyright (c) 2021 Open Risk (https://www.openriskmanagement.com)
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


from django.db import models
from portfolio.ProjectCategory import ProjectCategory
from django.urls import reverse
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class Project(models.Model):
    """
    The Project model holds data for a general sustainability Project (irrespective of financial aspects)


    """

    project_identifier = models.TextField(blank=True, null=True,
                                          help_text='A unique identification of the Project for internal use')

    project_description = MarkdownField(blank=True, null=True, rendered_field='text_rendered',
                                        validator=VALIDATOR_STANDARD,
                                        help_text='Textual description of a  Project. Markdown format is supported <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/GHG_Project">Documentation</a>')

    # text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()

    project_visualization = models.ImageField(upload_to='project_files', blank=True, null=True,
                                              help_text='Visual representation of a  Project')

    project_category = models.ForeignKey('ProjectCategory', blank=True, null=True, on_delete=models.CASCADE)

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Project_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
