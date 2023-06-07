Testing
=======================

.. note:: The testing framework is still under development. The following sub-section highlight the main approaches to testing the Equinox platform.

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

The Equinox User Manual has a number of concrete Use Cases that demonstrate the use of the platform in various sustainable portfolio management scenarios. From a technical perspective, loading the required datasets into the fresh installation performs a basic sanity test for the corresponding data models. Each use case can be loaded individually:


.. code:: bash

    bash loadfixtures-usecase-1.sh
    bash loadfixtures-usecase-2.sh
    bash loadfixtures-usecase-x.sh

