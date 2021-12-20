Workflows
-------------
Workflows is how Equinox orchestrates any desired calculation. This page provides a basic introduction. Further information is available in the use manual

Workflows are the primary means to get things done within Equinox. Each workflow is essentially a specification to get a set of data, perform some desired operations and do something with the output.

Models
~~~~~~~~~~~~~~~
- Workflow: Store generic workflows (with foreign keys to other objects)
- Limitflow: Workflow specialized for the applications of limit framework
- Playbook: Store generic playbook (with foreign key to workflow)
- Objective: Store generic objective (with foreign key to playbook)


Workflow Types
~~~~~~~~~~~~~~~~~~~

There are three key workflow types:

* A batch workflow that performs a single calculation and permanently stores the result </li>
* An interactive workflow that allows interactively working with models and data without saving the results
* A parametric batch workflow that performs a family of operations (for example a parameter space survey to allow some optimization) and stores the results


Workflow Components
~~~~~~~~~~~~~~~~~~~~~~

There are four workflow components:

* The portfolio data to be used
* The model to be used (if applicable)
* The model configuration parameters
* The model data parameters


Playbook
~~~~~~~~~~~~~~~
A Playbook is

1. one or more Workflows along with a list of Workflow-Deltas. Each delta produces a new result
2. a selection of post-processing operations on the results of the workflow execution. Each post-processing operation selects a number of results and produces an new playbook result


The Workflow Concept
~~~~~~~~~~~~~~~~~~~~

Workflows are a powerful means to expose the **full** functionality of
Equinox allowing near limitless customization. Defining new workflows
does require higher technical level and familiarity with the platform.
But once defined, workflows are the building blocks of Playbooks.
In turn, one or more Playbooks allow you to achieve your Credit
Portfolio Management Objectives

Standard tasks can usually be achieved easier and faster with the
*built-in* functionalities of the various apps.

Each workflow is:

-  a specification of a set of input data
-  the performance of some desired operation / calculations and finally
-  where applicable, the storage of the output

Workflow Classifications
~~~~~~~~~~~~~~~~~~~~~~~~

A good way to understand the nature of workflows is to examine some
possible classifications:

By Portfolio Management Objective
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Workflows can be classified according to the desired portfolio
management objective. This classification aims to help use Equinox in
the most effective way to perform the portfolio management mandate

By Content Type
^^^^^^^^^^^^^^^

Workflows can also be classified according to the type of content
produced. In logical order:

#. A **Modelling task** that performs a customized model calculation. We
   call modelling workflows simply *Workflows* as they are the only type
   of workflow that actually modifies the Equinox database (creates and
   inserts new data)
#. A **Reporting task** that produces a customized report for human
   consumption (e.g. in html or pdf format). We call reporting workflows
   simply *Reports*
#. A **Visualization task** that produces a customized visualization
   (either a static graphic or a dynamic visualization offering some
   embedded interactivity). We call visualization workflows simply
   *Visualizations*

A mentioned above, not all Equinox functionality is available or optimal
to use via Workflows. The most important category of tasks currently not
available via Workflows are operations modifying the Portfolio
databases.

By Interaction Style
^^^^^^^^^^^^^^^^^^^^^^^^^

Finally, workflows can also be classified according to the type of
interaction with the user:

-  A **Batch workflow** that performs a calculation and permanently
   stores the results in the database. This is the recommended mode for
   formal tasks performed using Equinox. Batch workflows may be a single
   calculation or a family of operations (for example a parameter space
   survey to allow some optimization) and stores the results
-  An **Interactive workflow** that allows *interactively* working with
   models and data. This is the recommended mode for exploratory
   analysis, training and other tasks that require significant
   experimentation. This mode does not (normally) save results in
   permanent storage (does not create a log file).

Modelling workflow Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are four modelling workflow components:

-  The model to be used (currently only one model per calculation)
-  The portfolio data to be used
-  The model configuration parameters
-  The model data parameters


