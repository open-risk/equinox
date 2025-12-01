Testing
=======================

.. note:: The testing framework is still under development. The following sub-section highlights the main approaches to testing the Equinox platform.

Django Test Framework
-----------------------
Back-end aspects of the equinox platform are primarily tested using pytest.

.. code:: bash

    python manage.py test tests



Behavior Driven Development
----------------------------
Front-end aspects of the equinox platform are primarily tested using behave and selenium

.. code:: bash

    python manage.py behave


Testing Use Cases
------------------

The Equinox User Manual has a number of concrete Use Cases that demonstrate the use of the platform in various sustainable portfolio management scenarios.

From a technical perspective, loading the required datasets into a fresh Equinox installation performs a basic sanity test for all the corresponding data models. Each use case can be loaded individually:


.. code:: bash

    bash loadfixtures-usecase-1.sh
    bash loadfixtures-usecase-2.sh
    bash loadfixtures-usecase-x.sh


The correspondence of usecase tests with workflows is as follows:

.. list-table:: Use cases and associated workflows
   :widths: auto
   :header-rows: 1

   * - Usecase
     - Application
     - Workflow
     - Remarkt
   * - 0
     - Start (Front End)
     - N/A
     - Tests generic setup without user data
   * - 1
     - All
     - URL
     - N/A
   * - 2
     - All
     - URL
     - N/A
   * - 3
     - All
     - URL
     - N/A
   * - 4
     - All
     - URL
     - N/A
   * - 5
     - Portfolio
     - `EP Workflows <https://www.openriskmanagement.com/equinox/workflows/equator_principles/>`_
     - Equator Principles