The equinox platform at a glance
============================================
**equinox** is a Python / Django powered sustainable portfolio management platform. It allows the collection and reporting of information relating to sustainable finance and any portfolio that has material sustainability characteristics

This documentation focuses on technical (software, installation, devops) characteristics of the equinox platform. Documentation of the user perspective (Functionality, workflows etc is provided `here <https://www.openriskmanagement.com/equinox>`_

Architecture
-------------

- Equinox is built as a web application framework adhering to REST principles. It make heavy use of Django's admin functionality.
- At the core of equinox are a number of **data models** that capture (allow persistence storage) of information about the different entities and concepts involved in Sustainable Finance and more specifically *Sustainable Portfolio Management*. These data models follow a logical pattern that is independent of any of the reference standards that are being implemented. This conceptual framework is documented in a number of `Open Risk White Papers <https://www.openriskmanagement.com/open-risk-white-papers/>`_.
- The platform functionality is delivered via a number of **apps** that process user inputs and portfolio data and deliver the required analyses and reports.

Data Layers
---------------
The data layer can be segmented into major categories:
- The *Physical Data Layer* that holds external information about physical aspects of assets, activities etc. and
- The *Socioeconomic Data Layer* that holds external information about economic agents and their economic / financial profiles
- The *Portfolio Management Layer* that overlays internal information about alternative scenarios, portfolio constraints, limits and targets.

Physical Data Layer
~~~~~~~~~~~~~~~~~~~~
- Assets are the core physical objects with attributable environmental impact (emissions) such as real estate, factories etc.
- An EmissionsSource is a discrete, defined GHG emissions source. It will typically be modelled as the product of an activity (e.g. production) and an emissions factor.

Socioeconomic Data Layer
~~~~~~~~~~~~~~~~~~~~~~~~~
- A Project Company is a Legal Entity that finances a Project
- Borrower is a Legal Counterparty to a Loan contract (may be natural person or corporate entity)
- A Loan is a borrowing made by a Project Company
- Contractors are Entities that are involved in delivering under contract to the Project Company
- Operators are Entities that are involved in operating under contract to the Project Company
- Sponsors are Entities that are involved in commissioning, guaranteeing or providing equity to the Project Company
- Stakeholders are other entities that are impacted or impacting by the Project Company
- Revenue focuses specifically on the business model of a Project Company
- Swap is an example of additional contract by the Project Company
- Scorecard collects relevant data to support the risk analysis of a Project Company

Project Management Data Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- A Project is the core portfolio management object. It belongs to a Project Category
- One or More Assets may be linked to a Project.
- A Project Activity is any activity with specific Sustainability impact (eg GHG reduction)
- A Primary Effect is the GHG impact of a Project Activity
- A Secondary Effect is the GHG impact of a Project Activity

Application Layer
------------------
The application layer helps users extract useful information from the database and perform the required analyses and reports. There are currently two major groups:

- Risk Analysis
- Results Explorer