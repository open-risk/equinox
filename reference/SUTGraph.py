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


class SUTGraph(models.Model):
    """
    The SUTGraph model implements a graph version of SUT system storage

    Key features
    - transaction matrices are stored as weighted adjacency matrices
    - only non-zero values are stored in graph edges

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text='SUT Graph ID')
    sut_year = models.PositiveIntegerField(null=True, blank=True, help_text="Reference Year")
    sut_family = models.CharField(max_length=80, null=True, blank=True, help_text="SUT Family")
    s_nodes = models.PositiveIntegerField(null=True, blank=True, help_text="Number of Supply Nodes")
    u_nodes = models.PositiveIntegerField(null=True, blank=True, help_text="Number of Edge Nodes")
    dtype = models.CharField(max_length=32, default='float64', help_text="Data Type")
    metadata = models.JSONField(null=True, blank=True, help_text="Additional Description")
    created_at = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sut_graphs"
        verbose_name = "SUT Graph"
        verbose_name_plural = "SUT Graphs"

    def __str__(self):
        return f"SUT Matrix {self.sut_family}[{self.sut_year}]: ({self.s_nodes}x{self.u_nodes})"

    def get_absolute_url(self):
        return reverse('reference:SUTGraph_edit', kwargs={'pk': self.pk})


class SUTGraphEdge(models.Model):
    graph = models.ForeignKey(SUTGraph, on_delete=models.CASCADE, related_name='sut_graph_edges')
    row_idx = models.IntegerField()
    col_idx = models.IntegerField()
    value = models.FloatField()

    class Meta:
        db_table = "sut_graph_edges"
        unique_together = (("graph", "row_idx", "col_idx"),)
        indexes = [
            Index(fields=['graph', 'row_idx', 'col_idx'], name='sut_edge_row_col_idx'),
            Index(fields=['graph', 'row_idx'], name='sut_edge_row_idx'),
            Index(fields=['graph', 'col_idx'], name='sut_edge_col_idx'),
        ]
        verbose_name = "SUT Graph Edge"
        verbose_name_plural = "SUT Graph Edges"

    def __str__(self):
        return f"({self.row_idx},{self.col_idx})={self.value}"


class SUTGraphNode(models.Model):
    graph = models.ForeignKey(SUTGraph, on_delete=models.CASCADE, related_name='sut_graph_nodes')
    row_idx = models.IntegerField()
    row_lbl = models.TextField()

    class Meta:
        db_table = "sut_graph_nodes"
        unique_together = (("graph", "row_idx"),)
        indexes = [
            Index(fields=['graph', 'row_idx'], name='sut_node_row_idx'),
        ]
        verbose_name = "SUT Graph Nodes"
        verbose_name_plural = "SUT Graph Nodes"

    def __str__(self):
        return f"({self.row_lbl})"
