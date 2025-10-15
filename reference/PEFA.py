# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
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

PEFA_CHOICES = [(0, 'Supply'), (1, 'Use')]


class PEFASUT(models.Model):
    """
    PEFA Supply and Use Tables

    """

    year = models.PositiveIntegerField(null=True, blank=True, help_text="Reference Year")
    industry = models.CharField(max_length=10, null=True, blank=True, help_text="Industry (NACE R2)")
    product = models.CharField(max_length=10, null=True, blank=True, help_text="Energy Product")
    region = models.CharField(max_length=10, null=True, blank=True, help_text="Geographical Region")
    value = models.FloatField(null=True, blank=True, help_text="Measurement Value (TJoules)")
    role = models.IntegerField(blank=True, null=True,
                               choices=PEFA_CHOICES,
                               help_text='Type of SUT Table')

    created_at = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pefa_sut"
        unique_together = (("role", "industry", "product", "region", "year"),)
        indexes = [
            Index(fields=['role', 'industry', 'product', 'region', 'year'], name='pefa_all_idx'),
            Index(fields=['role', 'region', 'year'], name='pefa_region_idx'),
        ]
        verbose_name = "PEFA SUT Data"
        verbose_name_plural = "PEFA SUT Data"

    def get_absolute_url(self):
        return reverse('reference:PEFASUT_edit', kwargs={'pk': self.pk})
