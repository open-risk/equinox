# Copyright (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)
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

CPV_LEVEL_CHOICES = [(0, 'division'), (1, 'group'), (2, 'class'), (3, 'category'), (4, 'subcategory')]

CPV_LEVEL_DICT = {'division': 0, 'group': 1, 'class': 2, 'category': 3, 'subcategory': 4}


class CPVData(models.Model):
    """
    The CPVData model holds Common Procurement Vocabulary reference data about goods and services sectors used in
    Green Public Procurement


    """

    CPV_ID = models.CharField(max_length=20, blank=True, null=True,
                              help_text='The CPV Code (without the control digit)')

    description = models.CharField(max_length=200, blank=True, null=True,
                                   help_text='The Textual Description of the CPV Code')

    short_code = models.CharField(max_length=10, blank=True, null=True,
                                  help_text='The short version of the codeCode (without the trailing zeros and with the taxonomy split-out using dashes)')

    level = models.IntegerField(blank=True, null=True,
                                choices=CPV_LEVEL_CHOICES,
                                help_text='The taxonomy Level of the CPV Code')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.CPV_ID)

    def get_absolute_url(self):
        return reverse('reference:CPVData_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Common Procurement Vocabulary"
        verbose_name_plural = "Common Procurement Vocabulary"
