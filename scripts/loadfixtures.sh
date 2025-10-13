#!/bin/bash
# source ./venv/bin/activate
python3 manage.py loaddata start/fixtures/DocPage.json
python3 manage.py loaddata start/fixtures/ORMKeyword.json
# python3 manage.py loaddata reference/fixtures/EmissionFactor.json
python3 manage.py loaddata reference/fixtures/BuildingEmissionFactor.json
python3 manage.py loaddata reference/fixtures/GPCSector.json
python3 manage.py loaddata reference/fixtures/NUTS3PointData.json
python3 manage.py loaddata reference/fixtures/ReferenceIntensity.json
python3 manage.py loaddata portfolio/fixtures/Project.json
python3 manage.py loaddata portfolio/fixtures/ProjectActivity.json
python3 manage.py loaddata portfolio/fixtures/PrimaryEffect.json
python3 manage.py loaddata portfolio/fixtures/SecondaryEffect.json
python3 manage.py loaddata portfolio/fixtures/GPCEmissionsSource.json
python3 manage.py loaddata risk/fixtures/Scenario.json