The PEFA Reference Data
========================

PEFA Reference Data provide energy flow reference data for European countries.

.. note:: This page is based on `Eurostat <https://ec.europa.eu/eurostat/cache/metadata/en/env_pefa_sims.htm>`_.

The physical energy flow accounts dataset (PEFA) is one module of the European environmental-economic accounts reported according to Regulation (EU) 691/2011 Annex VI.

The data set covers nationals economies as defined in national accounts (ESA 2010, paragraph 2.04), as well as its physical relation to economies in the rest of the world and the environment. The national economy is as defined in SEEA CF 2012 and National Accounts (NA); i.e. all economic activities undertaken by resident units (see ESA 2010, paragraph 2.04). Included are all EU Member States, EFTA countries, EU candidate countries and potential candidates.

The current overall time coverage is from 2000 to 2023 (not all countries have complete history).

PEFA Data Description
-------------------------

PEFA records the flows of energy (in terajoules) using the accounting framework of `physical supply and use tables <https://www.openriskmanual.org/wiki/Physical_Supply_and_Use_Tables>`_.

The unit of measure is one Terajoule (TJ)

This documentation refers to three PEFA datasets based on the same data collection. These datasets can be downloaded from Eurostat's `environmental datasets <https://ec.europa.eu/eurostat/web/environment/database>`_.

* Energy supply and use by NACE Rev. 2 activity (env_ac_pefasu), containing data on supply (table A), use (table B), transformation use (table B1), end use (table B2) and emission-relevant use (table C)
* Key indicators of physical energy flow accounts by NACE Rev. 2 activity (env_ac_pefa04)
* Physical energy flow accounts totals bridging to energy balances totals (env_ac_pefa05)


PEFA Data Dimensions
--------------------

1. Supply and Use tables (STK_FLOW)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The elements of this dimension are coming from the five questionnaire tables:

* energy supply (questionnaire table A);
* energy use (table B), of which
    * transformation use (table B1)
    * end use (table B2), and
* emission relevant use (table C).

2. Energy product (PROD_NRG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(not relevant for env_ac_pefa04 and env_ac_pefa05)

The flows of energy recorded in PEFA are broadly grouped into:

* flows from the environment to the economy (natural inputs),
* flows within the economy (energy products), and
* flows from the economy back to the environment (residuals),

Each of these generic groups is further broken down. In total this dimension distinguishes 31 items which are regulated in Commission Delegated Regulation (EU) 2016/172.


3. Classification of economic activities (NACE_R2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following NACE Rev.2 : (not relevant for env_ac_pefa05)

The supply and use of energy flows is broken down by NACE classification of economic activities. The aggregation level used is A*64 (i.e. 64 branches), fully compatible with ESA supply and use tables.

Furthermore, this dimension includes private households, accumulation (e.g. product inventories), the rest of the world economy for imports and exports, and the environment.

4. Indicators (INDIC_PEFA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(only relevant for env_ac_pefa04 and env_ac_pefa05)

Various key indicators that can be derived from the physical supply and use tables (env_ac_pefa04) and so-called 'bridging-items' (env_pefa_pefa05) which present the various elements explaining the differences between the national totals as reported by PEFA vis-a-vis the national totals as reported by Eurostat's energy balances.

5. Geopolitical entity (GEO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Covered are EU Member States, EFTA countries, candidate countries, and potential candidates.

6. Period of time (TIME)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All energy flow data are annual.

7. Unit (UNIT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All energy flows are reported in Terajoules.


Glossary
-----------------
A unit is said to be a resident unit of a country when it has a centre of economic interest in the economic territory of that country, that is, when it engages for an extended period (1 year or more) in economic activities in that territory.