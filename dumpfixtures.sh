#!/bin/bash
source ./venv/bin/activate
python3 manage.py dumpdata --format=json --indent 2 reference.GPCSector -o reference/fixtures/GPCSector.json
python3 manage.py dumpdata --format=json --indent 2 reference.EmissionFactor -o reference/fixtures/EmissionFactor.json
python3 manage.py dumpdata --format=json --indent 2 reference.BuildingEmissionFactor -o reference/fixtures/BuildingEmissionFactor.json
python3 manage.py dumpdata --format=json --indent 2 start.ORMKeyword -o start/fixtures/ORMKeyword.json
python3 manage.py dumpdata --format=json --indent 2 start.DocPage -o start/fixtures/DocPage.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.Project -o portfolio/fixtures/Project.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.ProjectActivity -o portfolio/fixtures/ProjectActivity.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.PrimaryEffect -o portfolio/fixtures/PrimaryEffect.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.SecondaryEffect -o portfolio/fixtures/SecondaryEffect.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.GPCEmissionsSource -o portfolio/fixtures/GPCEmissionsSource.json