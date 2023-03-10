# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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

# The IPCC Gases
GHG_GAS_CHOICES = [(0, 'CO2e'),
                   (1, 'CO2'),
                   (2, 'CH4'),
                   (3, 'N2O'),
                   (4, 'SF6'),
                   (5, 'CF4'),
                   (6, 'C2F6'),
                   (7, 'NF3'),
                   (8, 'CHF3'),
                   (9, 'CH2F2'),
                   (10, 'CH3F'),
                   (11, 'C2HF5'),
                   (12, 'C2H2F4'),
                   (13, 'CH2FCF3'),
                   (14, 'C2H3F3'),
                   (15, 'C2H4F3'),
                   (16, 'C2H4F2'),
                   (17, 'C3HF7'),
                   (18, 'C3H2F6'),
                   (19, 'C3H3F5')]

NOTATION_KEYS = [(0, 'NO'), (1, 'IE'), (2, 'C'),
                 (3, 'NE'), (4, 'NA')]

# GPC Data Quality Categories
GPC_DQ_KEYS = [(0, 'L'), (1, 'M'), (2, 'H')]

# PCAF Data Quality Categories
PCAF_DQ_KEYS = [(1, 'Score 1'), (2, 'Score 2'), (3, 'Score 3'), (4, 'Score 4'), (5, 'Score 5')]


class EmissionsSource(models.Model):
    """
    The Emission Source model holds granular activity and emissions type data that characterize and quantify the emissions of an Asset.

    An asset may involve multiple emissions sources


    """

    # IDENTITY

    source_identifier = models.CharField(max_length=80, null=True,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS

    asset = models.ForeignKey('portfolio.ProjectAsset', blank=True, null=True, on_delete=models.CASCADE,
                              help_text="Asset to which this source belongs")

    emissions_factor = models.ForeignKey('reference.EmissionFactor', blank=True, null=True, on_delete=models.CASCADE,
                                         help_text="Applicable Emissions Factor")

    # CHARACTERISTICS

    emitted_gas = models.IntegerField(blank=True, null=True,
                                      choices=GHG_GAS_CHOICES,
                                      help_text='Type of GHG Emission. Choose CO2e if already aggregated')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_identifier

    def get_absolute_url(self):
        return reverse('portfolio:EmissionsSource_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Emissions Source"
        verbose_name_plural = "Emissions Sources"


class GPCEmissionsSource(models.Model):
    """
    The GPC Emission Source model holds aggregated emission data per source that conforms to the GPC reporting
    recommendations

    """

    # IDENTITY

    source_identifier = models.CharField(max_length=80, null=True,
                                         help_text='An internal identifier for the GHG emissions source')

    # LINKS

    gpc_subsector = models.ForeignKey('reference.GPCSector', blank=True, null=True, on_delete=models.CASCADE,
                                      help_text="GPC Emissions (sub)sector to which this source belongs")

    # CHARACTERISTICS

    notation_key = models.IntegerField(null=True, blank=True, choices=NOTATION_KEYS,
                                       help_text='GPC Notation Key (NO, IE, etc)')

    co2_amount = models.FloatField(null=True, blank=True, help_text='CO2 amount in tonnes')
    ch4_amount = models.FloatField(null=True, blank=True, help_text='CH4 amount in tonnes')
    n2o_amount = models.FloatField(null=True, blank=True, help_text='N2O amount in tonnes')
    hfc_amount = models.FloatField(null=True, blank=True, help_text='HFC amount in tonnes')
    pfc_amount = models.FloatField(null=True, blank=True, help_text='PFC amount in tonnes')
    sf6_amount = models.FloatField(null=True, blank=True, help_text='SF6 amount in tonnes')
    nf3_amount = models.FloatField(null=True, blank=True, help_text='NF3 amount in tonnes')
    tco2e_amount = models.FloatField(null=True, blank=True, help_text='Total CO2 equivalent amount in tonnes')
    co2b_amount = models.FloatField(null=True, blank=True, help_text='CO2 (b) amount in tonnes')

    AD_DQ = models.IntegerField(null=True, blank=True, choices=GPC_DQ_KEYS,
                                help_text='Activity Data Quality Key (L, M, H)')

    EF_DQ = models.IntegerField(null=True, blank=True, choices=GPC_DQ_KEYS,
                                help_text='Emission Factor Data Quality Key (L, M, H)')

    comments = models.TextField(null=True, blank=True,
                                help_text="Explanatory comments (i.e. description of methods or notation keys used)")
    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_identifier

    def get_absolute_url(self):
        return reverse('portfolio:GPCEmissionsSource_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "GPC Emissions Source"
        verbose_name_plural = "GPC Emissions Sources"


class BuildingEmissionsSource(models.Model):
    """
    The Building Emission Source model holds granular activity and emissions type data that characterize and quantify the emissions of a Building. A building is either a residential or commercial Asset.

    The implemented approach is the PCAF methodology for Mortgages


    """

    # IDENTITY

    source_identifier = models.CharField(max_length=80, null=True,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS

    asset = models.ForeignKey('portfolio.Building', blank=True, null=True, on_delete=models.CASCADE,
                              help_text="The Asset (Building) to which this emissions source belongs")

    emissions_factor = models.ForeignKey('reference.BuildingEmissionFactor', blank=True, null=True, on_delete=models.CASCADE, help_text="The Applicable Building Emissions Factor (From PCAF Database)")

    # CHARACTERISTICS

    emitted_gas = models.IntegerField(blank=True, null=True,
                                      choices=GHG_GAS_CHOICES,
                                      help_text='Type of GHG Emission. Choose CO2e if already aggregated')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_identifier

    def get_absolute_url(self):
        return reverse('portfolio:BuildingEmissionsSource_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Building Emissions Source"
        verbose_name_plural = "Building Emissions Sources"


class GPPEmissionsSource(models.Model):
    """
    The GPP Emission Source model holds aggregated emissions data per procurement contract

    """

    # IDENTITY

    source_identifier = models.CharField(max_length=80, null=True,
                                         help_text='An internal identifier for the GHG emissions source')

    # LINKS

    project = models.ForeignKey('portfolio.Project', blank=True, null=True, on_delete=models.CASCADE,
                                      help_text="Project to which this emissions source belongs")

    # CHARACTERISTICS

    # Kyoto Gases

    co2_amount = models.FloatField(null=True, blank=True, help_text='CO2 amount in tonnes')
    ch4_amount = models.FloatField(null=True, blank=True, help_text='CH4 amount in tonnes')
    n2o_amount = models.FloatField(null=True, blank=True, help_text='N2O amount in tonnes')
    hfc_amount = models.FloatField(null=True, blank=True, help_text='HFC amount in tonnes')
    pfc_amount = models.FloatField(null=True, blank=True, help_text='PFC amount in tonnes')
    sf6_amount = models.FloatField(null=True, blank=True, help_text='SF6 amount in tonnes')
    nf3_amount = models.FloatField(null=True, blank=True, help_text='NF3 amount in tonnes')
    tco2e_amount = models.FloatField(null=True, blank=True, help_text='Total CO2 equivalent amount in tonnes')
    co2b_amount = models.FloatField(null=True, blank=True, help_text='CO2 (b) amount in tonnes')


    comments = models.TextField(null=True, blank=True,
                                help_text="Explanatory comments (i.e. description of methods used)")
    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_identifier

    def get_absolute_url(self):
        return reverse('portfolio:GPPEmissionsSource_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "GPP Emissions Source"
        verbose_name_plural = "GPP Emissions Sources"

