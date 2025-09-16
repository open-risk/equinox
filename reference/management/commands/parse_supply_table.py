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

# load supply table in both flat file and matrix format
import pandas as pd
import numpy as np

s_fla = pd.read_csv('../data/flatfile_eu-ic-supply_24ed_2022.csv')
s_mat = pd.read_csv('../data/matrix_eu-ic-supply_24ed_2022.csv')

icsupCol_mat = s_mat.columns.tolist()[1:]
icsupRow_mat = s_mat['rowLabels'].to_list()

# icsupRow_fla = s_fla['icsupRow'].to_list()
# icsupCol_fla = s_fla['icsupCol'].to_list()
# print(len(icsupCol_fla))
# print(len(icsupRow_fla))

s_mat = s_mat.drop('rowLabels', axis=1)
mat = s_mat.to_numpy()

MAX = 2944
index = 0
fla = np.empty(shape=(MAX, MAX))
for row in s_fla.itertuples(index=False):
    value = row[6]
    col_index = index % MAX
    row_index = int(index / MAX)
    fla[row_index, col_index] = value
    index += 1

error_count = 0
for i in range(MAX):
    for j in range(MAX):
        if mat[i, j] != fla[i, j]:
            print(icsupRow_mat[i], icsupCol_mat[j], mat[i, j])
            print(s_fla.iloc[i * MAX + j, s_fla.columns.get_loc('icsupRow')], s_fla.iloc[i * MAX + j, s_fla.columns.get_loc('icsupCol')], s_fla.iloc[i * MAX + j, s_fla.columns.get_loc('obsValue')], fla[i, j])
            print(80*'=')
            error_count += 1

print(error_count)
