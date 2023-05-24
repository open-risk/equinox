The equinox platform at a glance
============================================

**equinox** is a Python / Django powered sustainable portfolio management platform. It allows the collection and reporting of information relating to sustainable finance and more broadly any portfolio of financial contracts or instruments that has material sustainability related characteristics

This documentation focuses on technical (software, installation, devops) characteristics of the equinox platform. Documentation of the user perspective (Functionality, workflows etc is provided `here <https://www.openriskmanagement.com/equinox>`_

Architecture
-------------

- Equinox is built as a Web application platform adhering to REST principles. It makes heavy use of Django's admin functionalities and adds a number specialized apps that enable various portfolio management workflows.
- At the core of equinox are a number of sustainability and portfolio management related **data models** that capture (allow the persistence storage) of information. This information concerns the various different entities and concepts involved in Sustainable Finance and in particular *Sustainable Portfolio Management*. The equinox data models follow a logical pattern that is independent of any of the reference sustainability standards that are being implemented. The conceptual framework underpinning the data model is documented in a number of `Open Risk White Papers <https://www.openriskmanagement.com/open-risk-white-papers/>`_.
- The platform functionality is delivered via a number of **apps**. Each one of those apps process user inputs and portfolio data and delivers the required analyses and reports. They are documented individually in respective chapters.

Data Layers
---------------
The equinox data layer can be segmented into several major categories:
- The *Physical Data Layer* that holds information about physical aspects of assets, activities etc. This concerns mostly information typically external to the portfolio manager.
- The *Socioeconomic Data Layer* that holds information about economic agents and their economic and financial profiles. This too concerns information external to the portfolio manager.
- The *Portfolio Management Layer* that overlays internal portfolio management information about sustainability scenarios, portfolio constraints, limits and targets etc.


Lets look at those layers in some more detail. Each one is implemented as as set of specialized data models, with corresponding database schema.

Physical Data Layer
~~~~~~~~~~~~~~~~~~~~
- *Assets* such as real estate, factories etc. are the core physical objects documented. They have attributable environmental impact (for example GHG emissions)
- An *EmissionsSource* is a discrete, defined GHG emissions source linked to an asset. It will typically be modeled quantitatively as the product of an activity (e.g. production volume of some good or service) and an emissions factor. Sources come in large numbers of different types, depending on the application context.

Socioeconomic Data Layer
~~~~~~~~~~~~~~~~~~~~~~~~~

- A *Project Company* is a Legal Entity that finances a Project. It is the main abstraction to represent businesses or other entities that the portfolio manager maintains economic relationships with (provides financing, is trading in good or services etc).
- A *Borrower* is a Legal Counterparty to a Loan contract (may be natural person or corporate entity)'.
- A *Loan* is a borrowing made by a Project Company'.
- *Contractors* are Entities that are involved in delivering (under contract) goods or services to the Project Company'.
- *Operators* are Entities that are involved in operating (under contract) some aspect of the Project Company'.
- *Sponsors* are Entities that are involved in commissioning, guaranteeing or providing equity (and related financial instruments) to the Project Company'
- *Stakeholders* are other entities that are impacted and have a relation with the Project Company without belonging to any of the explicit categories.
- *Revenue* focuses specifically on the business model of a Project Company.
- A *Swap* is an example of a specialized financial contract by the Project Company.
- A *Scorecard* collects relevant data to support the risk analysis of a Project Company.

Project Management Data Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- A *Project* is the core portfolio management object, the individual investment, procurement or other economic relation of the portfolio manager. with an external economic agent. A Project can be classificed using a flexible *Project Category* taxonomy.
- One or More Assets (with the associated environmental impact as captured by different types of sources) may be linked to a Project.
- A *Project Activity* is any business activity with specific Sustainability impact (e.g., towards GHG reduction).
- A *Primary Effect* is the main GHG impact of a Project Activity
- A *Secondary Effect* is any additional GHG impact of a Project Activity

Application Layer
-----------------------
The application layer helps users extract useful information from the database and perform the required portfolio management analyses and reports. There are currently two major groups of application data:

Risk Analysis
~~~~~~~~~~~~~~

The **Risk App** is the main interface for *risk analytics* functionality (the calculation or risk metrics, KPI's and other indicators on the basis of portfolio and potentially other external data)

Reporting
~~~~~~~~~~~

Reports are the primary means to disseminate results of analyses outside the Equinox environment. The **Reporting App** is the primary means of generating reports.