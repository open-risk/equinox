from django.db import models
from django.urls import reverse


class Scenario(models.Model):
    """
    Data object holds the complete dataset for an economic scenario analysis (observable factors)
    Data are stored in JSON format to preserve flexibility

    """

    # main data for the DataEndPoint model
    name = models.CharField(max_length=80)

    # scenario description
    description = models.TextField(blank=True, null=True, help_text="Description")

    # number of scenarios
    scenario_no = models.IntegerField(default=1, help_text="Number of Scenarios")
    # number of factors
    factor_no = models.IntegerField(default=1, help_text="Number of Factors")
    # number of timepoints
    timepoint_no = models.IntegerField(default=1, help_text="Number of Timepoints (Periods + 1)")

    # Scenario data is a collection of dataseries
    # Related to eve.DataSeries (but distinct - not historical data)
    # Each dataseries has a set of dates and values and other metadata
    # The dates are common by construction
    # Stucture is a dict of arrays
    # {
    #   "Factor1" : [Values x N],
    #   "Factor2" : [Values x N],
    #   "FactorM" : [Values x N],
    #
    #   Timepoints are currently implicit (simply 0, .... , N)
    # TODO Specify explicitly
    #   "Timepoints" : [Values]
    #  }

    factor_data = models.JSONField(blank=True, null=True)

    # Scenario probabilities (List of size scenario_no, Must sum to one)
    scenario_probabilities = models.JSONField(blank=True, null=True)

    # general purpose data
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('DataSeries_list', kwargs={'name': self.name})
        return reverse('risk_analysis:Scenario', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Scenario"
        verbose_name_plural = "Scenarios"
