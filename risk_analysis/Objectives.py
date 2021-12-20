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

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# from model_explorer.models import ModelDefinition, ModelConfiguration, ModelData
from portfolio.Portfolios import Portfolio, LimitStructure
from risk_analysis.Scenarios import Scenario
from risk_analysis.Workflows import Workflow

# Global specification of the objective categories (used by both Objective and Workflow Models)

# TODO Refactor into
# CommonFlow / ModelFlow, IndexFlow, LimitFlow etc

OBJECTIVE_CHOICE = [(0, 'Portfolio Information'), (1, 'Concentration Risk'), (2, 'Origination'), (3, 'Risk Appetite'), (4, 'Risk Capital'), (5, 'Other')]


class Playbook(models.Model):
    """

    Single Run              single_run
    Benchmark Run           benchmark_calculation (external)
    External Convergence    convergence_run + benchmark_calculation
    Internal Convergence    single_run, parametric sequence (single_run)
    Cauchy Convergence      parametric sequence (single_run)
    Parametric Portfolio    parametric sequence (single_run)
    Parametric Model        parametric sequence (single_run)
    Random Sequence         parametric sequence (single_run)

    WORKFLOW DELTA SPECIFICATION

    Type: Parametric Model - Changes the some model configuration aspect
    "ModelParameter": ["model_configuration", "CorrelationMethod"],
    "ModelParameterRange": [0, 1],

    Type: Internal Convergence - Changes model configuration - compares internally different options
    "ModelParameter": ["model_configuration", "MacroScenarios"],
    "ModelParameterRange": [100, 1000, 3000, 10000],

    Type: Cauchy Convergence - Changes model configuration - computes successive approximations
    "ModelParameter": ["model_configuration", "BranchScenarios"],
    "ModelParameterRange": [1, 2,],

    Type: Parametric Portfolio
    "PortfolioParameter": ["portfolio_config", "Rating" ],
    "PortfolioParameterRange": [0, 1, ],

    "Parameter": ["model_configuration", "EquityCapital"],
    "ParameterRange": [0.1],

    Type: Random Scenario
    "ScenarioDataParameter": ["scenario_probabilities"],

    {
      "Type": "Parametric Portfolio",
      "TestName": "ScenarioEngine 0.3 Parameter Survey",

      WORKFLOW DATA (DUPLICATED / OVERRIDDEN)
      "BuildDir": "cmake-build-release/",
      "ExecName": "ScenarioEngine",
      "WorkflowDir": "Workflows/",
      "Workflow": "workflow_data_CECL_PORTFOLIO_SURVEY.json",
      "PortfolioDir": "Portfolios/",
      "PortfolioFile": "synthetic_data.json",
      "OutputDir": "Results/",
      "ResultsDir": "results/CECL_PORTFOLIO_SURVEY/",
      "SimOutputFile": "output.json",

      REPORTING SELECTORS (DUPLICATED / OVERRIDDEN)
      "ShowOutput": "False",
      "ShowLogFile": "False",
      "ShowFigure": "False",
      "ShowTernary": "True",
      "ShowTable": "False",

      "TestModelParamsFile": "testparams.json",
      "TestOutputFile": "analytic.json",
    }

    """
    # TODO develop YAML parsing / reporting etc.

    PLAYBOOK_TYPE = [(0, 'Parametric Portfolio Sequence'),
                     (1, 'Parametric Model Configuration'),
                     (2, 'Defender / Challenger Calculation'),
                     (3, 'Single Run'),
                     (4, 'Parametric Scenario'),
                     (5, 'Random Scenario'),
                     (6, 'Cauchy Convergence'),
                     (7, 'Internal Convergence'),
                     (8, 'External Convergence')]

    PLAYBOOK_STATUS_CHOICE = [(0, 'Draft'), (1, 'Published'), (2, 'Broken')]

    name = models.CharField(max_length=200, help_text="Assigned name to help manage playbooks")
    description = models.TextField(null=True, blank=True, help_text="A description of the main purpose and "
                                                                    "characteristics of the playbook")

    type = models.IntegerField(default=3, null=True, blank=True, choices=PLAYBOOK_TYPE,
                               help_text="The type of the playbook. Determines what post-processing must be performed")

    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, null=True, blank=True,
                                 help_text="The Workflow on which the playbook is based")

    benchmark_workflow = models.ForeignKey(Workflow, related_name='benchmark_workflow', on_delete=models.CASCADE,
                                           null=True, blank=True,
                                           help_text="A Benchmark Workflow used by the playbook")

    parameter_field = models.JSONField(default=dict, null=True, blank=True,
                                help_text="The workflow parameter field varied by the playbook "
                                          "a list of attibutes when nested")

    parameter_range = models.JSONField(default=dict, null=True, blank=True,
                                help_text="A list of parameter values to be iterated over when"
                                          "executing the playbook")

    api_version = models.CharField(default="0.1", max_length=50, null=True, blank=True,
                                   help_text="The API version to which the Playbook conforms")

    playbook_status = models.IntegerField(default=0, choices=PLAYBOOK_STATUS_CHOICE,
                                          help_text='Draft/Published Status (Default=Draft) of the Playbook')

    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    last_change_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow_explorer:playbook_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Playbook"
        verbose_name_plural = "Playbooks"


class Objective(models.Model):
    """
    The Objective Data object holds the high level definition of a portfolio management objective. It is aimed to be (eventually) a valid YAML specification

    **Example**

    Objective 1: Establish internal convergence of copula simulation against analytic calculation

    Playbook: 'playbooks/scenario_engine_cecl_convergence_copula.json'

    Raw Artefacts:
    - ScenarioEngine reporting json object: results/CECL_CONVERGENCE_COPULA/output_VALUE.json
    - ScenarioEngine log file:		Logs/workflow_ID.log

    Processed Artefacts:
    - Convergence Reporting in csv format: results/CECL_CONVERGENCE_COPULA/convergence_results.csv
    - Convergence Plot in svg format (via interactive matplotlib session): results/CECL_CONVERGENCE_COPULA/convergence_results.svg

    Conclusion: We have some sort of convergence

    """
    # TODO develop YAML parsing / reporting etc.

    name = models.CharField(max_length=200, help_text="Assigned name to help manage objectives")
    description = models.TextField(null=True, blank=True, help_text="A description of the main purpose and "
                                                                    "characteristics of the Objective")

    playbook = models.ForeignKey(Playbook, on_delete=models.CASCADE, null=True, blank=True,
                                 help_text="The playbook on which the objectives is based")

    category = models.IntegerField(default=0, null=True, blank=True, choices=OBJECTIVE_CHOICE,
                                   help_text="Objective category")

    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    last_change_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow_explorer:objective_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Objective"
        verbose_name_plural = "Objectives"
