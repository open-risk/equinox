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


class ORMKeyword(models.Model):
    default_url = "https://www.openriskmanual.org/wiki"
    keyword = models.CharField(max_length=400, help_text="The managed keyword")
    slug = models.CharField(max_length=400, help_text="Representation of keyword on documentation website URL",
                            null=True, blank=True)
    link = models.URLField(default=default_url, help_text="The Wiki serving keyword definitions")
    tooltip = models.TextField(blank=True, null=True, help_text="Optional storage of tooltip sentence (Definition)")

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = "Risk Manual Keyword"
        verbose_name_plural = "Risk Manual Keywords"


class DocPage(models.Model):
    slug = models.CharField(max_length=400, help_text="Representation of keyword on website URL", null=True, blank=True)
    title = models.CharField(max_length=400, help_text="Page Title", null=True, blank=True)
    tooltip_message = models.TextField(null=True, blank=True, help_text="Help-box message")
    content = models.TextField(null=True, blank=True, help_text="The html content of the documentation page")

    DOC_TYPE = [(0, 'html'), (1, 'markdown')]
    doc_type = models.IntegerField(default=0, choices=DOC_TYPE, help_text="Type of markup used in doc page")

    CATEGORY_CHOICES = [(0, 'General'),
                        (1, 'Clients'),
                        (2, 'Portfolios'),
                        (3, 'Liabilities'),
                        (4, 'Economic Data'),
                        (5, 'Historical Credit Data'),
                        (6, 'Products'),
                        (7, 'Scenarios'),
                        (8, 'Models'),
                        (9, 'Workflows'),
                        (10, 'Objectives'),
                        (11, 'Technical')]

    category = models.IntegerField(default=0, choices=CATEGORY_CHOICES,
                                   help_text="Category to which documentation page belongs")

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('start:Documentation', kwargs={'slug': self.slug})

    # Bookkeeping fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Documentation Page"
        verbose_name_plural = "Documentation Pages"
