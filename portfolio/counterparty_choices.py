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
# ADDITIONAL CHOICES
#

BORROWER_TYPE_CHOICES = [(0, '(a) Private Individual'), (1, '(b) Corporate')]


#
# EBA CHOICE DICTIONARIES COUNTERPARTY
#

COUNTERPARTY_ROLE_CHOICES = [(0, '(a) Guarantor'), (1, '(b) Borrower'), (2, '(c) Tenant')]

LEGAL_TYPE_OF_COUNTERPARTY_CHOICES = [
    (0, '(a) Listed Corporate is a Corporate entity whose shares are quoted and traded on a Stock Exchange'),
    (1, '(b) Unlisted Corporate is a Corporate entity whose shares are not quoted and traded on a stock exchange, '
        'however an unlisted corporate may have an unlimited number of shareholders to raise capital for any '
        'commercial venture'),
    (2, '(c) Listed Fund is a fund whose shares are quoted and traded on a Stock exchange'),
    (3, '(d) Unlisted Fund is a fund whose shares are not quoted and traded on a Stock exchange'),
    (4, '(e) Partnership is where the Sponsor constitutes a group of individuals who form a legal partnership, '
        'where profits and liabilities are shared; or,'),
    (5, '(f) Private Individual')]

TYPE_OF_PERSONAL_IDENTITY_NUMBER_CHOICES = [(0, '(a) Passport Number'), (1, '(b) National Insurance Number'),
                                            (2, '(c) National tax number'), (3, '(d) Other')]

GEOGRAPHIC_REGION_CLASSIFICATION_CHOICES = [(0, '(a) NUTS3 2013'), (1, '(b) NUTS3 2010'), (2, '(c) NUTS3 2006'),
                                            (3, '(d) NUTS3 2003'), (4, '(e) Other')]

EMPLOYMENT_STATUS_CHOICES = [(0, '(a) Employed'), (1, '(b) Employed with partial support (company subsidy)'),
                             (2, '(c) Protected life-time employment (civil servant)'), (3, '(d) Self-employed'),
                             (4, '(e) Unemployed'), (5, '(f) Student'), (6, '(g) Pensioner'), (7, '(h) Other')]

BASIS_OF_FINANCIAL_STATEMENTS_CHOICES = [(0, '(a) IFRS'), (1, '(b) National GAAP '), (2, '(c) Other')]

FINANCIAL_STATEMENTS_TYPE_CHOICES = [(0, '(a) Consolidated'), (1, '(b) Counterparty level')]

ENTERPRISE_SIZE_CHOICES = [(0, '(a) Micro-enterprise'), (1, '(b) Small enterprise'), (2, '(c) Medium enterprise'),
                           (3, '(d) Large enterprise')]

CROSS_DEFAULT_FOR_COUNTERPARTY_CHOICES = [(0, '(a) Full'), (1, '(b) Partial'), (2, '(c) None')]

CROSS_COLLATERALISATION_FOR_COUNTERPARTY_CHOICES = [(0, '(a) Full'), (1, '(b) Partial'), (2, '(c) None')]

LEGAL_STATUS_CHOICES = [
    (0, '(a) Listed Corporate is a Corporate entity whose shares are quoted and traded on a Stock Exchange'),
    (1, '(b) Unlisted Corporate is a Corporate entity whose shares are not quoted and traded on a stock exchange, '
        'however an unlisted corporate may have an unlimited number of shareholders to raise capital for any '
        'commercial venture'),
    (2, '(c) Listed Fund is a fund whose shares are quoted and traded on a Stock exchange'),
    (3, '(d) Unlisted Fund is a fund whose shares are not quoted and traded on a Stock exchange'),
    (4, '(e) Partnership is where the Sponsor constitutes a group of individuals who form a legal partnership, '
        'where profits and liabilities are shared; or,'),
    (5, '(f) Private Individual')]

LEGAL_PROCEDURE_TYPE_CHOICES = [(0, '(a) Corporate Restructuring Procedures, which also include funds'),
                                (1, '(b) Corporate Insolvency Procedures, which also include funds'),
                                (2, '(c) Private Individual Counterparty Debt Compromise Procedures'),
                                (3, '(d) Private Individual Counterparty Insolvency Procedures'),
                                (4, '(e) Partnership Restructuring Procedures'),
                                (5, '(f) Partnership Insolvency Procedures')]

LEGAL_PROCEDURE_NAME_CHOICES = [(0, 'Country Specific: Annex I')]


STAGE_REACHED_IN_INSOLVENCY_OR_RESTRUCTURING_PROCEDURE_CHOICES = [(0, '(a) A creditors committee has been formed'), (1, '(b) A moratorium against enforcement is in place'), (2, '(c) A restructuring plan has been proposed'), (3, '(d) A restructuring plan has been approved'), (4, '(e) A proof of claim has been filed'), (5, '(f) A bar date for claims has been issued'), (6, '(g) A notice of intention to sell secured assets has been given'), (7, '(h) A distribution has been made to secured creditors'), (8, '(i) A distribution has been made to unsecured creditors'), (9, '(j) A notice of the end of the procedure has been given')]
