Project
------------------------------

The Project model is the fundamental building block for many Equinox workflows.

A Project is a container for a discrete portfolio management action. It may represent an evaluation workflow (assessment) of some real asset (e.g. a Data Center) following the GHG Protocol for Projects. It may be a fully fledged financing structure for Project Finance. It might also be a major procurement contract.

A Project expresses the intentions and objectives of the portfolio manager. It is distinct from specific Assets (Facilities, Buildings, Supplies) and Contracts (Loans, Procurement Contracts), though any of those might be part of the bundle comprising a Project.

It is also distinct from Companies and Counterparties (Borrowers, Operators, Contractors etc).

The term is meant to be _broader_ than Portfolio Asset, to enable the modelling of actual projects where some new asset is brought to life or gets a significant makeover.

.. automodule:: portfolio.Project
   :members:
   :undoc-members:
   :noindex:

   .. automethod:: portfolio.Project.Project