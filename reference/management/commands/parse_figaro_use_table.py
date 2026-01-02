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

# load use table in both flat file and matrix format
import pandas as pd
import numpy as np

u_fla = pd.read_csv('../data/flatfile_eu-ic-use_24ed_2022.csv')
u_mat = pd.read_csv('../data/matrix_eu-ic-use_24ed_2022.csv')

# icuseCol_mat = u_mat.columns.tolist()[1:]
# icuseRow_mat = u_mat['rowLabels'].to_list()
# icuseRow_fla = u_fla['icuseRow'].to_list()
# icuseCol_fla = u_fla['icuseCol'].to_list()
# print(len(icuseCol_fla))
# print(len(icuseRow_fla))

u_mat = u_mat.drop('rowLabels', axis=1)
mat = u_mat.to_numpy()
# print(mat)

ROWS = 2950
COLS = 3174
index = 0
fla = np.empty(shape=(ROWS, COLS))
for row in u_fla.itertuples(index=False):
    value = row[6]
    row_label = row[0]
    col_label = row[1]
    col_index = index % COLS
    row_index = int(index / COLS)
    fla[row_index, col_index] = value
    index += 1
    # print(index, row_label, row_index, col_label, col_index, value)

# print(fla)

# error_count = 0
# for i in range(MAX):
#     for j in range(MAX):
#         if mat[i, j] != fla[i, j]:
#             print(icsupRow_mat[i], icsupCol_mat[j], mat[i, j])
#             print(s_fla.iloc[i * MAX + j, s_fla.columns.get_loc('icsupRow')], s_fla.iloc[i * MAX + j, s_fla.columns.get_loc('icsupCol')], s_fla.iloc[i * MAX + j, s_fla.columns.get_loc('obsValue')], fla[i, j])
#             print(80*'=')
#             error_count += 1
#
# print(error_count)
