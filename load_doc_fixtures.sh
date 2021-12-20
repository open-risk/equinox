#!/bin/bash
source ./venv/bin/activate
python3 manage.py loaddata start/fixtures/DocPage.json
