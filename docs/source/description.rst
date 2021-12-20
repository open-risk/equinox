The equinox platform
=====================
**equinox** is a Python / Django powered portfolio management platform that allows the collection and reporting of project finance risk and sustainability characteristics


Architecture
-------------

* At the core of equinox are a number of data models that capture information about the different entities and concepts involved in Sustainable Finance. These data models follow a logical pattern that is independent of any of the reference standards or eventual applications that are being implemented.
* Functionality is delivered via a number of apps that process user inputs and portfolio data and deliver analyses and reports


Data Layer
---------------
The data layer can be segmented into two major categories: The Physical Layer that holds information about physical aspects of assets, activities etc. and the "socioeconomic" layer that holds information about entities, economic and financial aspects etc.


Physical Layer
~~~~~~~~~~~~~~~~~~
* Project is the core object. It belongs to a Project Category
* One or More Assets are major real items linked to the Project.
* Primary Effect is the GHG impact of a Project Activity
* Secondary Effect is the GHG impact of a Project Activity
* Project Activity is a specific Sustainability impact (eg GHG reduction) of a Project

Socioeconomic Layer
~~~~~~~~~~~~~~~~~~~~~
* Project Company is a Legal Entity that finances a Project
* Contractors are Entities that are involved in delivering under contract to the Project Company
* Operators are Entities that are involved in operating under contract to the Project Company
* Sponsors are Entities that are involved in commissioning, guaranteeing or providing equity to the Project Company
* Stakeholders are other entities that are impacted or impacting by the Project Company
* Revenue focuses specifically on the business model of a Project Company
* A Loan is a borrowing made by a Project Company
* Swap is an example of additional contract by the Project Company
* Scorecard collects relevant data to support the risk analysis of a Project Company

Application Layer
------------------
The application layer help the user extract useful information from the database and perform the required analyses and reports

* Asset Manager
* Risk Analysis
* Results Explorer
