from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from reference.nace_list import NACE_CHOICES
from reference.nuts3_list import NUTS3_CHOICES


class Portfolio(models.Model):
    """
    The Portfolio object holds a collection of Projects

    Includes reference to user creating the data set (portfolio manager)

    Portfolios are named to facilitate recognition

    The actual Portfolio data stored in the PortfolioData model

    Notes is a user oriented field to allow storing human readable context about the portfolio

    **Type** is an integer field representing the type of the portfolio
    0 -> Performing Book (default)
    1 -> Historical Book


    """

    PORTFOLIO_TYPES = [(0, 'Performing'), (1, 'Historical')]

    name = models.CharField(max_length=200, help_text="An assigned name to help identify the portfolio")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user that created the portfolio")
    notes = models.TextField(blank=True, null=True,
                             help_text="Description of the purpose or other relevant information about the portfolio")
    portfolio_type = models.IntegerField(default=0, choices=PORTFOLIO_TYPES,
                                         help_text='0=Performing Book, 1=Historical Book')

    # portfolio shape parameters (statistics)

    max_rating = models.IntegerField(null=True, blank=True, help_text="Maximum rating")
    min_rating = models.IntegerField(null=True, blank=True, help_text="Minimum rating")
    mean_rating = models.IntegerField(null=True, blank=True, help_text="Average rating")

    max_lgd = models.IntegerField(null=True, blank=True, help_text="Maximum LGD")
    min_lgd = models.IntegerField(null=True, blank=True, help_text="Minimum LGD")
    mean_lgd = models.IntegerField(null=True, blank=True, help_text="Average LGD")

    max_ead = models.IntegerField(null=True, blank=True, help_text="Maximum EAD")
    min_ead = models.IntegerField(null=True, blank=True, help_text="Minimum EAD")
    mean_ead = models.IntegerField(null=True, blank=True, help_text="Average EAD")

    max_tenor = models.IntegerField(null=True, blank=True, help_text="Maximum Tenor")
    min_tenor = models.IntegerField(null=True, blank=True, help_text="Minimum Tenor")
    mean_tenor = models.IntegerField(null=True, blank=True, help_text="Average Tenor")

    country_no = models.IntegerField(null=True, blank=True, help_text="Number of Countries")
    sector_no = models.IntegerField(null=True, blank=True, help_text="Number of Sectors")

    # TODO disabled for now
    # Reindroduce JSONField to hold flexible portolio metadata
    # portfolio_data = JSONField()

    # bookkeeping
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio_explorer:portfolio_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class PortfolioSnapshot(models.Model):
    """
    The Portfolio_Snapshot object groups Portfolio for a given cutoff date. The Snapshot may be named to facilitate recognition.

    .. note:: The actual Snapshot data are stored in the various Models (with foreign key to a snapshot)

    """

    creation_date = models.DateTimeField(auto_now_add=True,
        help_text="Date at which the snapshot has been created. Different from the cutoff date")
    last_change_date = models.DateTimeField(auto_now=True)

    cutoff_date = models.DateTimeField(blank=True, null=True,
                                       help_text="Portfolio Cutoff Date (If available). Different from the creation date")

    name = models.CharField(blank=True, null=True, max_length=200, help_text="An assigned name to help identify the snapshot. By convention the name of the portfolio plus the cutoff date")


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('portfolio:PortfolioSnapshot_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Snapshot"
        verbose_name_plural = "Portfolio Snapshots"


class PortfolioData(models.Model):
    """
    The PortfolioData object aggregates portfolio data in table format


    """
    # TODO incorporate portfolio type based constraint

    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    Obligor_ID = models.CharField(max_length=200)
    EAD = models.FloatField(blank=True, null=True, help_text="Exposure at Default")
    LGD = models.IntegerField(blank=True, null=True, help_text="Loss Given Default Class")
    Tenor = models.IntegerField(blank=True, null=True, help_text="Tenor (integer years)")

    # The field encodes using an integer key a dictionary of business (industry) sectors
    Sector = models.IntegerField(blank=True, null=True, choices=NACE_CHOICES, help_text="Business Sector")

    # The field encodes using an integer key a dictionary of geographical locations
    # Eg. countries, NUTS regions etc.
    Country = models.IntegerField(blank=True, null=True, choices=NUTS3_CHOICES, help_text="NUTS3 Region of Operations")

    # bookkeeping
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('portfolio_explorer:portfolio_data_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Data"
        verbose_name_plural = "Portfolio Data"


class LimitStructure(models.Model):
    """
    The LimitStructure object holds target (budget) oriented limit data

    Includes reference to user creating the budget scenario

    Each LimitStructure is named to facilitate recognition

    """

    name = models.CharField(max_length=200, help_text="An assigned name to help identify the limit structure")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user that created the limit structure")
    notes = models.TextField(blank=True, null=True,
                             help_text="Description of the purpose or other relevant information about the limit structure")

    # limit structure parameters

    # max_rating = models.IntegerField(null=True, blank=True, help_text="Maximum rating")
    min_rating = models.IntegerField(null=True, blank=True, help_text="Minimum rating")

    # max_lgd = models.IntegerField(null=True, blank=True, help_text="Maximum LGD class")
    min_lgd = models.IntegerField(null=True, blank=True, help_text="Minimum LGD class")

    max_ead = models.FloatField(null=True, blank=True, help_text="Maximum EAD")
    # min_ead = models.FloatField(null=True, blank=True, help_text="Minimum EAD")

    max_tenor = models.IntegerField(null=True, blank=True, help_text="Maximum Tenor (Years)")
    # min_tenor = models.IntegerField(null=True, blank=True, help_text="Minimum Tenor")

    # bookkeeping
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio_explorer:limitstructure_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Limit Structure"
        verbose_name_plural = "Limit Structures"
