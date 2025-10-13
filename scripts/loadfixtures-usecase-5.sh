#!/bin/bash
source ./venv/bin/activate

python3 manage.py loaddata portfolio/fixtures/usecase-5/ProjectCategory.json
python3 manage.py loaddata portfolio/fixtures/usecase-5/PortfolioSnapshot.json
python3 manage.py loaddata portfolio/fixtures/usecase-5/ProjectPortfolio.json
python3 manage.py loaddata portfolio/fixtures/usecase-5/Project.json