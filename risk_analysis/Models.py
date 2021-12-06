from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ModelServer(models.Model):
    """Data object that holds model server configuration information.



    """

    MODEL_SERVER_TYPE = ((0, 'Python Library'),
                         (1, 'Web Service'))

    model_server_type = models.IntegerField(null=True, blank=True, default=0, choices=MODEL_SERVER_TYPE,
                                            help_text="Model Server Type")

    model_server_url = models.URLField(null=True, blank=True, help_text="A URL for a model server providing the model")

    model_server_name = models.CharField(max_length=200, null=True, blank=True,
                                         help_text="Internal name of the model server")

    model_server_description = models.TextField(null=True, blank=True,
                                                help_text="An extended description of the model server")

    def __str__(self):
        return self.model_server_name

    def get_absolute_url(self):
        return reverse('admin:model_server_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Model Server"
        verbose_name_plural = "Model Servers"


# Store Available Risk Model Definitions (Serialized RDF/XML)
class ModelDefinition(models.Model):
    """Data object holds the API Model definition (DOAM).

    The object is read only in this version
    Includes reference to user creating the data set
    Model Definition holds an RDF document

    TODO Remove duplication of information between model definition and model server
    For the moment kept so as not to break the current version of the API

    """

    name = models.CharField(max_length=200, help_text="The Model name precisely as used within OpenCPM "
                                                      "(capitalization / underscores are important!)")

    model_definition = models.TextField(blank=True, null=True, help_text="A RDF file containing Model metadata in "
                                                                         "accordance with the DOAM format")

    model_server = models.ForeignKey(ModelServer, null=True, blank=True,
                                     on_delete=models.CASCADE, help_text="The model server group")

    model_server_url = models.URLField(null=True, blank=True, help_text="A URL for a model server providing the model")

    model_server_name = models.CharField(default="creditnet", max_length=200, null=True, blank=True,
                                         help_text="Internal name of the model server")

    remote_model_url = models.URLField(blank=True, null=True, help_text="A remote URL where a model instance is live "
                                                                        "(only applicable for models served outside OpenCPM")

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('admin:model_definition_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Model Definition"
        verbose_name_plural = "Model Definitions"


class ModelConfiguration(models.Model):
    """
    Data object holds model configuration parameters
    TODO Generalize from ScenarioEngine Requirements


    """

    MODEL_MODE_CHOICES = ((0, 'DryRun'),
                          (1, 'Analytic Calculation'),
                          (2, 'Copula Simulation'),
                          (3, 'Asymptotic Enumerated'),
                          (4, 'Standard Simulation'),
                          (5, 'Confidence Capital'),
                          (6, 'Snapshot Generator'),
                          (7, 'Markov Simulation'),
                          (8, 'AIRB'),
                          (9, 'Macro Simulation'))

    SCENARIO_METHOD_CHOICES = ((1, 'Simulated Macro'),
                               (2, 'Enumerated Macro'),
                               (3, 'Simulate + Enumerate'),
                               (4, 'Enumerate + Simulate'))

    LGD_METHOD_CHOICES = ((0, 'Fixed LGD Percentage'),
                          (1, 'Stochastic LGD'))

    CORRELATION_METHOD_CHOICES = [(0, 'Single Factor(No Correlation Matrix Input)'),
                                  (1, 'Multi Factor (With Macro Correlation Matrix Input)')]

    INTERVAL_METHOD_CHOICES = [(0, 'Annual'), (1, 'Monthly'), (2, 'Quarterly')]

    model_configuration_name = models.CharField(max_length=200, help_text="The Model Configuration name")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    model = models.ForeignKey(ModelDefinition, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True, null=True, help_text="Description of the Model Configuration")
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    Analytic_Tests = models.IntegerField(null=True, blank=True, help_text="Whether to produce analytic tests")
    BranchScenarios = models.IntegerField(null=True, blank=True, help_text="Number of branch scenarios")
    MacroScenarios = models.IntegerField(null=True, blank=True, help_text="Number of macro scenarios")

    FactorScenarios = models.IntegerField(null=True, blank=True, help_text="Number of Factor scenarios")
    PortfolioScenarios = models.IntegerField(null=True, blank=True,
                                             help_text="Number of idiosyncratic portfolio scenarios")

    CorrelationMethod = models.IntegerField(default=0, null=True, blank=True, choices=CORRELATION_METHOD_CHOICES,
                                            help_text="Select the correlation method")
    Factors = models.IntegerField(null=True, blank=True, help_text="Number of Factors")

    Interval = models.IntegerField(default=0, null=True, blank=True, help_text="Temporal Interval Method")

    MaturityMethod = models.IntegerField(null=True, blank=True, help_text="Maturity method")
    ModelMethod = models.IntegerField(null=True, blank=True, choices=MODEL_MODE_CHOICES,
                                      help_text="Model method (where applicable")
    ScenarioMethod = models.IntegerField(null=True, blank=True, choices=SCENARIO_METHOD_CHOICES,
                                         help_text="Scenario method (where applicable)")
    ScenarioPeriods = models.IntegerField(null=True, blank=True, help_text="Scenario Periods")

    LGDMethod = models.IntegerField(null=True, blank=True, choices=LGD_METHOD_CHOICES,
                                    help_text="LGD Model Method")
    # DefaultOnly = models.NullBooleanField(null=True, blank=True, help_text="Default only mode")
    # EquityCapital = models.FloatField(null=True, blank=True, help_text="Equity capital")
    CalculationHorizon = models.IntegerField(null=True, blank=True, help_text="Modeling horizon")
    Ratings = models.IntegerField(null=True, blank=True, help_text="Number of rating classes")
    RiskHorizon = models.IntegerField(null=True, blank=True, help_text="Risk horizon")
    RatingPeriods = models.IntegerField(null=True, blank=True, help_text="Rating system periods")
    StageGap = models.IntegerField(null=True, blank=True, help_text="IFRS 9 Stage Gap")
    LiabilityMethod = models.IntegerField(null=True, blank=True, help_text="Liability method")
    Resolution = models.IntegerField(null=True, blank=True, help_text="Resolution")
    Order = models.IntegerField(null=True, blank=True, help_text="AR Model order")

    # For concentration risk analysis
    Parameters = models.JSONField(null=True, blank=True, help_text="Flexible Parameter Field")

    def __str__(self):
        return self.model_configuration_name

    def get_absolute_url(self):
        return reverse('admin:model_configuration_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Model Configuration"
        verbose_name_plural = "Model Configurations"


# Store User Model Parametrization Data
class ModelData(models.Model):
    """
    Data object holds additional required model data that are not available as distinct data sources
    The object is read/write
    Includes reference to the models that can consume the data
    Includes reference to user creating the data set
    Model Data field stores a flexible data structure
    Optional fields with flexible structure. Examples
        'Factors' : Scalar
        'Scenario' : Array
        'Transition Matrix': Matrix
    """
    #    TODO: Implement example of distinct model data storage
    #    TODO: Enable link with eve dataseries object

    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    model = models.ForeignKey(ModelDefinition, on_delete=models.CASCADE, default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)
    model_data = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('admin:model_explorer_modeldata_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Model Data"
        verbose_name_plural = "Model Data"
