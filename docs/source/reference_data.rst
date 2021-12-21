Reference Data
==========================
Equinox aims to integrate in the database a number reference databases that facilitate tasks of sustainable portfolio management. In the current focus such reference material concerns the emissions factors for various processes and activities.

Emissions Factors
---------------------------

Sources of emissions factors include:

* IPCC, Guidelines for National Greenhouse Gas Inventories (2006)
* IPCC, Emission Factor Database
* Country-specific emission factors from national inventories, reports, and guidelines
* Emission factors contained in the GHG Protocol calculation tools and guidance
* The GHG Protocol for Project Accounting and the related GHG Protocol Guidelines for Quantifying GHG Reductions from Grid-Connected Electricity Projects (if applicable)
* CDM databases and the CDM Tool to Calculate the Emission Factor for an Electricity System


The IPCC EFDB Database
---------------------------

The overall objective of the EFDB is to be an always up-to-date companion for the IPCC Guidelines for
National Greenhouse Gas Inventory that is seen as a worldwide resource for greenhouse gas inventory developers.

The EFDB has the objective to provide a variety of users, in particular the inventory compilers of the
Parties to the UNFCCC, with current and well-documented emission factors and other parameters, as well as to establish a communication platform for distributing and commenting on new research and
measurement data. Such a platform can provide an efficient means for experts and researchers to
disseminate new emission factors or other parameters in a timely manner to a worldwide audience of
potential end users. The EFDB is meant to be a recognised data repository where users can find
emission factors and other parameters with background documentation or technical references.

.. note:: As stated in the EFDB documentation, the responsibility of using this information appropriately will always remain with the users themselves.

EFDB Database Access
---------------------------
* Online access to the EFDB Database is available `here <https://www.ipcc-nggip.iges.or.jp/EFDB/find_ef.php?reset=>`_
* The EFDB Database is available for offline use in `IPCC Downloads <https://www.ipcc-nggip.iges.or.jp/EFDB/downloads.php>`_

Equinox incorporates the EFDB database in its entirety to enable internal use of its data.

EFDB Database Structure
---------------------------
The database structure is in the form of a long database table (~17K entries, one per emissions factor). For each emissions factor the following data are provided

* EF ID
* IPCC Categories
* Gases
* Fuel
* Type of parameter
* Description
* Technologies/Practices
* Parameters/Conditions
* Region/Regional Conditions
* Abatement/Control Technologies
* Other properties
* Value
* Unit
* Equation
* IPCC Worksheet
* Source of data
* Technical reference
* Abstract in English
* Uncertainty lower
* Uncertainty upper
* Data quality
* Data quality reference
* Other info on data quality
* Comments from the data provider
* Comments from others
* Data provider
* Link

EFDB Data Groups
------------------------
To improve the readability of the internal representation the data are grouped in the following categories:

* Identification of the Emissions Factor: (ID, Gas / Fuel, IPCC Category, Description)
* Practices/Conditions: (Regional or Technology Conditions and Details)
* Quantitative: (The value, range, units and uncertainty)
* Reference: (Data sources, references, links etc)
* Other: Any other attribute not fitting in the above



