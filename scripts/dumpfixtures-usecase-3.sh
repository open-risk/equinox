#!/bin/bash
source ./venv/bin/activate

python3 manage.py dumpdata --format=json --indent 2 portfolio.Counterparty -o portfolio/fixtures/usecase-3/Counterparty.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.PowerPlant -o portfolio/fixtures/usecase-3/PowerPlant.json

python3 manage.py dumpdata --format=json --indent 2 portfolio.Certificate -o portfolio/fixtures/usecase-3/Certificate.json