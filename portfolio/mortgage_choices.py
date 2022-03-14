# Copyright (c) 2020 - 2022 Open Risk (https://www.openriskmanagement.com)
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


#
# CHOICE DICTIONARIES MORTGAGES
#

CHANNEL_OF_ORIGINATION_CHOICES = [(0, '(a) Branch'), (1, '(b) Internet'), (2, '(c) Broker'), (3, '(d) Other')]

ASSET_CLASS_CHOICES = [(0, 'Residential'), (1, 'CRE')]

LOAN_PURPOSE_CHOICES = [(0, '(a) Residential real estate - owner occupied'),
                        (1, '(b) Residential real estate investment'),
                        (2, '(c) Commercial Real Estate (CRE)'),
                        (5, '(f) Commercial development'),
                        (6, '(g) Residential development')]


AMORTISATION_TYPE_CHOICES = [(0, '(a) Linear (L)'), (1, '(b) Annuity (A)'),
                             (2, '(c) Interest Only (IO) i.e. no amortisation with a bullet'),
                             (3, '(d) Bespoke Repayment')]

ACCOUNTING_STAGES_OF_ASSET_QUALITY_CHOICES = [(0, '(a) IFRS Stage 1'), (1, '(b) IFRS Stage 2'),
                                              (2, '(c) IFRS Stage 3 (Impaired)'),
                                              (3, '(d) Fair Value Through P rofit and Loss'),
                                              (4, '(e) Other Accounting Standard - Impaired Asset'),
                                              (5, '(f) Other Accounting Standard - Not Impaired')]

ORIGINAL_INTEREST_RATE_TYPE_CHOICES = [(0, '(a) Fixed'), (1, '(b) Variable'), (2, '(c) Mixed')]

ORIGINAL_INTEREST_RATE_REFERENCE_CHOICES = [(0, '(a) 1m EURIBOR'), (1, '(b) 3m EURIBOR'), (2, '(c) 6m EURIBOR'),
                                            (3, '(d) 1m LIBOR'), (4, '(e) 3m LIBOR'), (5, '(f) 6m LIBOR'),
                                            (6, '(g) Standard Variable Rate (SVR)'), (7, '(h) EONIA')]

CURRENT_INTEREST_RATE_TYPE_CHOICES = [(0, '(a) Fixed'), (1, '(b) Variable'), (2, '(c) Mixed')]

CURRENT_INTEREST_RATE_REFERENCE_CHOICES = [(0, '(a) 1m EURIBOR'), (1, '(b) 3m EURIBOR'), (2, '(c) 6m EURIBOR'),
                                           (3, '(d) 1m LIBOR'), (4, '(e) 3m LIBOR'), (5, '(f) 6m LIBOR'),
                                           (6, '(g) Standard Variable Rate (SVR)'), (7, '(h) EONIA')]

INTEREST_PAYMENT_FREQUENCY_CHOICES = [(0, '(a) Monthly'), (1, '(b) Quarterly'), (2, '(c) Semi-Annually'),
                                      (3, '(d) Annually'), (4, '(e) Daily'), (5, '(f) Other')]

PRINCIPAL_PAYMENT_FREQUENCY_CHOICES = [(0, '(a) Monthly'), (1, '(b) Quarterly'), (2, '(c) Semi-Annually'),
                                       (3, '(d) Annually'), (4, '(e) Daily'), (5, '(f) Other')]

LOAN_STATUS_CHOICES = [(0, '(a) Performing'), (
    1, '(b) Non-performing as defined in table F18 in Annex V to Implementing Regulation (EU) No 680/2014')]

NONPERFORMING_REASON_CHOICES = [(0, '(a) Impaired as defined by IFRS 9.5.5 or the applicable accounting standard'),
                                (1, '(b) Defaulted as defined by CRR Art. 178'),
                                (2, '(c) More than 90 days past due'), (3, '(d) Unlikely to pay')]

LOAN_COVENANTS_CHOICES = [
    (0, '(a) Loan to Value (LTV) is the ratio of a loan to the value of the collateral purchased'),
    (1, '(b) Interest Coverage Ratio (ICR) is the ratio of earnings before interest and tax to the '
        'interest expense in the same period'),
    (2, '(c) Debt Service Coverage Ratio (DSCR) is the ratio of annual net operating income to debt '
        'obligations owed in the last 12m'),
    (3, '(d) Other')]

MARP_STATUS_CHOICES = [(0, '(a) Not in MARP'), (1, '(b) Exited MARP'), (2, '(c) Provision 23 - 31 days in arrears'), (3, '(d) Provision 24 - Financial difficulty'), (4, '(e) Provision 28 - Not co-operating warning'), (5, '(f) Provision 29 - Not co-operating'), (6, '(g) Provision 42 - Restructure offer'), (7, '(h) Provision 45 - Restructure declined by seller'), (8, '(i) Provision 47 - Restructure declined by borrower'), (9, '(j) Self-Cure'), (10, '(k) Alternative Repayment Arrangement (ARA)')]
