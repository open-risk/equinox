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
import random
import string

from django.core.management import BaseCommand
from django.db import connection

from reference.IOData import IOGraph, IOGraphEdge, IOGraphNode


def random_string(n=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))


class Command(BaseCommand):
    help = 'Insert test IO Graph Data'

    def handle(self, *args, **kwargs):
        # Delete existing objects
        IOGraph.objects.all().delete()
        IOGraphEdge.objects.all().delete()
        IOGraphNode.objects.all().delete()

        size = 4

        G = IOGraph(
            io_year='2022',
            io_family='Test IO',
            io_part='X',
            nodes=size,
            edges=size,
            dtype='float64',
            metadata=None
        )
        G.save()

        indata = []
        for i in range(size):
            node = IOGraphNode(
                graph=G,
                row_idx=i,
                row_lbl=random_string()
            )
            indata.append(node)
        IOGraphNode.objects.bulk_create(indata)

        indata = []
        for i in range(size):
            for j in range(size):
                edge = IOGraphEdge(
                    graph=G,
                    row_idx=i,
                    col_idx=j,
                    value=random.random()
                )
                indata.append(edge)

        IOGraphEdge.objects.bulk_create(indata)
