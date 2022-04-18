Equinox Policy
==========================================
Policy is an Equinox app to monitor and manage portfolio-wide policy data.

Quick start
---------------------
1. Add "policy" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'policy',
]

2. Include the policies URLconf in your project urls.py like this::
path('policy/', include('policy.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/

to create a policy (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/policy/ to start working with policy data
