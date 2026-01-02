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


"""

 head -1 policy/fixtures/policy_data/OECD.ENV.EPI\,DSD_CAPMF@DF_CAPMF\,1.0+all.csv

"""

# The CAPMF policy field names as they are in the CSV header

field_names = ['Policy Stringency', 'Policy Count']

# Field codes as constructed from the CSV headers

field_codes = ['POL_STRINGENCY',
               'POL_COUNT'
               ]

# field description (from CSV headers)
field_description = ['Policy Stringency',
                     'Policy Count'
                     ]

field_description_long = field_description

# from codebook

# code list

field_code_list = {'POL_STRINGENCY': {'0': 'no measures',
                                      '1': 'recommend closing',
                                      '2': 'require closing',
                                      '3': 'require closing all levels'},
                   'POL_COUNT': {'0': 'no measures',
                                 '1': 'general'}
                   }

field_type = ['numerical', 'numerical']
