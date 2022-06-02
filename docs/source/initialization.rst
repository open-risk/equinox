Initialization
==============================
A new equinox instance will have no data in the database. To get a feel for the platform it is advisable to load some of the datasets included in the distribution. A production oriented installation will have its own procedure for populating the database depending on the use cases supported and other requirements.

Here we discuss how to do demo oriented initializations both for a local installation from sources and a docker based installation respectively

.. note:: The data sets included in the distribution are for demonstration / testing purposes only, may be entirely random and/or incomplete and are not fit for any other use.


Loading Data into a local instance
------------------------------------------------
Inside your virtualenv issue:

.. code:: bash

    bash loadfixtures.sh

This will load a basic dummy dataset. At present this script is very basic.

.. note:: You can select any of the json files available within the fixtures directory, just edit the shell script.

.. code:: python

    python3 manage.py loaddata --format=json DESIRED_FIXTURE_FILE.json


Loading Data into a Docker instance
-----------------------------------------------
In a docker based installation simply execute the above inside your container. For example:

.. code:: bash

    docker exec -it 106bdb7e103f python3 manage.py loaddata --format=json ./equinox/fixtures/synthetic_data_1.json