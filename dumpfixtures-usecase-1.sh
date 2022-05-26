#!/bin/bash
source ./venv/bin/activate

python3 manage.py dumpdata --format=json --indent 2 portfolio.PortfolioManager -o portfolio/fixtures/usecase-1/PortfolioManager.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.ProjectPortfolio -o portfolio/fixtures/usecase-1/ProjectPortfolio.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.Project -o portfolio/fixtures/usecase-1/Project.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.Contractor -o portfolio/fixtures/usecase-1/Contractor.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.ProjectActivity -o portfolio/fixtures/usecase-1/ProjectActivity.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.ProjectEvent -o portfolio/fixtures/usecase-1/ProjectEvent.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.ProjectAsset -o portfolio/fixtures/usecase-1/ProjectAsset.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.GPPEmissionsSource -o portfolio/fixtures/usecase-1/GPPEmissionsSource.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.MultiAreaSource -o portfolio/fixtures/usecase-1/MultiAreaSource.json