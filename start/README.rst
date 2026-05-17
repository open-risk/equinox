Equinox Start App
==========================================

Start is the core Equinox app providing front page functionality and supporting various auxiliary tasks.

This would normally be included by default as the first of the Equinox apps in the settings.py file

Quick start
---------------------
1. Add "start" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'start',
]

2. Include the risk URLconf in your project urls.py like this::
path('start/', include('start.urls')),

3. Run ``python manage.py migrate`` to create the Start models.

4. Start the development server and visit http://127.0.0.1:8000/admin/