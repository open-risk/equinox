# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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

"""
Emissions Intensity (CO2 tonnes (1000 x kg) per mln (1000000 EUR) per CPV dimension

"""
intensity = {'09': 348.9,
             '76': 348.9,
             '14': 40.4,
             '15': 68.9,
             '18': 68.9,
             '19': 68.9,
             '22': 68.9,
             '24': 68.9,
             '30': 68.9,
             '38': 68.9,
             '31': 68.9,
             '32': 68.9,
             '33': 68.9,
             '34': 68.9,
             '44': 68.9,
             '35': 68.9,
             '37': 68.9,
             '16': 68.9,
             '42': 68.9,
             '43': 68.9,
             '39': 68.9,
             '50': 68.9,
             '41': 117.9,
             '90': 117.9,
             '45': 168.2,
             '55': 321.1,
             '60': 136.6,
             '64': 136.6,
             '72': 30.3,
             '48': 30.3,
             '70': 184.1,
             '79': 20.3,
             '71': 20.3,
             '73': 20.3,
             '63': 20.3}


class ReferenceIntensity(models.Model):
    """
    The Reference Emissions Intensity model holds reference emission intensities for comparison purposes.

    Usage: Internal (Portfolio). Intensities can be juxtaposed with these external / macro benchmarks


    """

    Sector = models.CharField(max_length=80, blank=True, null=True, help_text='Standard Description')

    Gases = models.CharField(max_length=80, blank=True, null=True, help_text='Standard Description')

    Fuel = models.CharField(max_length=80, blank=True, null=True, help_text='Standard Description')

    Description = models.TextField(blank=True, null=True, help_text='Standard Description')

    Region = models.CharField(max_length=80, blank=True, null=True, help_text='Standard Description')

    Value = models.CharField(max_length=20, blank=True, null=True, help_text='Standard Description')

    Unit = models.CharField(max_length=20, blank=True, null=True, help_text='Standard Description')

    Data_Source = models.CharField(max_length=80, blank=True, null=True, help_text='Standard Description')

    Lower_Bound = models.CharField(max_length=20, blank=True, null=True, help_text='Standard Description')

    Upper_Bound = models.CharField(max_length=20, blank=True, null=True, help_text='Standard Description')

    Data_Quality = models.CharField(max_length=80, blank=True, null=True, help_text='Standard Description')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('reference:ReferenceIntensity_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Reference Intensity"
        verbose_name_plural = "Reference Intensities"
