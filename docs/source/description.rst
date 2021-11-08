The equinox platform
=====================

**equinox** is a Python / Django powered portfolio management platform that allows the collection and reporting of project finance risk and sustainability characteristics


Functionality
-------------
The equinox platform may be useful to financial industry users (portfolio managers, business analysts), data engineers and/or risk model developers. It currently targets the following use cases:

* Compile standardized credit risk score according to EBA Specialized Lending criteria for Project Finance
* PCAF Emissions accounting and reporting
* Equator Principles Reporting


.. note:: equinox is still in active development. The functionality of the platform will be significantly enhanced in future versions. If you have specific requests / ideas please raise them in our github repository.


Architecture
-------------

At the core of equinox are a number of data models that capture information about the different entities and concepts involved in Project Finance. These data models follow a logical pattern that is independent of any of the reference standards that are being implemented.


* Project is the core object. It belongs to a Project Category
* One or More Assets are major real items linked to the Project.
* Contractors are Entities that are involved in delivering the Project
* Operators are Entities that are involved in running the Project
* Sponsors are Entities that are involved in commissioning, guaranteeing or providing equity finance for the Project
* Stakeholders are other entities that are impacted or impacting the Project
* Primary Effect is the GHG impact of a Project Activity
* Secondary Effect is the GHG impact of a Project Activity
* Project Activity is a specific Sustainability impact (eg GHG reduction) of a Project
* Project Company is a Legal Entity that finances a Project
* Revenue focuses specifically on the business model of a Project Company
* A Loan is a borrowing made by a Project Company
* Swap is an example of additional contract by the Project Company
* Scorecard collects relevant data to support the risk analysis of a Project Company
