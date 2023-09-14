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

# !/usr/bin/env python
import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'equinox.settings'
django.setup()

from portfolio.ProjectCategory import ProjectCategory

get = lambda node_id: ProjectCategory.objects.get(pk=node_id)

# GHG Protocol Project Categories
root = ProjectCategory.add_root(name='Generic Project')
ghg_node = get(root.pk).add_child(name='GHG Protocol Project')
ted_node = get(root.pk).add_child(name='Procurement Project')

node = get(ghg_node.pk).add_child(name='Wind Power')
get(node.pk).add_sibling(name='Landfill Gas')
get(node.pk).add_sibling(name='Afforestation')
get(node.pk).add_sibling(name='Energy Efficiency')
get(node.pk).add_sibling(name='Transportation Fuel Switch')
get(node.pk).add_sibling(name='Industrial Fuel Switch')
get(node.pk).add_sibling(name='Agricultural Tillage')

# Procurement Project Categories

node = get(ted_node.pk).add_child(name='WORKS')
get(node.pk).add_sibling(name='SERVICES')
get(node.pk).add_sibling(name='SUPPLIES')
