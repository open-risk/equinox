#!/bin/bash
source ./venv/bin/activate

python3 manage.py loaddata portfolio/fixtures/usecase-3/Counterparty.json
python3 manage.py loaddata portfolio/fixtures/usecase-3/PowerPlant.json
python3 manage.py loaddata portfolio/fixtures/usecase-3/Certificate.json
