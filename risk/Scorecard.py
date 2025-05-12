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
from django.urls import reverse

from portfolio.ProjectCompany import ProjectCompany


class Scorecard(models.Model):
    """
    The Scorecard data model holds data for defined scorecards. The current implementation is a Credit Scorecard of the ProjectCompany

    """

    scorecard_identifier = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Identification of a specific scorecard data container<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Scorecard">Documentation</a>')

    scorecard_data = models.JSONField(blank=True, null=True,
                                      help_text='Scorecard data as key/value pairs of characteristics / attributes <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Characteristic">Documentation</a>')

    # LINKS

    project_company = models.ForeignKey(ProjectCompany, blank=True, null=True, on_delete=models.CASCADE,
                                        help_text="The Project Company who's score is being computed")

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.scorecard_identifier

    def get_absolute_url(self):
        return reverse('risk:Scorecard_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Scorecard"
        verbose_name_plural = "Scorecards"
