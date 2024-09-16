#!/bin/bash

# Download Raw data from OxCGRT github repo (final datasets)
# https://github.com/OxCGRT/covid-policy-dataset/blob/main/data/OxCGRT_compact_national_v1.csv
# https://github.com/OxCGRT/covid-policy-dataset/blob/main/data/OxCGRT_compact_subnational_v1.csv

DAY=$(date -d "today" +"%d-%m-%Y")
FILE="Oxford_Policies_Report_"$DAY".csv"
cp OxCGRT_latest.csv ../../policy_data/Oxford_Policies_Report_Latest.csv
mv OxCGRT_latest.csv ../../policy_data/$FILE

echo "================================================================================" > ../../policy_data/Logs/processing.log
echo "Downloading Oxford dataset as of "$DAY >> ../../policy_data/Logs/processing.log
echo "================================================================================" >> ../../policy_data/Logs/processing.log
echo "Done!"