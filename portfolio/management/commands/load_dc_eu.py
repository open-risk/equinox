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

import json

import geojson
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from portfolio.DataCenter import DataCenter
from portfolio.Operator import Operator
from portfolio.Portfolios import ProjectPortfolio, PortfolioSnapshot
from provenance.models import Agent

from utils.geospatial import calculate_barycenter, calculate_polygon_area


class Command(BaseCommand):
    help = 'Imports Data Center / Operator data from the euroDaCe Dataset'

    # Import data from GeoJSON file

    # filename = 'portfolio/fixtures/dc.0.2.json'
    filename = 'portfolio/fixtures/dc.0.1.json'

    """
    Create Data Center Operators (if they do not exist already in the DB)

    """

    operators = []
    with open(filename) as f:
        data = json.load(f)
        if isinstance(data.get('features'), list):
            features = data.get('features')
            for feature in features:
                props = feature['properties']
                if 'operator' in props.keys():
                    operators.append(props['operator'])
        operators = list(set(operators))
    f.close()

    noop = len(operators)
    print(f"Found {noop:02d} operators")

    newop = 0
    for operator in operators:
        op, created = Operator.objects.get_or_create(operator_identifier=operator)
        if created:
            newop += 1

    # Placeholder Operator if Unknown
    op, created = Operator.objects.get_or_create(operator_identifier='Unknown')
    if created:
        newop += 1

    print(f"Created {newop:02d} operators")

    """
     Create Portfolio, Portfolio Snapshot and Provenance Data

    """

    portfolio_id, portfolio_created = ProjectPortfolio.objects.get_or_create(name='EU Data Centers')

    portfolio_snapshot_id, snapshot_created = PortfolioSnapshot.objects.get_or_create(name='2025')

    agent_id, agent_created = Agent.objects.get_or_create(name='OSM')

    print('Created Portfolio, Snapshot, Agent Data')

    """
    Create Data Centers
    
    """

    print('Inserting Data Center Data')
    indata = []
    with open(filename) as f:
        data = json.load(f)
        if isinstance(data.get('features'), list):
            features = data.get('features')
            for feature in features:
                props = feature['properties']

                if 'operator' in props.keys():
                    operator_name = props['operator']
                else:
                    operator_name = 'Unknown'
                op = Operator.objects.get(operator_identifier=operator_name)

                if 'name' in props.keys():
                    data_center_name = props['name']
                else:
                    data_center_name = 'Unknown'

                # TODO roundtrip consistency
                # ID key depends on whether GeoJSON is direct OSM import or Equinox export

                if 'datacenter_id' in props.keys():
                    datacenter_id = props['datacenter_id']
                elif '@id' in props.keys():
                    datacenter_id = props['@id']

                # Branch according to geometry type
                geom = feature['geometry']['type']
                coords = str(feature['geometry']['coordinates'])
                coordinates = list(geojson.utils.coords(feature))

                geometry = None
                surface_area = None

                if geom == 'Point':
                    lon = feature['geometry']['coordinates'][0]
                    lat = feature['geometry']['coordinates'][1]
                    gstring = '{"type": "Point", "coordinates": ' + coords + '}'
                    geometry = GEOSGeometry(gstring)
                    dc = DataCenter(
                        portfolio=portfolio_id,
                        snapshot=portfolio_snapshot_id,
                        datacenter_id=datacenter_id,
                        datacenter_name=data_center_name,
                        country=props['country'],
                        datacenter_location=Point(lon, lat),
                        geometry_type=DataCenter.get_geometry_by_display(geom),
                        operator=op,
                        prov_operator=agent_id)
                    indata.append(dc)
                elif geom in ['LineString', 'Polygon', 'MultiPolygon']:
                    if geom == 'LineString':
                        gstring = '{"type": "LineString", "coordinates": ' + coords + '}'
                    elif geom == 'Polygon':
                        gstring = '{"type": "Polygon", "coordinates": ' + coords + '}'
                        surface_area = calculate_polygon_area(coordinates)
                    elif geom == 'MultiPolygon':
                        gstring = '{"type": "MultiPolygon", "coordinates": ' + coords + '}'
                    geometry = GEOSGeometry(gstring)

                    dc = DataCenter(
                        portfolio=portfolio_id,
                        snapshot=portfolio_snapshot_id,
                        datacenter_id=datacenter_id,
                        datacenter_name=data_center_name,
                        country=props['country'],
                        datacenter_location=Point(calculate_barycenter(coordinates)),
                        geometry=geometry,
                        geometry_type=DataCenter.get_geometry_by_display(geom),
                        surface_area=surface_area,
                        operator=op,
                        prov_operator=agent_id)
                    indata.append(dc)
                else:
                    print("No geometry found")

    nodc = len(indata)
    print(f"Created {nodc:02d} data centers")

    DataCenter.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted all Data Center data into the db'))
