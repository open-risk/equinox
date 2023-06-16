#!/bin/bash
source ./venv/bin/activate

python3 manage.py dumpdata --format=json --indent 2 portfolio.ProjectCategory -o portfolio/fixtures/usecase-5/ProjectCategory.json
