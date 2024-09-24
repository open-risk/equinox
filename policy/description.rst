Policy App
=============================
The Policy App provides portfolio-wide Policy oriented functionality of equinox.

Policies are in general discretionary choices among a menu options (that can change over time). They can be numerical or categorical in nature.

Category
--------
Policies


Models
------

Policy Models Store generic policy data

* Dataflow
* Dataseries
* Geoslice

Admin
-----

Standard Model Admin


API
---
TODO

Functionality
-----------------------

* Provide overviews and dashboards for portfolio-wide policy data

Management Commands
--------------------

* create fixtures for Oxford COVID policy database
* create fixtures for OECD CAPMF policy database

Architecture
------------

Dependencies
-----------------

* core app Django only
* management commands:

    * pandas
    * scipy

Is dependent on by
--------------------

File structure
-----------------
TODO


Testing
----------------------

* test/test_policy/test_models.py (test creation of core models)
* policy/tests.py

Backup Procedure
---------------------
