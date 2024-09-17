#!/bin/bash
set -e

DJANGO_DIR=$(cd ../../..; pwd)
SCRIPT_DIR="/equinox/policy/fixtures/policy_data"
# DATA_DIR="/equinox/policy/fixtures/policy_data/dataflows"
DATA_DIR="../../fixtures/policy_data/dataflows"

echo "-> Step 1: Extracting Dataflows to Dict"
# python3 $DJANGO_DIR/manage.py extract_capmf_policy_dataflows
echo "-> Step 1: Successful"

echo "-> Step 2: Clean Old Dataflows"
# rm -rf $DATA_DIR/*
echo "-> Step 2: Successful"

echo "-> Step 3: Recreate Dataflow Dir"
# python3 $DJANGO_DIR/manage.py create_capmf_policy_dataflow_dir
echo "-> Step 3: Successful"

echo "-> Step 4: Extracting Dataseries"
# python3 $DJANGO_DIR/manage.py extract_capmf_policy_dataseries
echo "-> Step 4: Successful"

echo "-> Step 5: Create Dimensions Dictionary"
# python3 $DJANGO_DIR/manage.py create_capmf_policy_dimension_dict
echo "-> Step 5: Successful"

echo "-> Step 6: Process Policy Data"
# python3 $DJANGO_DIR/manage.py process_capmf_policy
echo "-> Step 6: Successful"

echo "-> Step 7: Create Dataflow Catalog"
# python3 $DJANGO_DIR/manage.py create_capmf_policy_dataflow_catalog
echo "-> Step 7: Successful"

echo "-> Step 8: Populate dataseries"
# python3 $DJANGO_DIR/manage.py populate_pd_dataseries
echo "-> Step 8: Successful"

echo "-> Step 9: Populate dataflows"
# python3 $DJANGO_DIR/manage.py populate_pd_dataflows
echo "-> Step 9: Successful"

echo "-> Step 10: Populate geoslices"
# python3 $DJANGO_DIR/manage.py populate_pd_geoslices
echo "-> Step 10: Successful"