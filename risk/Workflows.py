# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from portfolio.Portfolios import ProjectPortfolio, LimitStructure
from risk.Scenarios import Scenario

OBJECTIVE_CHOICE = [(0, 'Portfolio Information'), (1, 'Concentration Risk'), (2, 'Origination'), (3, 'Risk Appetite'),
                    (4, 'Risk Capital'), (5, 'Other')]


# Global specification of the objective categories (used by both Objective and Workflow Models)

# TODO Refactor into
# CommonFlow / ModelFlow, IndexFlow, LimitFlow etc


class Limitflow(models.Model):
    """
    The Limit Flow Data object holds the structural specification of a limit framework workflow calculation

    Includes reference to user creating the workflow

    """

    # TODO Inherit from workflow class

    WORKFLOW_STATUS_CHOICE = [(0, 'Draft'), (1, 'Published'), (2, 'Broken')]

    DEBUG = '0'
    BATCH = '1'
    INTERACTIVE = '2'
    PARAMETRIC = '3'
    STUB = '4'
    TYPE_CHOICES = (
        (DEBUG, 'Debug'),
        (BATCH, 'Batch'),
        (INTERACTIVE, 'Interactive'),
        (PARAMETRIC, 'Parametric'),
        (STUB, 'Stub'),
    )

    REPORTING_CHOICE = ((n, str(n)) for n in range(4))

    name = models.CharField(default="Default Name", max_length=200,
                            help_text="Assigned name to help manage workflow collections")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1, help_text="The creator of the workflow")
    workflow_type = models.CharField(null=True, blank=True, max_length=2, choices=TYPE_CHOICES, default=INTERACTIVE)

    # Default objective is risk appetite
    objective = models.IntegerField(default=3, null=True, blank=True, choices=OBJECTIVE_CHOICE,
                                    help_text="Objective category of the limitflow")

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    workflow_id = models.CharField(null=True, blank=True, default='CN_0000', max_length=200,
                                   help_text="Serial Number Workflow"
                                             "in the format MM_NNNN ")

    workflow_description = models.TextField(default="Default Description", null=True, blank=True,
                                            help_text="A description of the main purpose and "
                                                      "characteristics of the workflow")

    workflow_status = models.IntegerField(null=True, blank=True, default=0, choices=WORKFLOW_STATUS_CHOICE,
                                          help_text='Draft/Published Status (Default=Draft)')

    api_version = models.CharField(default="0.4", max_length=50, null=True, blank=True,
                                   help_text="The API version to which the Workflow conforms")

    #
    # DATA TO CONSTRUCT THE INPUTS CONFIGURATION

    #
    # Foreign Key Relations
    #
    # workflow_model = models.ForeignKey(ModelDefinition, on_delete=models.CASCADE, null=True, blank=True,
    #                                    help_text="The Model on which the workflow is based")

    portfolio = models.ForeignKey(ProjectPortfolio, on_delete=models.CASCADE, null=True, blank=True,
                                  help_text="The Portfolio to use with the Workflow")

    limit_structure = models.ForeignKey(LimitStructure, on_delete=models.CASCADE, null=True, blank=True,
                                        help_text="The Limit Structure to use with the Workflow")

    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=True, blank=True,
                                 help_text="The Scenario Data to use with Workflow")

    # DATA TO CONSTRUCT THE OUTPUTS CONFIGURATION
    reporting_mode = models.IntegerField(default=0, null=True, blank=True, choices=REPORTING_CHOICE,
                                         help_text="The type of report to produce")
    results_url = models.CharField(default="", max_length=200, null=True, blank=True,
                                   help_text="Where to store the results")

    results_list = models.JSONField(default=dict, null=True, blank=True,
                                    help_text="List of desired result items (when applicable")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('risk:limitflow_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Limitflow"
        verbose_name_plural = "Limitflows"
