Equinox Policy
==========================================
Policy is an Equinox app to monitor and manage portfolio-wide policy data.

In a sustainable portfolio management context, Policy refers to a system of principles, objectives, rules and guidelines, adopted by an Organization (company, public sector etc.) to guide decision making with respect to particular situations and implemented via procedures or protocols to achieve stated goals.

Policies express the plan or course of action by an authority, intended to influence and determine decisions, actions, and other matters. Policy defines limits within which decisions are made.

The equinox





Quick Start
---------------------
1. Add "policy" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'policy',
]

2. Include the policies URLconf in your project urls.py like this::
path('policy/', include('policy.urls')),

3. Run ``python manage.py migrate`` to create the policy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/

to create a policy (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/policy/ to start working with policy data
