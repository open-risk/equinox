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
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

from portfolio.ProjectActivity import ProjectActivity


class ActivityBarrier(models.Model):
    """
    The Activity Barrier model holds data for barriers to Project Activities


    """

    # IDENTIFICATION

    barrier_identifier = models.CharField(max_length=80, blank=True, null=True, help_text='A unique identification of a Barrier')

    barrier_description = MarkdownField(default='', rendered_field='text_rendered',
                                                 validator=VALIDATOR_STANDARD,
                                                 help_text='Textual description of an Activity Barrier. Markdown format is supported <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/">Documentation</a>')

    # ATTN cannot be null
    text_rendered = RenderedMarkdownField()

    # LINKS
    project_activity = models.ForeignKey(ProjectActivity, blank=True, null=True, on_delete=models.CASCADE, help_text="The Project Activity to which this Primary Effect belongs")


    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.barrier_identifier

    def get_absolute_url(self):
        return reverse('risk:ActivityBarrier_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Activity Barrier"
        verbose_name_plural = "Activity Barrier"
