#!/bin/bash
source ./venv/bin/activate

python3 manage.py dumpdata --format=json --indent 2 portfolio.PortfolioManager -o portfolio/fixtures/usecase-2/PortfolioManager.json