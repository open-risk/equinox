Equinox Reporting App
==========================================

Reporting is an Equinox app that produces a range of reports in various formats.

List of Report Types
---------------------------------------

* Tabular
* Maps
* Ad-hoc Visualization

Quick start
---------------------

1. Add "reporting" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'reporting',
]

2. Include the reporting URLconf in your project urls.py like this::
path('reporting/', include('reporting.urls')),

3. Run ``python manage.py migrate`` to create the reporting models.

4. Start the development server and visit http://127.0.0.1:8000/admin/