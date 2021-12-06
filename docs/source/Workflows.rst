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
