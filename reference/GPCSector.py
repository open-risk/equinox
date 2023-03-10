# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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

from django.db import models

from treebeard.mp_tree import MP_Node

GPC_SCOPES = [(0, 'Scope 1'), (1, 'Scope 2'), (2, 'Scope 3')]


class GPCSector(MP_Node):
    """
    The GPC Sector model implements a Category Tree for GPC Sectors


    """
    name = models.CharField(max_length=50, help_text="A concise name")

    gpc_ref_no = models.CharField(max_length=10, help_text="The GPC Reference number")

    gpc_scope = models.IntegerField(blank=True, null=True, choices=GPC_SCOPES,
                                    help_text="Applicable GHG Emission Scope (Numerical: 1, 2, 3). This is linked to the GPC Reference Number")

    description = models.TextField(blank=True, null=True, help_text="Detailed Sectoral Description")

    node_order_by = ['name']

    # bookkeeping
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'GPC Sector: {}'.format(self.name)

    class Meta:
        verbose_name = "GPC Sector"
        verbose_name_plural = "GPC Sectors"
