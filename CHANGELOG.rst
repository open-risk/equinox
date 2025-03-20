ChangeLog
===========================

This is the *global* Changelog for the overall Equinox platform and its API changes. Individual apps have their own more detailed changelogs within each app's subdirectory:

* :doc:`portfolio-changelog`
* :doc:`policy-changelog`
* :doc:`reference-changelog`
* :doc:`reporting-changelog`
* :doc:`start-changelog`
* :doc:`risk-changelog`

v0.8.0 (25-09-2024)
-------------------
* Enhancements: OECD Climate Actions and Policies Workflow
* Dependencies: Django 5.0 related updates
    * OSMGeoAdmin deprecation
    * sqlite bug workaround: python ./manage.py shell -c "import django;django.db.connection.cursor().execute('SELECT InitSpatialMetaData(1);')";
* Enhancements: Postgres backend option
* Scripts for deleting user data from database
* Vega visualization framework

v0.7.1 (14-09-2023)
-------------------
* Update to Python 3.10

v0.7 (09-06-2023)
-------------------
* Enhancements: New models supporting Scope 2 reporting
* Fixtures for various use cases
* Adopt pytest and basic coverage of all models

v0.6 (15-06-2022)
-----------------
* Enhancements: cpv / cpa mapping
* Documentation: expand to cover app views
* Dependencies: added scipy, bumped to latest versions
* Summary Statistics Reporting and Visualization
* Adopt behave BDD testing framework

v0.5 (25-05-2022)
-----------------
* Release 0.5 includes a complete data set to be used in testing "use case 1" (featuring mock city-wide procurement portfolio)

v0.4 (22-04-2022)
------------------
* Earth Day 2022 Release
* Major enhancements include procurement data framework and portfolio policy framework

v0.3.2 (31-03-2022)
-------------------
* Integration of Procurement data models / workflows

v0.3.14 (14-03-2022)
--------------------
* Pi-Day pre-release
* PCAF for Mortgages

v0.3 (01-03-2022)
-----------------
* Release on PyPI
* Release Docs on Read The Docs

v0.2 (22-04-2021)
-----------------
* Earth Day Release. Integration of PCAF metrics

v0.1 (21-03-2021)
-------------------
* Initial Release of Equinox