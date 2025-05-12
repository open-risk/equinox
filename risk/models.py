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

"""
The main Risk models are defined in individual files for readability
Use models.py for any additional / auxiliary models


"""

# Reporting modes is a dictionary storing the description of risk reports
# and compatibility with different model methods

ReportingModeName = {
    0: 'No Reporting',
    1: 'Scenario Average Rating Distribution',
    2: 'Full Rating Distribution',
    3: 'Simulated vs Analytic Results',
    4: 'Distribution Moments',
    5: 'Single Period Histogram',
    6: 'Multi Period Histogram',
    7: 'Single Scenario',
    8: 'Stage Results',
    9: 'Exposure Rating Distribution',
    10: 'Stage Migration',
    11: 'Entity Rating',
    12: 'WAM',
    13: 'Distribution Risk Horizon',
    14: 'Moments Risk Horizon',
    15: 'Empty',
    16: 'Enumerated Scenario',
    17: 'Entity Default Rate Distribution',
    18: 'Simulated Metrics',
    19: 'Conditional Transitions',
    20: 'Expectations at Risk horizon',
    21: 'Analytic Metrics',
    22: 'Distribution Risk Horizon',
    23: 'Stage Exposure at Risk Horizon',
    24: 'Macro Scenario Distribution',
    25: 'Macro Scenario Statistics',
    26: 'Macro Scenario Snapshot',
    27: 'GeoSlice'
}

ReportingModeDescription = {
    0: 'No Reporting. Useful for debugging purposes',
    1: 'Scenario Average number of names in given rating, per period',
    2: 'Multiperiod Matrices with DefaultGrid distributions',
    3: 'Multiperiod Metrics',
    4: 'Multiperiod Metrics',
    5: 'Single Period Histogram',
    6: 'Multiperiod Matrices with DefaultGrid distributions',
    7: 'Single Scenario Metrics',
    8: 'Multiperiod Metrics Graph (over Scenarios)',
    9: 'Multiperiod Matrices with DefaultGrid distributions',
    10: 'Stage Migration Aggregate Statistics (Scenario Averages)',
    11: 'Multiperiod Matrices with DefaultGrid distributions',
    12: 'Multiperiod Metrics Graph (over Scenarios)',
    13: 'Scenario Metrics (At Risk Horizon)',
    14: 'Moments of Emissions (At Risk Horizon)',
    15: 'Empty',
    16: 'Probability Weighted Scenario GHG',
    17: 'Distribution of entity GHG',
    18: 'Simulated GHG per period',
    19: 'Conditional Transition Rates from-to-period',
    20: 'Expected Statistics at horizon',
    21: 'Analytic statistics per period',
    22: 'Histogram of PnL at risk horizon',
    23: 'Scenario Metrics (At Risk Horizon)',
    24: 'The distributions of macro factor variables',
    25: 'Summary statistics of macro factor variables',
    26: 'The realizations of macro factors (scenarios)',
    27: 'GeoSlice'
}

ModelModes = {
    0: 'DryRun Mode / Testing setup',
    1: 'Analytic Calculation',
    2: 'Simulated Scenarios Including Uncertainty',
    3: 'Enumerated Scenario'
}

ModelModesShort = {
    0: 'DryRun',
    1: 'Analytic',
    2: 'Simulated',
    3: 'Enumerated'
}

ReportingModeMatch = {
    0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    1: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    2: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    3: [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    4: [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    5: [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    6: [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    7: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    8: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    9: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    10: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    11: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    12: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    13: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    14: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    15: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    16: [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    17: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    18: [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    19: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    20: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    21: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    22: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    23: [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    24: [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    25: [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    26: [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    27: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
