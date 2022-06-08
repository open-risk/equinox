#!/bin/bash
source ./venv/bin/activate

python3 manage.py dumpdata --format=json --indent 2 start.DocPage -o start/fixtures/DocPage.json
python3 manage.py dumpdata --format=json --indent 2 start.ORMKeyword -o start/fixtures/ORMKeyword.json

python3 manage.py dumpdata --format=json --indent 2 reference.EmissionFactor -o reference/fixtures/EmissionFactor.json
python3 manage.py dumpdata --format=json --indent 2 reference.BuildingEmissionFactor -o reference/fixtures/BuildingEmissionFactor.json
python3 manage.py dumpdata --format=json --indent 2 reference.GPCSector -o reference/fixtures/GPCSector.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.PortfolioManager -o portfolio/fixtures/PortfolioManager.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.Project -o portfolio/fixtures/Project.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.ProjectActivity -o portfolio/fixtures/ProjectActivity.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.PrimaryEffect -o portfolio/fixtures/PrimaryEffect.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.SecondaryEffect -o portfolio/fixtures/SecondaryEffect.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.GPCEmissionsSource -o portfolio/fixtures/GPCEmissionsSource.json

python3 manage.py dumpdata --format=json --indent 2 risk.Scenario -o risk/fixtures/Scenario.json

python3 manage.py dumpdata auth.User --indent 2 > start/fixtures/users.json
python3 manage.py dumpdata auth.Group --indent 2 > start/fixtures/groups.json
python3 manage.py dumpdata --format=json --indent 2 portfolio.PointSource -o portfolio/fixtures/PointSource.json

python3 manage.py dumpdata reference.NUTS3PointData --indent 2 > reference/fixtures/NUTS3PointData.json
