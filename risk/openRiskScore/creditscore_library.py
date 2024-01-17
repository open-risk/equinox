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


import numpy as np
import requests


def get_all_data(data_url):
    s = requests.Session()
    page = 1
    response = s.get(data_url)
    dataList = []
    resp_json = response.json()
    dataList.append(resp_json["_items"])
    # print("LINKS", resp_json["_links"]["next"])
    # print("ITEMS", resp_json["_items"])
    while resp_json["_links"].has_key("next"):
        page += 1
        new_url = data_url + "?page=" + str(page)
        response = s.get(new_url)
        resp_json = response.json()
        # print("LINKS", resp_json["_links"])
        dataList.append(resp_json["_items"])
    # print("TOTAL ->", dataList)
    return dataList


# the concentration index collection (ADD OTHER functions)
def calculate_sme_z_score(portfolio_url, model_inputs):
    # Step 1: Get portfolio data (client attributes)

    client_data_raw = get_all_data(portfolio_url)
    # print("TOTAL -> ", client_data_raw)

    id = []
    v1 = []
    v2 = []
    v3 = []
    v4 = []
    v5 = []
    v6 = []
    v7 = []

    # iterate over all obligor attribute vectors

    # for entry in client_data_raw['_items']:
    for dlist in client_data_raw:
        for entry in dlist:
            id.append(entry['client_id'])
            v1.append(entry['Ebitda'])
            v2.append(entry['Total_Assets'])
            v3.append(entry['Short_Term_Debt'])
            v4.append(entry['Equity_Book_Value'])
            v5.append(entry['Retained_Earnings'])
            v6.append(entry['Cash'])
            v7.append(entry['Interest_Expenses'])

    v1s = np.array(v1)
    v2s = np.array(v2)
    v3s = np.array(v3)
    v4s = np.array(v4)
    v5s = np.array(v5)
    v6s = np.array(v6)
    v7s = np.array(v7)

    r1 = np.true_divide(v1s, v2s)
    r2 = np.true_divide(v3s, v4s)
    r3 = np.true_divide(v5s, v2s)
    r4 = np.true_divide(v6s, v2s)
    r5 = np.true_divide(v1s, v7s)
    r0 = np.ones_like(r1)

    w = model_inputs['weights']

    # calculate z-score as linear combination

    x = np.multiply(r1, w[1]) \
        + np.multiply(r2, w[2]) \
        + np.multiply(r3, w[3]) \
        + np.multiply(r4, w[4]) \
        + np.multiply(r5, w[5]) \
        + np.multiply(r0, w[0])

    # calculate probability of default

    t1 = np.exp(x)
    t2 = np.ones_like(x) + t1
    p = 1 - np.true_divide(t1, t2)

    # print('result', p)
    return {"result": p.tolist()}
