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


from shapely.geometry import Polygon

"""
Calculate the area of a polygon
Does not work reliably with linestrings or multipolygons

"""


def calculate_polygon_area(coordinates):

    polygon = Polygon(coordinates)
    area = polygon.area
    return area


"""
Calculate the centroid (barycenter) for a given set of coordinates
Works with any geometry, (multi)polygon, linestring etc.

"""


def calculate_barycenter(coordinates):
    x_sum = 0
    y_sum = 0
    num_points = len(coordinates)

    for coord in coordinates:
        x_sum += coord[0]
        y_sum += coord[1]

    barycenter_x = x_sum / num_points
    barycenter_y = y_sum / num_points

    point = (barycenter_x, barycenter_y)
    return point
