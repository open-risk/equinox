Pages
=====================
Users access and make use of the equinox through a number of "pages" that work similar to most web applications.



Portfolio Pages
------------------
Portfolio Pages are in general where the portfolio manager will work with concrete information.


Analysis Pages
----------------
Analysis Pages are the pages where the portfolio manager organizes and executes analyses that support sustainable portfolio management  objectives.

- Workflow: Store generic workflows (with foreign keys to other objects)
- Limitflow: Workflow specialized for the applications of limit framework
- Playbook: Store generic playbook (with foreign key to workflow)
- Objective: Store generic objective (with foreign key to playbook)

You can use controller to

* fetch and store workflow data from a opencpm instance (TBD)
* Orchestrate creditNet runs (parametric etc.)
* Orchestrate other model runs (TBD)


TBD: integrate offline configurations with DB based configurations
- CLI ADMIN functions delete_workflows playbooks etc.


controller knows about Objectives and Playbooks. It does not know about workflows except indirectly (through playbooks)

A number of classes emulate opencpm objects (simplified)

Objectives
~~~~~~~~~~~~~~~~

*Objectives* is the core organizational concept of Equinox. Under the Objectives approach, the credit portfolio management mission is decomposed into a number of distinct objectives (aims, targets) which in turn can be achieved by executing a sequence of tasks, denoted *playbooks* or *workflows*

In its simplest, the end result of fulfilling a portfolio management objective using Equinox is the production of a set of numbers (a Report) about various aspects of the portfolio. Working with visual data may also lead to *graphical reports*. More complex reports will involve composite workflows and storage of results (also for Audit purposes).

Objective Categories
~~~~~~~~~~~~~~~~~~~~

Provide *Portfolio Information*

In this category of objectives the goal is to obtain insights about the
current stat of the portfolio through views and summaries of portfolio
data.

Manage *Concentration Risk*

In this category the focus is on identifying weaknesses in the current
portfolio such as excessive concentrations to different risk factors

Guide *Origination* of new credit assets

This category ties up portfolio management with overall strategy for the
portfolio. Actual or hypothetical proposals are analyzed in the context
of the current portfolio

Manage *Risk Appetite*

This category links up portfolio management objectives with risk
constraints (for example exposure limits) imposed by internal or
external requirements and policies.

Manage *Risk Capital* and risk-adjusted returns

This category links the asset side (risky assets) with the liability
side (equity and debt instruments or guarantees). It is the most complex
objective class

Support for Objectives in Equinox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Equinox achieving the objectives is via one of the following
mechanisms:

-  Using **Built-in** (standardized) functionality in the various
   **Apps** that directly fulfills an objective without further
   requirements from the user
-  The more flexible **Playbook/Workflow** mechanism that enables full
   customization and extension of Equinox to incorporate arbitrarily
   complex sequences of calculations and report generation (but also
   requires deeper technical skills)

Examples
~~~~~~~~

-  A simple example of fulfilling a Portfolio Information objective is
   using a built-in method is to create a report on portfolio statistics
   using the Portfolio Explorer app
-  An example of using a workflow-based method to fulfill a
   concentration management objective is to compute a concentration
   index via one of the linked models available for that purpose

Keeping Record (Audit Trail)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Equinox can assist with reaching Portfolio Management objectives but it
does not know what those objectives are, cannot verify whether they are
appropriate or whether they have been achieved! The functionality that
is provided in this direction is a faithful audit trail (record of
calculations) that have been performed (The Results Explorer App)


Playbooks
~~~~~~~~~~~~~~~~
1) one or more Workflows along with a list of Workflow-Deltas. Each delta produces a new result
2) a selection of post-processing operations on the results of the workflow execution. Each post-processing operation selects a number of results and produces an new playbook result

1) Workflow Deltas
* A workflow-delta is a modification to a JSON object based Workflow
* It identifies the field to modify and the new value
* The list is an explicit enumeration (but can become a function)
* It must produce a workflow that validates the JSON schema

2) Post Processing Operations
* Take a set of existing results and create summaries / estimates / plots
* Eg. Compare two model results
* Compute rate of convergence
* Compare two portfolio outcomes

Reporting Pages
-----------------
Reporting Pages are where portfolio managers generate information material to communicate to other stakeholders.

Reports are the primary means to disseminate results of analyses outside the Equinox environment

The Objectives and Results Explorer provides the functionality for extracting business information from the Equinox system. The type of analysis and reporting provided in this section is linked to the objectives set out in the Sustainable Portfolio Management mandate.