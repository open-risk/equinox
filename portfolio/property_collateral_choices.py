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
# CHOICE DICTIONARIES PROPERTY COLLATERAL
#

SECTOR_OF_PROPERTY_CHOICES = [(0, '(a) Commercial Real Estate'), (1, '(b) Residential Real Estate')]

TYPE_OF_PROPERTY_CHOICES = [(0, '(a) Semi-detached house'), (1, '(b) Detached house'), (2, '(c) Apartment'),
                            (3, '(d) Terrace'), (4, '(e) Caravan Park'), (5, '(f) Car Park'),
                            (6, '(g) Health Care'), (7, '(h) Hospitality / Hotel'), (8, '(i) Industrial'),
                            (9, '(j) Land – agriculture'), (10, '(k) Land - zoning'), (11, '(l) Land - permit'),
                            (12, '(m) Leisure'), (13, '(n) Multifamily '), (14, '(o) Mixed Use'),
                            (15, '(p) Office'), (16, '(q) Bar / Pub'), (17, '(r) Restaurant'), (18, '(s) Retail'),
                            (19, '(t) High street retail'), (20, '(u) Commercial centre'), (21, '(v) Self-Storage'),
                            (22, '(w) Warehouse'), (23, '(x) Other')]

TYPE_OF_OCCUPANCY_CHOICES = [(0, '(a) Owner-occupied'),
                             (1, '(b) Partially owner-occupied, defined as a property that is partly rented'),
                             (2, '(c) Tenanted'), (3, '(d) Vacant'), (4, '(e) Other')]

PURPOSE_OF_PROPERTY_CHOICES = [(0, '(a) Investment property'), (1, '(b) Owner occupied'), (2, '(c) Buy-to-let'),
                               (3, '(d) Other')]

CONDITION_OF_PROPERTY_CHOICES = [(0, '(a) Excellent'), (1, '(b) Good'), (2, '(c) Fair'), (3, '(d) Poor')]

GEOGRAPHIC_REGION_CLASSIFICATION_CHOICES = [(0, '(a) NUTS3 2013'), (1, '(b) NUTS3 2010'), (2, '(c) NUTS3 2006'),
                                            (3, '(d) NUTS3 2003'), (4, '(e) Other')]

AREA_TYPE_OF_PROPERTY_CHOICES = [(0, '(a) Prime city centre'), (1, '(b) City centre'), (2, '(c) City non-centre'),
                                 (3, '(d) Suburban'), (4, '(e) Rural')]

TENURE_CHOICES = [(0, '(a) Freehold'), (1, '(b) Leasehold'), (2, '(c) Other')]

INTERNAL_or_EXTERNAL_INITIAL_VALUATION_CHOICES = [(0, '(a) Internal'), (1, '(b) Outsourced')]

TYPE_OF_INITIAL_VALUATION_CHOICES = [(0, '(a) Full Appraisal'), (1, '(b) Drive-by'),
                                     (2, '(c) Automated Valuation Model'), (3, '(d) Indexed'), (4, '(e) Desktop'),
                                     (5, '(f) Managing or Estate Agent'), (6, '(g) Purchase Price'),
                                     (7, '(h) Mark to market'), (8, '(i) Counterparties Valuation'),
                                     (9, '(j) Other')]

INTERNAL_or_EXTERNAL_LATEST_VALUATION_CHOICES = [(0, '(c) Internal'), (1, '(d) Outsourced')]

TYPE_OF_LATEST_VALUATION_CHOICES = [(0, '(a) Full Appraisal'), (1, '(b) Drive-by'),
                                    (2, '(c) Automated Valuation Model'), (3, '(d) Indexed'), (4, '(e) Desktop'),
                                    (5, '(f) Managing or Estate Agent'), (6, '(g) Purchase Price'),
                                    (7, '(h) Hair Cut'), (8, '(i) Mark to market'),
                                    (9, '(j) Counterparties Valuation'), (10, '(k) Other')]

PARTY_LIABLE_FOR_VAT_CHOICES = [(0, '(a) Institution'), (1, '(b) Buyer(s)'), (2, '(c) Counterparty')]

VALUE_OF_ENERGY_PERFORMANCE_CERTIFICATE_CHOICES = [(0, '(a) A'), (1, '(b) B'), (2, '(c) C'), (3, '(d) D'),
                                                   (4, '(e) E'), (5, '(f) F'), (6, '(g) G')]
