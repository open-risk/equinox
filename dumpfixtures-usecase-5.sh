#!/bin/bash
source ./venv/bin/activate

python3 manage.py dumpdata --natural-foreign --format=json --indent 2 portfolio.ProjectCategory -o portfolio/fixtures/usecase-5/ProjectCategory.json
python3 manage.py dumpdata --natural-foreign --format=json --indent 2 portfolio.PortfolioSnapshot -o portfolio/fixtures/usecase-5/PortfolioSnapshot.json
python3 manage.py dumpdata --natural-foreign --format=json --indent 2 portfolio.ProjectPortfolio -o portfolio/fixtures/usecase-5/ProjectPortfolio.json
python3 manage.py dumpdata --natural-foreign --format=json --indent 2 portfolio.Project -o portfolio/fixtures/usecase-5/Project.json