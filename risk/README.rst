Equinox Risk
==========================================
Risk is an Equinox app dedicated to performing various Risk Analysis tasks on the basis of Equinox data

Quick start
---------------------
1. Add "risk" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'risk',
]

2. Include the risk URLconf in your project urls.py like this::
path('risk/', include('risk.urls')),

3. Run ``python manage.py migrate`` to create the risk models.

4. Start the development server and visit http://127.0.0.1:8000/admin/