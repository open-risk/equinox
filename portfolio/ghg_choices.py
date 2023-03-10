# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software'), to deal
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

PRIMARY_GHG_EFFECTS = [(0, 'Reduction in combustion emissions from generating grid-connected electricity'),
                       (1,
                        'Reduction in combustion emissions from generating energy or off-grid electricity, or from flaring'),
                       (2,
                        'Reductions in industrial process emissions from a change in industrial activities or management practices'),
                       (3, 'Reductions in fugitive emissions'),
                       (4, 'Reductions in waste emissions'),
                       (5, 'Increased storage or removals of CO2 by biological processes')]

SECONDARY_GHG_EFFECTS = [(0,
                          'One-Time Effect: Changes in GHG emissions associated with the construction, installation, and establishment or the decommissioning and termination of the project activity'),
                         (1,
                          'Recurring Upstream Effect: Recurring changes in GHG emissions associated with inputs to the project activity, relative to baseline emissions'),
                         (2,
                          'Recurring Downstream Effect: Recurring changes in GHG emissions associated with outputs of the project activity, relative to baseline emissions'),
                         (3, 'Noted but not considered')]

BASELINE_ESTIMATION_PROCEDURE = [(0, 'Project-Specific Procedure'),
                                 (1, 'Performance Standard Procedure')]

# The PCAF DQ Scoring Scheme
GHG_DATA_QUALITY_CHOICES = [(1, '(a) Score 1'),
                            (2, '(b) Score 2'),
                            (3, '(c) Score 3'),
                            (4, '(d) Score 4'),
                            (5, '(e) Score 5')]
