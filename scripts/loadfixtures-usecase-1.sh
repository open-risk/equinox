#!/bin/bash
source ./venv/bin/activate

python3 manage.py loaddata portfolio/fixtures/usecase-1/PortfolioManager.json
python3 manage.py loaddata portfolio/fixtures/usecase-1/ProjectPortfolio.json
python3 manage.py loaddata portfolio/fixtures/usecase-1/Project.json
python3 manage.py loaddata portfolio/fixtures/usecase-1/Contractor.json
python3 manage.py loaddata portfolio/fixtures/usecase-1/ProjectActivity.json
python3 manage.py loaddata portfolio/fixtures/usecase-1/ProjectAsset.json
python3 manage.py loaddata portfolio/fixtures/usecase-1/ProjectEvent.json
python3 manage.py loaddata portfolio/fixtures/usecase-1/GPPEmissionsSource.json
python3 manage.py loaddata portfolio/fixtures/usecase-1/MultiAreaSource.json