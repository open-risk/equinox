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


from django.db import models
from django.urls import reverse
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

from portfolio.Project import Project
from portfolio.ghg_choices import BASELINE_ESTIMATION_PROCEDURE

PROJECT_ACTIVITY_ROLE = [(0, 'Target'),
                         (1, 'Baseline')]


class ProjectActivity(models.Model):
    """
    The Project Activity model holds data for specific sustainability activities associated with a Project.

    The model acts as a container for both the target activity and alternative "baseline candidates"


    """
    # IDENTIFICATION

    project_activity_identifier = models.CharField(max_length=80, blank=True, null=True,
                                                   help_text='A unique identification of a Project Activity for internal use')

    project_activity_description = MarkdownField(blank=True, null=True, rendered_field='text_rendered',
                                                 validator=VALIDATOR_STANDARD,
                                                 help_text='Textual description of a Project Activity. Markdown format is supported <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/GHG_Project_Activity">Documentation</a>')

    text_rendered = RenderedMarkdownField()



    # LINKS

    project = models.ForeignKey('Project', blank=True, null=True, on_delete=models.CASCADE,
                                help_text="The Project to which this Activity belongs")

    # DATA

    project_activity_emissions = models.FloatField(blank=True, null=True, help_text="Emissions expressed in t CO2 eq/year")

    baseline_activity_emissions = models.FloatField(blank=True, null=True, help_text="Emissions expressed in t CO2 eq/year")

    project_activity_role = models.IntegerField(blank=True, null=True, choices=PROJECT_ACTIVITY_ROLE,
                                              help_text='Select whether the activity role is baseline or target')


    baseline_estimation = models.IntegerField(blank=True, null=True, choices=BASELINE_ESTIMATION_PROCEDURE,
                                              help_text='Baseline procedures are methods used to estimate baseline emissions <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Baseline_Emissions">Documentation</a>')

    baseline_procedure_justification = MarkdownField(blank=True, null=True, rendered_field='text_rendered2',
                                                     validator=VALIDATOR_STANDARD,
                                                     help_text='Justification of the Baseline Estimation Procedure selected <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Baseline_Emissions">Documentation</a>')

    # text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered2 = RenderedMarkdownField()

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_activity_identifier

    def get_absolute_url(self):
        return reverse('portfolio:ProjectActivity_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Project Activity"
        verbose_name_plural = "Project Activities"
