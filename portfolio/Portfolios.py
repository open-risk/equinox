from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from reference.nace_list import NACE_CHOICES
from reference.nuts3_list import NUTS3_CHOICES

from portfolio.PortfolioManager import PortfolioManager


class ProjectPortfolio(models.Model):

    """
        The ProjectPortfolio object holds a collection of Projects (Economic activities with defined environmental impact)

        Includes reference to the user creating the data set (portfolio manager)

        Portfolios are named to facilitate recognition

        Actual Portfolio data are optionally aggregated and stored in the PortfolioData model
        Timed Portfolio data are tagged using the PortfolioSnapshot model

        TODO "Notes" is a user oriented field to allow storing human readable context about the portfolio

        **Type** is an integer field representing the type of the portfolio
        0 -> Performing Book / Current Book
        1 -> Historical Book

    """

    # IDENTITY

    name = models.CharField(max_length=200, help_text="An assigned name to help identify the portfolio")

    # LINKS

    # user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user that created the portfolio")

    manager = models.ForeignKey(PortfolioManager, null=True, blank=True, on_delete=models.CASCADE,
                                help_text="The portfolio manager that manages the portfolio")

    # OTHER

    PORTFOLIO_TYPES = [(0, 'Performing'), (1, 'Historical')]

    notes = models.TextField(blank=True, null=True,
                             help_text="Description of the purpose or other relevant information about the portfolio")
    portfolio_type = models.IntegerField(default=0, choices=PORTFOLIO_TYPES,
                                         help_text='0=Performing Book, 1=Historical Book')

    # portfolio shape parameters (statistics)

    # max_rating = models.IntegerField(null=True, blank=True, help_text="Maximum rating")
    # min_rating = models.IntegerField(null=True, blank=True, help_text="Minimum rating")
    # mean_rating = models.IntegerField(null=True, blank=True, help_text="Average rating")
    #
    # max_lgd = models.IntegerField(null=True, blank=True, help_text="Maximum LGD")
    # min_lgd = models.IntegerField(null=True, blank=True, help_text="Minimum LGD")
    # mean_lgd = models.IntegerField(null=True, blank=True, help_text="Average LGD")
    #
    # max_ead = models.IntegerField(null=True, blank=True, help_text="Maximum EAD")
    # min_ead = models.IntegerField(null=True, blank=True, help_text="Minimum EAD")
    # mean_ead = models.IntegerField(null=True, blank=True, help_text="Average EAD")
    #
    # max_tenor = models.IntegerField(null=True, blank=True, help_text="Maximum Tenor")
    # min_tenor = models.IntegerField(null=True, blank=True, help_text="Minimum Tenor")
    # mean_tenor = models.IntegerField(null=True, blank=True, help_text="Average Tenor")
    #
    # country_no = models.IntegerField(null=True, blank=True, help_text="Number of Countries")
    # sector_no = models.IntegerField(null=True, blank=True, help_text="Number of Sectors")

    # TODO disabled for now
    # Reintroduce JSONField to hold flexible portfolio metadata
    # portfolio_data = JSONField()

    # bookkeeping
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:ProjectPortfolio_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Project Portfolio"
        verbose_name_plural = "Project Portfolios"


class PortfolioSnapshot(models.Model):
    """
    The Portfolio_Snapshot object helps group time-sensitive Portfolio data for a given cutoff date. The Snapshot may
    be named to facilitate recognition (E.g. Q1-2020).

    .. note:: The actual Snapshot data are stored in the various Models (with foreign keys to a portfolio snapshot)

    """
    name = models.CharField(blank=True, null=True, max_length=200,
                            help_text="An assigned name to help identify the snapshot. By convention the name of the portfolio plus the cutoff date")


    cutoff_date = models.DateTimeField(blank=True, null=True,
                                       help_text="Portfolio Cutoff Date (If available). Different from the creation date")

    # BOOKKEEPING
    creation_date = models.DateTimeField(auto_now_add=True,
                                         help_text="Date at which the snapshot has been created. Different from the cutoff date")
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:PortfolioSnapshot_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Snapshot"
        verbose_name_plural = "Portfolio Snapshots"


class PortfolioTable(models.Model):
    """
    The Portfolio Table object aggregates core (credit) portfolio data in a "master table" format to facilitate various quantitative portfolio analysis procedures


    """
    # TODO incorporate portfolio type based constraints

    portfolio_id = models.ForeignKey(ProjectPortfolio, on_delete=models.CASCADE)

    Obligor_ID = models.CharField(max_length=200, blank=True, null=True, help_text="Obligor ID")

    EAD = models.FloatField(blank=True, null=True)
    LGD = models.IntegerField(blank=True, null=True)
    Tenor = models.IntegerField(blank=True, null=True)

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
        return reverse('portfolio:portfolio_table_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Table"
        verbose_name_plural = "Portfolio Tables"


class LimitStructure(models.Model):
    """
    The LimitStructure object holds target (budget) oriented limit data

    Includes reference to user creating the budget scenario

    Each LimitStructure is named to facilitate recognition

    """

    name = models.CharField(max_length=200, help_text="An assigned name to help identify the limit structure")
    portfolio = models.ForeignKey(ProjectPortfolio, null=True, blank=True, on_delete=models.CASCADE, help_text="The portfolio to which the limit structure applies")
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
        return reverse('portfolio:limitstructure_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Limit Structure"
        verbose_name_plural = "Limit Structures"
