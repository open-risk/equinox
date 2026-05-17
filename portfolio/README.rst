Equinox Portfolio App
==========================================
Portfolio is a Django app to store Sustainable Portfolio Data.

This is the central collection of objects, most other apps in some way depend or augment the functionality provided by the Portfolio app.

Quick start
---------------------
1. Add "portfolio" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'portfolio',
]

2. Run ``python manage.py migrate`` to create the portfolio models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
