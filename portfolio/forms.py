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

from django import forms
from django.forms import ModelForm

from portfolio.Portfolios import ProjectPortfolio


class CreatePortfolioForm(ModelForm):
    size = forms.IntegerField(label='Portfolio Size (N)')

    class Meta:
        model = ProjectPortfolio
        exclude = ('last_change_date', 'creation_date')


class ClonePortfolioForm(forms.Form):
    name = forms.CharField(label='Portfolio Name', max_length=100)


class AssemblePortfolioForm(forms.Form):
    name = forms.CharField(label='Portfolio Name', max_length=100)
    size = forms.IntegerField(label='Portfolio Size')


class ImportPortfolioForm(forms.Form):
    name = forms.CharField(label='Portfolio Name', max_length=100)
    file = forms.FileField(label='Select a file', help_text='max. 42 megabytes', widget=forms.FileInput)
