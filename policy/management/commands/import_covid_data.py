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

import pandas as pd

pdata = pd.read_csv("OxCGRT_latest.csv")

# get column names
print(list(pdata.columns.values))

# print(pdata.head(5))

# # transform alpha-3 to alpha-2
# for index, row in pdata.iterrows():
#     cc = row['CountryCode']
#     print(cc, countryISOMapping[cc])

cols = ['CountryName', 'CountryCode',
        'Date',
        'C1_School closing', 'C1_Flag',
        'C2_Workplace closing', 'C2_Flag',
        'C3_Cancel public events', 'C3_Flag',
        'C4_Restrictions on gatherings', 'C4_Flag',
        'C5_Close public transport', 'C5_Flag',
        'C6_Stay at home requirements', 'C6_Flag',
        'C7_Restrictions on internal movement', 'C7_Flag',
        'C8_International travel controls',
        'E1_Income support', 'E1_Flag',
        'E2_Debt/contract relief',
        'E3_Fiscal measures',
        'E4_International support',
        'H1_Public information campaigns', 'H1_Flag',
        'H2_Testing policy',
        'H3_Contact tracing',
        'H4_Emergency investment in healthcare',
        'H5_Investment in vaccines',
        'M1_Wildcard',
        'ConfirmedCases',
        'ConfirmedDeaths',
        'StringencyIndex', 'StringencyIndexForDisplay',
        'StringencyLegacyIndex', 'StringencyLegacyIndexForDisplay',
        'GovernmentResponseIndex', 'GovernmentResponseIndexForDisplay',
        'ContainmentHealthIndex', 'ContainmentHealthIndexForDisplay',
        'EconomicSupportIndex', 'EconomicSupportIndexForDisplay']
