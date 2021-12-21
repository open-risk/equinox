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
from django.urls import reverse


class EmissionFactor(models.Model):
    """
    The Emissions Factor model holds IPCC reference data about activity emission factors


    """

    EF_ID = models.IntegerField(blank=True, null=True,
                                help_text='Standard Description')

    IPCC_Category = models.CharField(max_length=80, blank=True, null=True,
                                     help_text='Standard Description')

    Gases = models.CharField(max_length=80, blank=True, null=True,
                             help_text='Standard Description')

    Fuel = models.CharField(max_length=80, blank=True, null=True,
                            help_text='Standard Description')

    Parameter_Type = models.CharField(max_length=80, blank=True, null=True,
                                      help_text='Standard Description')

    Description = models.TextField(blank=True, null=True,
                                   help_text='Standard Description')

    Technology_Practices = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Standard Description')

    Parameter_Conditions = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Standard Description')

    Regional_Conditions = models.CharField(max_length=80, blank=True, null=True,
                                           help_text='Standard Description')

    Control_Technologies = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Standard Description')

    Other_Properties = models.CharField(max_length=80, blank=True, null=True,
                                        help_text='Standard Description')

    Value = models.CharField(max_length=20, blank=True, null=True,
                                help_text='Standard Description')

    Unit = models.CharField(max_length=20, blank=True, null=True,
                            help_text='Standard Description')

    Equation = models.CharField(max_length=80, blank=True, null=True,
                               help_text='Standard Description')

    IPCC_Worksheet = models.CharField(max_length=80, blank=True, null=True,
                                      help_text='Standard Description')

    Data_Source = models.CharField(max_length=80, blank=True, null=True,
                                   help_text='Standard Description')

    Technical_Reference = models.CharField(max_length=80, blank=True, null=True,
                                           help_text='Standard Description')

    English_Abstract = models.CharField(max_length=80, blank=True, null=True,
                                        help_text='Standard Description')

    Lower_Bound = models.CharField(max_length=20, blank=True, null=True,
                                      help_text='Standard Description')

    Upper_Bound = models.CharField(max_length=20, blank=True, null=True,
                                      help_text='Standard Description')

    Data_Quality = models.CharField(max_length=80, blank=True, null=True,
                                    help_text='Standard Description')

    Data_Quality_Reference = models.CharField(max_length=80, blank=True, null=True,
                                              help_text='Standard Description')

    Other_Data_Quality = models.CharField(max_length=80, blank=True, null=True,
                                          help_text='Standard Description')

    Data_Provider_Comments = models.CharField(max_length=80, blank=True, null=True,
                                              help_text='Standard Description')

    Other_Comments = models.CharField(max_length=80, blank=True, null=True,
                                      help_text='Standard Description')

    Data_Provider = models.CharField(max_length=80, blank=True, null=True,
                                     help_text='Standard Description')

    Link = models.URLField(blank=True, null=True,
                           help_text='Standard Description')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.EF_ID)

    def get_absolute_url(self):
        return reverse('reference:EmissionFactor_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Emissions Factor"
        verbose_name_plural = "Emissions Factors"
