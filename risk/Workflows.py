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

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# from model_explorer.models import ModelDefinition, ModelConfiguration, ModelData
from portfolio.Portfolios import ProjectPortfolio, LimitStructure
from risk.Scenarios import Scenario
from risk.models import ModelDefinition, ModelData, ModelConfiguration

OBJECTIVE_CHOICE = [(0, 'Portfolio Information'), (1, 'Concentration Risk'), (2, 'Origination'), (3, 'Risk Appetite'), (4, 'Risk Capital'), (5, 'Other')]

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
    workflow_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=INTERACTIVE)

    # Default objective is risk appetite
    objective = models.IntegerField(default=3, null=True, blank=True, choices=OBJECTIVE_CHOICE,
                                    help_text="Objective category of the limitflow")

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    workflow_id = models.CharField(default='CN_0000', max_length=200, help_text="Serial Number Workflow"
                                                                                "in the format MM_NNNN ")

    workflow_description = models.TextField(default="Default Description", null=True, blank=True,
                                            help_text="A description of the main purpose and "
                                                      "characteristics of the workflow")

    workflow_status = models.IntegerField(default=0, choices=WORKFLOW_STATUS_CHOICE,
                                          help_text='Draft/Published Status (Default=Draft)')

    api_version = models.CharField(default="0.4", max_length=50, null=True, blank=True,
                                   help_text="The API version to which the Workflow conforms")

    #
    # DATA TO CONSTRUCT THE INPUTS CONFIGURATION

    #
    # Foreign Key Relations
    #
    workflow_model = models.ForeignKey(ModelDefinition, on_delete=models.CASCADE, null=True, blank=True,
                                       help_text="The Model on which the workflow is based")

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
        return reverse('workflow_explorer:limitflow_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Limitflow"
        verbose_name_plural = "Limitflows"


class Workflow(models.Model):
    """
    The Workflow Data object holds the structural specification of an elementary workflow calculation

    Includes reference to user creating the workflow


    """


    WORKFLOW_STATUS_CHOICE = [(0, 'Draft'), (1, 'Published'), (2, 'Broken')]

    DEBUG = '0'
    BATCH = '1'
    INTERACTIVE = '2'
    # PARAMETRIC is obsolete (superseded by Playbook functionality)
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
    VERBOSITY_CHOICE = ((n, str(n)) for n in range(4))
    RUN_LEVEL_CHOICE = ((2, 'Model Configuration'),
                        (3, 'Model Data'),
                        (4, 'Scenario Data'),
                        (5, 'Asset Data'),
                        (6, 'Liability Data'),
                        (7, 'Diagnostic Tests'),
                        (8, 'Model Calculation'),
                        (9, 'Reporting'))


    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1, help_text="The creator of the workflow")

    # Equinox Workflow Type. Serialized But in Schema / Not Used Externally
    workflow_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=INTERACTIVE)

    # Equinox Objective. Not Used Externally
    # TODO align with linkage to objective via playbook
    objective = models.IntegerField(default=0, null=True, blank=True, choices=OBJECTIVE_CHOICE,
                                    help_text="Objective category of the workflow")

    # Equinox History Tracking. Not used Externally
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    #
    #  SECTION 1: MUST VALIDATE AGAINST JSON SCHEMA
    #
    # "required": [
    # L1 Attributes
    #     "name",
    #     "workflow_id",
    #     "workflow_description",
    #     "workflow_status",
    #     "run_level",
    #     "api_version",
    #     "model_server"
    #     "remote_model_url",
    # L2 Objects
    #     "model_configuration",
    #     "model_data",
    #     "input_set",
    #     "output_set",
    # ]

    name = models.CharField(default="Default Name", max_length=200,
                            help_text="Assigned name to help manage workflow collections")

    workflow_id = models.CharField(default='CN_0000', max_length=200,
                                   help_text="Serial Number of the Workflow in the format MM_NNNN."
                                             "It is NOT the same as the database ID (pk) ")

    workflow_description = models.TextField(default="Default Description", null=True, blank=True,
                                            help_text="A description of the main purpose and "
                                                      "characteristics of the workflow")

    workflow_status = models.IntegerField(default=0, choices=WORKFLOW_STATUS_CHOICE,
                                          help_text='Draft/Published Status (Default=Draft)')

    # Run Level is only usefully for more complex models that have substantial internal structure
    run_level = models.IntegerField(default=7, null=True, blank=True, choices=RUN_LEVEL_CHOICE,
                                    help_text="Run level (for debug purposes only")

    api_version = models.CharField(default="0.4", max_length=50, null=True, blank=True,
                                   help_text="The API version to which the Workflow conforms")

    #
    # The Foreign Key Relations of the Workflow
    #


    workflow_model = models.ForeignKey(ModelDefinition, on_delete=models.CASCADE, null=True, blank=True,
                                       help_text="The Model on which the workflow is based")
    #
    # Model Configuration and Model Data are always exposed completely as nested objects
    #
    model_configuration = models.ForeignKey(ModelConfiguration, on_delete=models.CASCADE, null=True, blank=True,
                                            help_text="The stored Model Configuration set to use for this workflow")

    model_data = models.ForeignKey(ModelData, on_delete=models.CASCADE, null=True, blank=True,
                                   help_text="Additional model data to use in this workflow")

    #
    # These foreign keys are provided as API URL's
    #

    portfolio = models.ForeignKey(ProjectPortfolio, on_delete=models.CASCADE, null=True, blank=True,
                                  help_text="The Portfolio to use with the Workflow")


    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=True, blank=True,
                                 help_text="The Scenario Data to use with Workflow")


    # This stores local disk directory (not used in online mode)
    # For compatibility with serialized workflow catalogs in disk
    root_dir = models.CharField(default="", max_length=200, null=True, blank=True,
                                help_text="Root directory for distribution files")


    single_asset_flag = models.BooleanField(default=False, help_text="Set to TRUE for single asset portfolio")


    # DATA TO CONSTRUCT THE OUTPUTS CONFIGURATION
    reporting_mode = models.IntegerField(default=0, null=True, blank=True, choices=REPORTING_CHOICE,
                                         help_text="The type of report to produce")
    results_url = models.CharField(default="", max_length=200, null=True, blank=True,
                                   help_text="Where to store the results")

    results_list = models.JSONField(default=dict, null=True, blank=True,
                             help_text="List of desired result items (when applicable")

    scenario_output = models.IntegerField(default=0, null=True, blank=True,
                                          help_text="What type of snapshot output to create")
    verbose_level = models.IntegerField(default=1, null=True, blank=True, choices=VERBOSITY_CHOICE,
                                        help_text="The verbosity level of logging")

    # ATTN: HOLDS AD-HOC DATA
    # Not part of JSON Schema
    portfolio_data = models.JSONField(default=dict, null=True, blank=True,
                               help_text="Container for portfolio data. Not part of JSON Schema 0.4")

    scenario_data = models.JSONField(default=dict, null=True, blank=True,
                              help_text="Container for scenario data. Not part of JSON Schema 0.4")

    # LEGACY FIELDS (Not stored in Workflow Model, compiled on the fly)
    # input_set = models.TextField(blank=True)
    # output_set = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow_explorer:workflow_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Workflow"
        verbose_name_plural = "Workflows"
