#!/bin/bash
source ./venv/bin/activate

python manage.py dumpdata --format=json --indent 2 portfolio.operator portfolio.projectcompany portfolio.datacenter portfolio.datacentercampus portfolio.projectportfolio portfolio.portfoliosnapshot provenance.agent > fixtures-test.json
