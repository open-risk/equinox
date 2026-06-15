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
from django.db.models import Index
from django.urls import reverse

GRID_MIX_CHOICES = [(0, 'Production'), (1, 'Supplier'), (2, 'Residual')]


class AIBMix(models.Model):
    """
    European Grid Energy Mixes from the Association of Issuing Bodies

    """

    year = models.PositiveIntegerField(null=True, blank=True, help_text="Reference Year",
                                       verbose_name='Measurement Year')
    country = models.CharField(max_length=10, null=True, blank=True, help_text="Geographical Region Code",
                               verbose_name='Region')
    grid_mix_value = models.FloatField(null=True, blank=True, help_text="Measurement Value", verbose_name='Value')
    grid_mix_type = models.IntegerField(null=True, blank=True, choices=GRID_MIX_CHOICES, help_text="Grid Mix Type",
                                        verbose_name='Type')

    created_at = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "AIB Grid Mix Data"
        verbose_name_plural = "AIB Grid Mix Data"

    def get_absolute_url(self):
        return reverse('admin:reference_aibmix_change', args=[self.pk])
