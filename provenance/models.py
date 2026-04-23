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

# Partial implementation of PROV following
# https://github.com/kristinriebe/django-prov_vo/blob/master/prov_vo/models.py

AGENT_TYPE_CHOICES = (
    ('voprov:Organization', 'voprov:Organization'),
    ('voprov:Individual', 'voprov:Individual'),
)

ACTIVITY_TYPE_CHOICES = (
    ('obs:Observation', 'obs:Observation'),
    ('obs:Reduction', 'obs:Reduction'),
    ('obs:Classification', 'obs:Classification'),
    ('obs:Crossmatch', 'obs:Crossmatch'),
    ('calc:ChemicalPipeline', 'calc:ChemicalPipeline'),
    ('calc:Distances', 'calc:Distances'),
    ('other', 'other'),
)


class Agent(models.Model):
    name = models.CharField(max_length=128, null=True)  # human readable label, firstname + lastname
    type = models.CharField(max_length=128, null=True,
                            choices=AGENT_TYPE_CHOICES)  # types of entities: single entity, dataset
    email = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    url = models.URLField(null=True, blank=True, help_text="URL of Provenance Agent")

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('admin:provenance_agent_change', args=[self.pk])

    class Meta:
        verbose_name = "PROV Agent"
        verbose_name_plural = "PROV Agents"
