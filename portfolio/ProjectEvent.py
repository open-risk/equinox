# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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

EVENT_CHOICES = [(0, 'Initiated'),
                 (1, 'Public'),
                 (2, 'Live'),
                 (3, 'Modified'),
                 (4, 'Closed')]


class ProjectEvent(models.Model):
    """
    The Project Life Cycle model holds event data that document the status (stage) in the life cycle of a Project.

    The model acts as a container for the historical progression of a project from initiation to completion

    A Project will have at least one Project Life Cycle event (project initiation or equivalent)


    """
    # IDENTIFICATION

    project_event_identifier = models.CharField(max_length=80, blank=True, null=True,
                                                help_text='A unique identification (e.g. documentation serial) of a Project Lifecycle Event for internal or external use')

    # LINKS

    project = models.ForeignKey('Project', blank=True, null=True, on_delete=models.CASCADE,
                                help_text="The Project to which this Activity belongs")

    # PROJECT ACTIVITY DATA

    project_event_type = models.IntegerField(blank=True, null=True, choices=EVENT_CHOICES,
                                             help_text='The project event type')

    project_event_date = models.DateTimeField(blank=True, null=True, help_text='The Lifecycle Event date')

    project_event_description = models.CharField(max_length=200, blank=True, null=True,
                                                 help_text='Optional Event Description')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_event_identifier

    def get_absolute_url(self):
        return reverse('portfolio:ProjectEvent_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Project Event"
        verbose_name_plural = "Project Events"
