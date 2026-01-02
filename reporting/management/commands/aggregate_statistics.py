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

from django.core.management import BaseCommand

from reporting.models import SummaryStatistics, AggregatedStatistics


class Command(BaseCommand):
    help = 'Aggregate summary statistics across time for top-level sectors'

    def handle(self, *args, **kwargs):
        # Delete existing objects
        AggregatedStatistics.objects.all().delete()

        stats = SummaryStatistics.objects.all()

        # aggregate sectors to top level
        top_level = {}
        for entry in stats:
            dataid = entry.sector[:1]
            key = (dataid, entry.country)
            if key in top_level.keys():
                top_level[key] += entry.value_total
            else:
                top_level[key] = entry.value_total

        indata = []
        for key in top_level:
            # print(key[0], key[1], top_level[key])
            co = AggregatedStatistics(
                country=key[1],
                sector=key[0],
                value_total=top_level[key]
            )
            indata.append(co)

        AggregatedStatistics.objects.bulk_create(indata)
