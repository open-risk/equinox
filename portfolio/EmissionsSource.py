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

from django.db import models
from portfolio.model_choices import *
from django.urls import reverse

# The IPCC Gases
GHG_GAS_CHOICES = [(0, 'CO2e'),
                   (1, 'CO2'),
                   (1, 'CH4'),
                   (1, 'N2O'),
                   (1, 'SF6'),
                   (1, 'CF4'),
                   (1, 'C2F6'),
                   (1, 'NF3'),
                   (1, 'CHF3'),
                   (1, 'CH2F2'),
                   (1, 'CH3F'),
                   (1, 'C2HF5'),
                   (1, 'C2H2F4'),
                   (1, 'CH2FCF3'),
                   (1, 'C2H3F3'),
                   (1, 'C2H4F3'),
                   (1, 'C2H4F2'),
                   (1, 'C3HF7'),
                   (1, 'C3H2F6'),
                   (1, 'C3H3F5')]


class EmissionsSource(models.Model):
    """
    The Emission Source model holds activity and emissions type data that characterize and quantify the emissions of an Asset.


    """

    # IDENTITY

    source_identifier = models.CharField(max_length=80, null=True,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS

    asset = models.ForeignKey('Asset', blank=True, null=True, on_delete=models.CASCADE,
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
