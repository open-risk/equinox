#!/bin/bash
source ./venv/bin/activate
python3 manage.py loaddata start/fixtures/DocPage.json
python3 manage.py loaddata start/fixtures/ORMKeyword.json
python3 manage.py loaddata reference/fixtures/GPCSector.json