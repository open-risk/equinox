# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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

from portfolio.model_choices import *


class Project(models.Model):
    """
    The Project model holds data for a general sustainability Project (irrespective of financial attributes)


    """

    # TODO Project Status

    # IDENTIFICATION

    project_identifier = models.CharField(max_length=80, blank=True, null=True,
                                          help_text='A unique identification of the Project for internal use')

    project_title = models.CharField(max_length=160, blank=True, null=True, verbose_name='Title',
                                     help_text='The title of the project')

    project_reference = models.CharField(max_length=160, blank=True, null=True,
                                         help_text='Manager reference for the project')

    # LINKS

    project_category = models.ForeignKey('ProjectCategory', blank=True, null=True, verbose_name='Category',
                                         on_delete=models.SET_NULL,
                                         help_text="The project category to which this project is best classified")

    portfolio = models.ForeignKey('ProjectPortfolio', blank=True, null=True, on_delete=models.CASCADE,
                                  help_text="The portfolio to which this project belongs")

    snapshot = models.ForeignKey('PortfolioSnapshot', on_delete=models.CASCADE, blank=True, null=True,
                                 help_text="The portfolio snapshot to which the project belongs")

    # PROJECT DATA

    project_description = MarkdownField(blank=True, null=True, default="", rendered_field='text_rendered',
                                        validator=VALIDATOR_STANDARD,
                                        help_text='Textual description of a Project. Markdown format is supported <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/GHG_Project">Documentation</a>')

    # text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()

    cpv_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='CPV',
                                help_text="The Common Procurement Vocabulary Code (Main Code)")

    cpa_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='CPA',
                                help_text="The Classification of Products by Activity Code")

    country = models.CharField(max_length=40, null=True, blank=True,
                               help_text='Country where the project is originated (not necessarily of performance')

    region = models.CharField(max_length=10, null=True, blank=True, verbose_name='Region',
                              help_text='NUTS Code of Region where the project takes place.')

    project_budget = models.IntegerField(blank=True, null=True, help_text="The Project Budget", verbose_name='Budget')

    project_currency = models.CharField(max_length=4, blank=True, null=True, verbose_name='Currency',
                                        help_text="The currency code in which the project is accounted for")

    # PROJECT SCORECARD DATA

    design_and_technology_risk = models.IntegerField(blank=True, null=True, choices=DESIGN_AND_TECHNOLOGY_RISK_CHOICES,
                                                     help_text='Risk Factor. EBA 3.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Technology_Risk">Documentation</a>')

    completion_risk = models.IntegerField(blank=True, null=True, choices=COMPLETION_RISK_CHOICES,
                                          help_text='Risk SubFactor. EBA 3.2.3. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # OTHER

    construction_risk = models.FloatField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    project_visualization = models.ImageField(upload_to='project_files', blank=True, null=True,
                                              help_text='Visual representation of a  Project')
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
