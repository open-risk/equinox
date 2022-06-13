# encoding: utf-8

# (c) 2017-2021 Open Risk, all rights reserved
#
# ConcentrationMetrics is licensed under the MIT license a copy of which is included
# in the source distribution of TransitionMatrix. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.


""" ConcentrationMetrics

.. moduleauthor: Open Risk

"""

import numpy as np
import pandas as pd
import os

# ADJUST THIS TO REFLECT YOUR OWN ENVIRONMENT!
# Set the full path including trailing slash
package_name = 'transitionMatrix'
module_path = os.path.dirname(__file__)
source_path = module_path
dataset_path = source_path + "/datasets/"


class Index(object):
    """  The concentration index object provides the main interface to the various index calculation


    """

    def __init__(self):
        pass

    # call index by name
    def callMethod(self, name, data, *args):
        return getattr(self, name)(data, *args)

    # calculate total size
    def total_size(self, data):
        return np.sum(data)

    def get_weights(self, data):
        """ Calculate data weights

        :param data: Positive data of weights
        :type data: numpy array
        :return: Vector weights
        :raise: TypeError if negative total size
        """

        try:
            # select the first column only
            if len(data.shape) > 1:
                data = data[:, 0]
            # print(data)
        except:
            print("Data is not in numpy format")
            exit()

        ts = self.total_size(data)
        if ts <= 0:
            raise TypeError('Input data vector must have positive values')
            exit()
        else:
            return np.true_divide(data, ts)

    def cr(self, data, n):
        """ Calculate the Concentration Ratio

        :param data: Positive data
        :type data: numpy array
        :param n: Integer selecting the top-n entries
        :type n: int
        :return: Concentration Ratio (Float)
        :raise: TypeError if n out of range

        `Open Risk Manual Entry for Concentration Ratio <https://www.openriskmanual.org/wiki/Concentration_Ratio>`_
        """
        if n < 0 or n > data.size:
            raise TypeError('n must be an positive integer smaller than the data size')
        else:
            data = np.array(sorted(data, reverse=True))
            weights = self.get_weights(data)
            return weights[:n].sum()

    def berger_parker(self, data):
        """ Calculate the Berger Parker Index (special version of the Concentration Ratio)

        :param data: Positive data
        :type data: numpy array
        :return: Berger Parker (Float)

        `Open Risk Manual Entry for Berger-Parker Index <https://www.openriskmanual.org/wiki/Concentration_Ratio>`_
        """
        return self.cr(data, 1)

    def hhi(self, data, normalized=True, ci=None, samples=None):
        """ Calculate the Herfindahl-Hirschman index

        :param data: Positive data
        :type data: numpy array
        :return: HHI (Float)

        `Open Risk Manual Entry for Hirschman-Herfindahl Index <https://www.openriskmanual.org/wiki/Herfindahl-Hirschman_Index>`_
        """
        # Normalize the data
        weights = self.get_weights(data)
        n = weights.size
        # Compute the HHI
        if n == 0:
            return 0
        else:
            h = np.square(weights).sum()
            if normalized:
                return (h - 1.0 / n) / (1.0 - 1.0 / n)
            else:
                return h

    def hk(self, data, a):
        """ Calculate the inverted Hannah Kay index

        :param data: Positive data
        :type data: numpy array
        :param a: Integer index parameter alpha
        :return: HK (Float)

        `Open Risk Manual Entry for Hannah Kay Index <https://www.openriskmanual.org/wiki/Hannah_Kay_Index>`_
        """
        weights = self.get_weights(data)
        n = weights.size
        if n == 0:
            return 0
        else:
            if a <= 0:
                raise TypeError('Alpha must be strictly positive')
            elif a == 1:
                weights_nz = weights[weights != 0]
                log_weights = np.log(weights_nz)
                h = np.multiply(weights_nz, log_weights).sum()
                return np.exp(h)
            else:
                h1 = np.power(weights, a).sum()
                h2 = np.power(h1, 1.0 / (a - 1.0))
                return h2

    def hoover(self, data):
        """ Calculate the Hoover index

        :param data: Positive data
        :type data: numpy array
        :return: Hoover (Float)

        `Open Risk Manual Entry for Hoover Index <https://www.openriskmanual.org/wiki/Hoover_Index>`_
        """

        weights = self.get_weights(data)
        n = weights.size
        if n == 0:
            return 0
        else:
            return 0.5 * np.absolute(weights - 1.0 / n).sum()

    def gini(self, data):
        """ Calculate the Gini index

        :param data: Positive data
        :type data: numpy array
        :return: Gini (Float)

        .. note:: The formula appears also with the opposite sign convention

        `Open Risk Manual Entry for Gini Index <https://www.openriskmanual.org/wiki/Gini_Index>`_
        """
        data = np.array(sorted(data, reverse=True))
        weights = self.get_weights(data)
        n = weights.size
        if n == 0:
            return 0
        else:
            i = np.arange(1, n + 1)
            return 1.0 + (1.0 - 2.0 * np.multiply(i, weights).sum()) / n

    def shannon(self, data, normalized=True):
        """ Calculate the Shannon entropy index

        :param data: Positive data
        :type data: numpy array
        :return: Shannon entropy (Float)

        `Open Risk Manual Entry for Shannon Entropy Index <https://www.openriskmanual.org/wiki/Shannon_Index>`_
        """
        weights = self.get_weights(data)
        # remove zero weights
        weights_nz = weights[weights != 0]
        n = weights_nz.size
        if n == 0:
            return 0
        else:
            log_weights = np.log(weights_nz)
            h = - np.multiply(weights_nz, log_weights).sum()
            if normalized:
                return 1.0 - h / np.log(n)
            else:
                return h

    def atkinson(self, data, epsilon):
        """ Calculate the Atkinson inequality index

        :param data: Positive data
        :type data: numpy array
        :param epsilon: Index parameter
        :type epsilon: float
        :return: Atkinson inequality (Float)

        .. Todo :: Resolve divide by zero when N is very large

        `Open Risk Manual Entry for Atkinson Index <https://www.openriskmanual.org/wiki/Atkinson_Index>`_
        """
        weights = self.get_weights(data)
        n = weights.size
        if n == 0:
            return 0
        else:
            if epsilon <= 0:
                raise TypeError('Epsilon must be strictly positive (>0.0)')
            elif epsilon == 1:
                weights_nz = weights[weights != 0]
                n = weights_nz.size
                log_weights = np.log(weights_nz)
                h = log_weights.sum() / n
                return 1 - n * np.exp(h)
            else:
                n2 = np.power(n, epsilon / (epsilon - 1.0))
                h1 = np.power(weights, 1.0 - epsilon).sum()
                h2 = np.power(h1, 1.0 / (1.0 - epsilon))
                return 1 - n2 * h2

    def gei(self, data, alpha):
        """ Calculate the Generalized Entropy Index

        :param data: Positive data
        :type data: numpy array
        :param alpha: Index parameter
        :return: Generalized Entropy Index (Float)

        `Open Risk Manual Entry for Generalized Entropy Index <https://www.openriskmanual.org/wiki/Generalized_Entropy_Index>`_
        """
        weights = self.get_weights(data)
        n = weights.size
        if n == 0:
            return 0
        else:
            if alpha == 0:
                weights_nz = weights[weights != 0]
                n = weights_nz.size
                log_weights = np.log(weights_nz)
                h = log_weights.sum() / n
                index = - (np.log(n) + h)
            elif alpha == 1:
                weights_nz = weights[weights != 0]
                n = weights_nz.size
                log_weights = np.log(weights_nz)
                h = np.multiply(weights_nz, log_weights).sum()
                index = np.log(n) + h
            else:
                n2 = np.power(n, alpha)
                h1 = n2 * np.power(weights, alpha).sum() - n
                index = h1 / n / alpha / (alpha - 1.0)
            return index

    def theil(self, data):
        """ Calculate the Theil Index (Generalized Entropy Index for a=1)

        :param data: Positive data
        :type data: numpy array
        :return: Theil Index (Float)

        `Open Risk Manual Entry for Theil Index <https://www.openriskmanual.org/wiki/Theil_Index>`_
        """
        weights = self.get_weights(data)
        return self.gei(weights, 1)

    def kolm(self, data, alpha):
        """ Calculate the Kolm index

        :param data: Positive data
        :type data: numpy array
        :param alpha: Index parameter
        :return: Kolm Index (Float)

        `Open Risk Manual Entry for Kolm Index <https://www.openriskmanual.org/wiki/Kolm_Index>`_
        """
        n = data.size
        if n == 0:
            return 0
        else:
            mu = data.mean()
            weights = self.get_weights(data)
            n_weights = np.multiply(- n * mu * alpha, weights)
            h = np.exp(n_weights).sum()
            return mu + (np.log(h) - np.log(n)) / alpha

    def ellison_glaeser(self, data, na, ni):
        """ Ellison and Glaeser (1997) indexes of industrial concentration.

        Implemented as in equation (5) of original reference
        Input data are a data frame of three columns of the following type:
        Exposure    Area        Industry
        Float       Categorical Categorical

        .. note:: The ordering of the columns is important. The index is not symmetric with respect to area and industry factors

        :param data: exposure data
        :type data: pandas dataframe
        :param na: number of areas
        :type na: integer
        :param ni: number of industries
        :type ni: integer
        :return: EG Indexes (list)

        `Open Risk Manual Entry for Ellison-Glaeser Index <https://www.openriskmanual.org/wiki/Ellison_Glaeser_Index>`_
        """

        #
        # Group by area
        #
        # Compute area totals and total exposure
        area_groups = data.groupby(['Area']).sum()
        area_totals = area_groups['Exposure'].values
        total_exposure = area_totals.sum()

        # Compute area fraction of total
        xa = area_totals / total_exposure

        # Compute area HHI
        hhi_g = self.hhi(area_totals, normalized=False)

        #
        # Group by industry
        #
        industry_groups = data.groupby(['Industry'])
        hhi_i = []
        industry_totals = []
        total = 0
        eg_indexes = []
        s = np.zeros((ni, na))
        for industry_index, group in industry_groups:
            # compute industry totals
            # x = group['Exposure'].as_matrix()
            x = group['Exposure'].values
            i_total = x.sum()
            total += i_total
            industry_totals.append(i_total)
            # compute industry specific HHI
            hhi_i_val = self.hhi(x, normalized=False)
            hhi_i.append(hhi_i_val)

            # compute industry/area fraction of industry total
            # group industy group further by area and sum up
            industry_group = pd.DataFrame(group).groupby('Area').sum()
            # The aggregated area values for this industry
            ig_values = industry_group.values[:, 0]
            # The index of the aggregated values
            ai = list(industry_group.index)
            # for all area and industry pairs with non-zero exposure
            for a in range(len(ai)):
                share = ig_values[a] / i_total
                s[industry_index, ai[a]] = share

            # compute EG industry concentration index
            egi = 0
            for a in range(len(ai)):
                egi += (s[industry_index, a] - xa[a]) ** 2
            val = hhi_i[industry_index]
            # original EG formula scaled so that uniform distribution has zero gi
            gi = egi / (1.0 - hhi_g) / (1 - val)
            eg_indexes.append(gi)

        return eg_indexes

    def compute(self, data, *args, ci=None, samples=None, index='hhi'):
        # Compute bootstraped confidence interval estimates

        # Actual value of the index
        value = self.callMethod(index, data, *args)
        if ci is not None:
            sample_values = []
            for s in range(samples):
                sample_data = np.random.choice(data, size=len(data), replace=True)
                sample_values.append(self.callMethod(index, sample_data, *args))

            values = np.array(sample_values)
            values.sort()
            lower_bound_index = int((1.0 - ci) * samples)
            upper_bound_index = int(ci * samples)
            lower_bound = values[lower_bound_index]
            upper_bound = values[upper_bound_index]
            return lower_bound, value, upper_bound
        else:
            return value
