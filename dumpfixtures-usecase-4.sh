#!/bin/bash
source ./venv/bin/activate

python3 manage.py dumpdata --format=json --indent 2 reference.EmissionFactor -o reference/fixtures/usecase-4/EmissionFactor.json
