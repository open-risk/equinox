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

from django.db import models
from django.urls import reverse


class Scenario(models.Model):
    """
    The Scenario data object holds the complete dataset for an environmental / economic scenario projection (observable factors) NB: The quantitative data are stored in JSON format to preserve flexibility

    The Scenario data is a collection of data timeseries
    Each dataseries has a set of dates and values and other metadata
    The dates are common by construction
    The structure is a dict of arrays, one for each factor
     {
       "Factor1" : [Values x N],
       "Factor2" : [Values x N],
       "FactorM" : [Values x N],
     }

    Timepoints are specified explicitly (and are assumed common measurement points for all factors)
      "Timepoints" : [Values]
     }

    """

    # IDENTIFICATION

    # the name of the scenario
    name = models.CharField(max_length=200, help_text="A way to identify the scenario projection")

    # scenario description
    description = models.TextField(blank=True, null=True, help_text="Scenario Description")

    # LINKS
    # TODO link with portfolio entities
    # portfolio = models.ForeignKey('Portfolio', blank=True, null=True, on_delete=models.CASCADE)

    # SCENARIO DATA

    cutoff_date = models.CharField(max_length=80, blank=True, null=True,
                                   help_text="Scenario Cutoff Date, Base Year or similar Time Reference")

    scenario_type = models.CharField(blank=True, null=True, max_length=80, help_text="Scenario Type or Category")

    # number of scenarios. this supports bundled projections (possibly with probabilities attached to each project)
    scenario_no = models.IntegerField(default=1, help_text="Number of Scenarios")
    # Scenario probabilities (must sum to one)
    scenario_probabilities = models.JSONField(blank=True, null=True,
                                              help_text="Scenario Probabilities (Optional). For mathematical consistency must add to unity")

    # number of factors projected per scenario. this supports multi-factor (multi-variable)
    factor_no = models.IntegerField(blank=True, null=True, default=1,
                                    help_text="The Number of Scenario Factors (Variables)")

    factor_values = models.JSONField(blank=True, null=True,
                                     help_text="Factor Values under the Projection as a Dict (See Docs)")

    factor_units = models.JSONField(blank=True, null=True, help_text="Factor Variable Name / Units")

    # number of timepoints
    timepoint_no = models.IntegerField(default=1, help_text="Number of Timepoints (Periods + 1)")
    timepoints = models.JSONField(blank=True, null=True, help_text="Timepoint Values")

    # general purpose data
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('risk:scenario_form_editor', kwargs={'pk': self.pk})
        return reverse('risk:scenario_graphical_editor', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Scenario"
        verbose_name_plural = "Scenarios"
