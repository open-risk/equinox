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

from django.db import models, transaction, connection
from django.db.models import Index, Sum
import uuid

from django.urls import reverse


class IOMatrix(models.Model):
    """
    The IOMatrix model holds the key information about IO datasets stored in Equinox

    NB: Multi-regional data must be flattened

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text='IO Matrix ID')
    io_year = models.PositiveIntegerField(null=True, blank=True, help_text="Reference Year")
    io_family = models.CharField(max_length=80, null=True, blank=True, help_text="IO Family")
    io_part = models.CharField(max_length=80, null=True, blank=True, help_text="IO Part")
    nrows = models.PositiveIntegerField(null=True, blank=True, help_text="Number of Rows")
    ncols = models.PositiveIntegerField(null=True, blank=True, help_text="Number of Columns")
    dtype = models.CharField(max_length=32, default='float64', help_text="Data Type")
    metadata = models.JSONField(null=True, blank=True, help_text="Additional Description")
    created_at = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "io_matrices"
        verbose_name = "IO Matrix"
        verbose_name_plural = "IO Matrices"

    def __str__(self):
        return f"IO Matrix {self.io_family}[{self.io_year}]: {self.io_part} ({self.nrows}x{self.ncols})"

    def get_absolute_url(self):
        return reverse('reference:IOMatrix_edit', kwargs={'pk': self.pk})


class IOMatrixEntry(models.Model):

    matrix = models.ForeignKey(IOMatrix, on_delete=models.CASCADE, related_name='io_matrix_entries')
    row_idx = models.IntegerField()
    col_idx = models.IntegerField()
    row_lbl = models.TextField()
    col_lbl = models.TextField()
    value = models.FloatField()

    class Meta:
        db_table = "io_matrix_entries"
        unique_together = (("matrix", "row_idx", "col_idx"),)
        indexes = [
            Index(fields=['matrix', 'row_idx', 'col_idx'], name='mx_row_col_idx'),
            Index(fields=['matrix', 'row_idx'], name='mx_row_idx'),
            Index(fields=['matrix', 'col_idx'], name='mx_col_idx'),
        ]
        verbose_name = "IO Matrix Entry"
        verbose_name_plural = "IO Matrix Entries"

    def __str__(self):
        return f"({self.row_idx},{self.col_idx})={self.value}"

    @classmethod
    def fetch_submatrix(cls, matrix_id, r1, r2, c1, c2):
        """
        Return list of (row_idx, col_idx, value) within specified bounds.
        """
        return list(
            cls.objects.filter(
                matrix_id=matrix_id,
                row_idx__gte=r1, row_idx__lte=r2,
                col_idx__gte=c1, col_idx__lte=c2
            ).values_list('row_idx', 'col_idx', 'value')
            .order_by('row_idx', 'col_idx')
        )

    @classmethod
    def row_sums(cls, matrix_id):
        """
        Return list of (row_idx, sum) for the matrix.
        """
        return list(
            cls.objects.filter(matrix_id=matrix_id)
            .values('row_idx')
            .annotate(sum=Sum('value'))
            .order_by('row_idx')
        )
