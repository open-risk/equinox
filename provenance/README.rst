Equinox Provenance App
==========================================
Provenance is a Django app to help keep track of data provenance.

It loosely follows the data schemas of the PROV ontology.

Currently only the Agent model is implemented.


Quick start
---------------------
1. Add "portfolio" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'provenance',
]

2. Run ``python manage.py migrate`` to create the provenance models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
