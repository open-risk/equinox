# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from pathlib import Path

# Directories

EQUINOX_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = os.path.join(EQUINOX_DIR, 'policy/fixtures/policy_data/')
ROOT_DIR = DATA_PATH

# Output files:
dataseries_file = ROOT_DIR + "dataseries.latest.json"
dimensions_file = ROOT_DIR + "dimensions.latest.json"
dataseries_update_file = ROOT_DIR + "dataseries.update.json"
metadata_file = ROOT_DIR + 'wikidata_extract_19_05_2020.json'

DATA_FILE = 'CAPMF.csv'
# DATA_FILE = 'OECD.ENV.EPI,DSD_CAPMF@DF_CAPMF,1.0+all.csv'
# DATA_FILE = 'OxCGRT_compact_national_v1.csv'
# DATA_FILE = 'Oxford_Policies_Report_Latest.csv'
# DATA_FILE = 'OxCGRT_latest.csv'

CSV_FILE_PATH = DATA_PATH + DATA_FILE

# Logfile
logfile_path = DATA_PATH + 'Logs/processing.log'

datatypes = {
    'country_region_code': str,
    'country_region': str,
    'sub_region_1': str,
    'sub_region_2': str,
    'retail_and_recreation_percent_change_from_baseline': float,
    'grocery_and_pharmacy_percent_change_from_baseline': float,
    'parks_percent_change_from_baseline': float,
    'transit_stations_percent_change_from_baseline': float,
    'workplaces_percent_change_from_baseline': float,
    'residential_percent_change_from_baseline': float
}

BACKUP_DIR = DATA_PATH + "Backups/"
LOG_DIR = DATA_PATH + "Logs/"
CURRENT_DIR = DATA_PATH + "CURRENT/"

# Input files:
dataflows_file = ROOT_DIR + "dataflows.latest.json"

# Log files
dataflow_update_log = "dataflow_update.log"
download_log = "dataseries_download.log"
parsing_log = "dataseries_parsing.log"
error_log = "error.log"

# Download mode parameters
# TODO If dataflows have changed, using Update mode throws directory error
# Select update mode
# Download_Mode = 'Update'
Download_Mode = 'Clean_Start'

# Select update type (D=Daily, A=All)
Download_Type = 'A'
# Download_Type = 'A'

CUTOFF_CHANGE_RED = 30  # 50% change day-on-day
CUTOFF_CHANGE_ORANGE = 20  # 25% change day-on-day
CUTOFF_CHANGE_YELLOW = 10  # 10% change day-on-day

# Statistics Strings
stat_strings = {
    'Max': 'Maximum',
    'Min': 'Minimum',
    'T': 'Latest',
    'Mean': 'Average'
}

# Activity names in sequence
activities = ['Retail and Recreation', 'Grocery and Pharmacy', 'Parks', 'Transit Stations', 'Workplaces',
              'Residential']

activities_short = ['RR', 'GP', 'PA', 'TS', 'WO', 'RE']

dataflows = ['AE', 'AF', 'AG', 'AO', 'AR', 'AT', 'AU', 'AW', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG',
             'BH', 'BJ', 'BO', 'BR', 'BS',
             'BW', 'BY', 'BZ', 'CA', 'CH', 'CI', 'CL', 'CM', 'CO',
             'CR', 'CV', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'EG', 'ES',
             'FI', 'FJ', 'FR', 'GA',
             'GB', 'GE', 'GH', 'GR', 'GT', 'GW', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL',
             'IN', 'IQ',
             'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB',
             'LI', 'LK', 'LT', 'LU', 'LV', 'LY', 'MD',
             'MK', 'ML', 'MM', 'MN', 'MT', 'MU', 'MX',
             'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'OM', 'PA',
             'PE', 'PG', 'PH',
             'PK', 'PL', 'PR', 'PT', 'PY', 'QA', 'RE', 'RO', 'RW', 'SA', 'SE', 'SG', 'SI', 'SK',
             'SN', 'SV', 'TG',
             'TH', 'TJ', 'TR', 'TT', 'TW', 'TZ', 'UG', 'US', 'UY', 'VE', 'VN',
             'YE', 'ZA', 'ZM', 'ZW',
             'EU']

country_dict = {'AE': 'United Arab Emirates', 'AF': 'Afghanistan', 'AG': 'Antigua and Barbuda', 'AO': 'Angola',
                'AR': 'Argentina', 'AT': 'Austria', 'AU': 'Australia', 'AW': 'Aruba', 'BA': 'Bosnia and Herzegovina',
                'BB': 'Barbados', 'BD': 'Bangladesh', 'BE': 'Belgium', 'BF': 'Burkina Faso', 'BG': 'Bulgaria',
                'BH': 'Bahrain', 'BJ': 'Benin', 'BO': 'Bolivia', 'BR': 'Brazil', 'BS': 'The Bahamas', 'BW': 'Botswana',
                'BY': 'Belarus', 'BZ': 'Belize', 'CA': 'Canada', 'CH': 'Switzerland', 'CI': "Côte d'Ivoire",
                'CL': 'Chile', 'CM': 'Cameroon', 'CN': 'China',
                'CO': 'Colombia', 'CR': 'Costa Rica', 'CV': 'Cape Verde',
                'CZ': 'Czechia', 'DE': 'Germany', 'DK': 'Denmark', 'DO': 'Dominican Republic', 'EC': 'Ecuador',
                'EE': 'Estonia', 'EG': 'Egypt', 'ES': 'Spain', 'FI': 'Finland', 'FJ': 'Fiji', 'FR': 'France',
                'GA': 'Gabon', 'GB': 'United Kingdom', 'GE': 'Georgia', 'GH': 'Ghana', 'GR': 'Greece',
                'GT': 'Guatemala', 'GW': 'Guinea-Bissau', 'HK': 'Hong Kong', 'HN': 'Honduras', 'HR': 'Croatia',
                'HT': 'Haiti', 'HU': 'Hungary', 'ID': 'Indonesia', 'IE': 'Ireland', 'IL': 'Israel', 'IN': 'India', 'IS' : 'Iceland',
                'IQ': 'Iraq', 'IT': 'Italy', 'JM': 'Jamaica', 'JO': 'Jordan', 'JP': 'Japan', 'KE': 'Kenya',
                'KG': 'Kyrgyzstan', 'KH': 'Cambodia', 'KR': 'South Korea', 'KW': 'Kuwait', 'KZ': 'Kazakhstan',
                'LA': 'Laos', 'LB': 'Lebanon', 'LI': 'Liechtenstein', 'LK': 'Sri Lanka', 'LT': 'Lithuania',
                'LU': 'Luxembourg', 'LV': 'Latvia', 'LY': 'Libya', 'MD': 'Moldova', 'MK': 'North Macedonia',
                'ML': 'Mali', 'MM': 'Myanmar (Burma)', 'MN': 'Mongolia', 'MT': 'Malta', 'MU': 'Mauritius',
                'MX': 'Mexico', 'MY': 'Malaysia', 'MZ': 'Mozambique', 'NA': 'Namibia', 'NE': 'Niger', 'NG': 'Nigeria',
                'NI': 'Nicaragua', 'NL': 'Netherlands', 'NO': 'Norway', 'NP': 'Nepal', 'NZ': 'New Zealand',
                'OM': 'Oman', 'PA': 'Panama', 'PE': 'Peru', 'PG': 'Papua New Guinea', 'PH': 'Philippines',
                'PK': 'Pakistan', 'PL': 'Poland', 'PR': 'Puerto Rico', 'PT': 'Portugal', 'PY': 'Paraguay',
                'QA': 'Qatar', 'RE': 'Réunion', 'RO': 'Romania', 'RW': 'Rwanda', 'RU': 'Russia',
                'SA': 'Saudi Arabia', 'SE': 'Sweden',
                'SG': 'Singapore', 'SI': 'Slovenia', 'SK': 'Slovakia', 'SN': 'Senegal', 'SV': 'El Salvador',
                'TG': 'Togo', 'TH': 'Thailand', 'TJ': 'Tajikistan', 'TR': 'Turkey', 'TT': 'Trinidad and Tobago',
                'TW': 'Taiwan', 'TZ': 'Tanzania', 'UG': 'Uganda', 'US': 'United States', 'UY': 'Uruguay',
                'VE': 'Venezuela', 'VN': 'Vietnam', 'YE': 'Yemen', 'ZA': 'South Africa', 'ZM': 'Zambia',
                'ZW': 'Zimbabwe', 'RS': 'Serbia',
                'EU': 'European Union'}

# the 28 countries of EU (keeping UK in)
eu_geolocations = {
    "AT": "Austria",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DE": "Germany",
    "DK": "Denmark",
    "EE": "Estonia",
    "ES": "Spain",
    "FI": "Finland",
    "FR": "France",
    "GB": "United Kingdom",
    "GR": "Greece",
    "HR": "Croatia",
    "HU": "Hungary",
    "IE": "Ireland",
    "IT": "Italy",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "MT": "Malta",
    "NL": "Netherlands",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "SE": "Sweden",
    "SI": "Slovenia",
    "SK": "Slovakia",
}

countryISOMapping = {
    "AFG": "AF",
    "ALA": "AX",
    "ALB": "AL",
    "DZA": "DZ",
    "ASM": "AS",
    "AND": "AD",
    "AGO": "AO",
    "AIA": "AI",
    "ATA": "AQ",
    "ATG": "AG",
    "ARG": "AR",
    "ARM": "AM",
    "ABW": "AW",
    "AUS": "AU",
    "AUT": "AT",
    "AZE": "AZ",
    "BHS": "BS",
    "BHR": "BH",
    "BGD": "BD",
    "BRB": "BB",
    "BLR": "BY",
    "BEL": "BE",
    "BLZ": "BZ",
    "BEN": "BJ",
    "BMU": "BM",
    "BTN": "BT",
    "BOL": "BO",
    "BIH": "BA",
    "BWA": "BW",
    "BVT": "BV",
    "BRA": "BR",
    "VGB": "VG",
    "IOT": "IO",
    "BRN": "BN",
    "BGR": "BG",
    "BFA": "BF",
    "BDI": "BI",
    "KHM": "KH",
    "CMR": "CM",
    "CAN": "CA",
    "CPV": "CV",
    "CYM": "KY",
    "CAF": "CF",
    "TCD": "TD",
    "CHL": "CL",
    "CHN": "CN",
    "HKG": "HK",
    "MAC": "MO",
    "CXR": "CX",
    "CCK": "CC",
    "COL": "CO",
    "COM": "KM",
    "COG": "CG",
    "COD": "CD",
    "COK": "CK",
    "CRI": "CR",
    "CIV": "CI",
    "HRV": "HR",
    "CUB": "CU",
    "CYP": "CY",
    "CZE": "CZ",
    "DNK": "DK",
    "DJI": "DJ",
    "DMA": "DM",
    "DOM": "DO",
    "ECU": "EC",
    "EGY": "EG",
    "SLV": "SV",
    "GNQ": "GQ",
    "ERI": "ER",
    "EST": "EE",
    "ETH": "ET",
    "FLK": "FK",
    "FRO": "FO",
    "FJI": "FJ",
    "FIN": "FI",
    "FRA": "FR",
    "GUF": "GF",
    "PYF": "PF",
    "ATF": "TF",
    "GAB": "GA",
    "GMB": "GM",
    "GEO": "GE",
    "DEU": "DE",
    "GHA": "GH",
    "GIB": "GI",
    "GRC": "GR",
    "GRL": "GL",
    "GRD": "GD",
    "GLP": "GP",
    "GUM": "GU",
    "GTM": "GT",
    "GGY": "GG",
    "GIN": "GN",
    "GNB": "GW",
    "GUY": "GY",
    "HTI": "HT",
    "HMD": "HM",
    "VAT": "VA",
    "HND": "HN",
    "HUN": "HU",
    "ISL": "IS",
    "IND": "IN",
    "IDN": "ID",
    "IRN": "IR",
    "IRQ": "IQ",
    "IRL": "IE",
    "IMN": "IM",
    "ISR": "IL",
    "ITA": "IT",
    "JAM": "JM",
    "JPN": "JP",
    "JEY": "JE",
    "JOR": "JO",
    "KAZ": "KZ",
    "KEN": "KE",
    "KIR": "KI",
    "PRK": "KP",
    "KOR": "KR",
    "KWT": "KW",
    "KGZ": "KG",
    "LAO": "LA",
    "LVA": "LV",
    "LBN": "LB",
    "LSO": "LS",
    "LBR": "LR",
    "LBY": "LY",
    "LIE": "LI",
    "LTU": "LT",
    "LUX": "LU",
    "MKD": "MK",
    "MDG": "MG",
    "MWI": "MW",
    "MYS": "MY",
    "MDV": "MV",
    "MLI": "ML",
    "MLT": "MT",
    "MHL": "MH",
    "MTQ": "MQ",
    "MRT": "MR",
    "MUS": "MU",
    "MYT": "YT",
    "MEX": "MX",
    "FSM": "FM",
    "MDA": "MD",
    "MCO": "MC",
    "MNG": "MN",
    "MNE": "ME",
    "MSR": "MS",
    "MAR": "MA",
    "MOZ": "MZ",
    "MMR": "MM",
    "NAM": "NA",
    "NRU": "NR",
    "NPL": "NP",
    "NLD": "NL",
    "ANT": "AN",
    "NCL": "NC",
    "NZL": "NZ",
    "NIC": "NI",
    "NER": "NE",
    "NGA": "NG",
    "NIU": "NU",
    "NFK": "NF",
    "MNP": "MP",
    "NOR": "NO",
    "OMN": "OM",
    "PAK": "PK",
    "PLW": "PW",
    "PSE": "PS",
    "PAN": "PA",
    "PNG": "PG",
    "PRY": "PY",
    "PER": "PE",
    "PHL": "PH",
    "PCN": "PN",
    "POL": "PL",
    "PRT": "PT",
    "PRI": "PR",
    "QAT": "QA",
    "REU": "RE",
    "ROU": "RO",
    "RUS": "RU",
    "RWA": "RW",
    "BLM": "BL",
    "SHN": "SH",
    "KNA": "KN",
    "LCA": "LC",
    "MAF": "MF",
    "SPM": "PM",
    "VCT": "VC",
    "WSM": "WS",
    "SMR": "SM",
    "STP": "ST",
    "SAU": "SA",
    "SEN": "SN",
    "SRB": "RS",
    "SYC": "SC",
    "SLE": "SL",
    "SGP": "SG",
    "SVK": "SK",
    "SVN": "SI",
    "SLB": "SB",
    "SOM": "SO",
    "ZAF": "ZA",
    "SGS": "GS",
    "SSD": "SS",
    "ESP": "ES",
    "LKA": "LK",
    "SDN": "SD",
    "SUR": "SR",
    "SJM": "SJ",
    "SWZ": "SZ",
    "SWE": "SE",
    "CHE": "CH",
    "SYR": "SY",
    "TWN": "TW",
    "TJK": "TJ",
    "TZA": "TZ",
    "THA": "TH",
    "TLS": "TL",
    "TGO": "TG",
    "TKL": "TK",
    "TON": "TO",
    "TTO": "TT",
    "TUN": "TN",
    "TUR": "TR",
    "TKM": "TM",
    "TCA": "TC",
    "TUV": "TV",
    "UGA": "UG",
    "UKR": "UA",
    "ARE": "AE",
    "GBR": "GB",
    "USA": "US",
    "UMI": "UM",
    "URY": "UY",
    "UZB": "UZ",
    "VUT": "VU",
    "VEN": "VE",
    "VNM": "VN",
    "VIR": "VI",
    "WLF": "WF",
    "ESH": "EH",
    "YEM": "YE",
    "ZMB": "ZM",
    "ZWE": "ZW",
    "XKX": "XK",
    "RKS": "XK",
    'EU27_2020': "EU"
}
