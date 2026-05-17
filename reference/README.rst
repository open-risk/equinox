Equinox Reference App
==========================================

Reference is an Equinox app that stores a variety of reference (external and/or slowly changing data).

List of External Reference Data stored
---------------------------------------

* CPV Classification (for European Public Procurement)
* IPCC Emission Factors (EFDB)
* GPC Sectors (Category Tree)
* NACE 2.0 Classification
* NUTS 3 Classification



List of Auxiliary Data stored
-----------------------------

* Emission Intensities
* Input-Output Data


Quick start
---------------------
1. Add "reference" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'reference',
]

2. Run ``python manage.py migrate`` to create the reference models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
