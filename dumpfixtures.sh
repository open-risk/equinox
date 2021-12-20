#!/bin/bash
source ./venv/bin/activate
python3 manage.py dumpdata --format=json --indent 2 reference.GPCSector -o reference/fixtures/GPCSector.json