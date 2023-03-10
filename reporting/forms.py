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

from reporting.models import Visualization
from django import forms
from django.forms import ModelForm

from portfolio.Portfolios import ProjectPortfolio

aggregation_choices = [(0, 'Avg'), (1, 'Count'), (2, 'Max'), (3, 'Min'), (4, 'Sum'), (5, 'StdDev'), (6, 'Variance')]

portfolio_attributes = [(0, 'EAD'), (1, 'LGD'), (2, 'Rating'), (3, 'Stage'),
                        (4, 'Tenor'), (5, 'Sector'), (6, 'Country')]


class CustomPortfolioAggregatesForm(forms.Form):
    aggregator_function = forms.ChoiceField(label="The Aggregation Function to Apply", choices=aggregation_choices)
    attribute = forms.ChoiceField(label='Field to Aggregate', choices=portfolio_attributes)


class VisualizationInteractiveForm(ModelForm):
    class Meta:
        model = Visualization
        fields = ['name']
