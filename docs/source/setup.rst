Installation
=======================
You can install and use the equinox platform in any computing system that supports *Python* **or** *Docker*.

.. note:: The current User Interface (UI) of equinox is desktop oriented and might not work properly in smaller (mobile) screens. Mobile clients are in the roadmap for future development

Installation via Docker
-----------------------
Installation via docker is recommended as a long term production option as it provides a streamlined and fast setup of an equinox instance. If you do not want to use docker scroll further down for :ref:`Manual installation from sources`


Step 1: Install Docker
~~~~~~~~~~~~~~~~~~~~~~~

.. note:: A working docker installation is required! Docker is available for many operating systems and platforms (Windows, MacOS, Linux, running on Intel/AMD or ARM chipsets among others). Follow the installation instructions `here <https://docs.docker.com/engine/install/>`_.

Once the installation is complete, make sure the docker service is running by testing that you can run the docker *'hello-world'* application.

.. code:: bash

    sudo service docker start
    sudo docker run hello-world

Now we are ready for the next step. You can either pull an image from Docker Hub or build a local image:

Step 2: Pull the equinox image from Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can pull and run the latest image from Docker Hub (This method is recommended if you do not want to mess at all with the source distribution).

.. note:: We are also providing images also for the ARM/v7 architecture (Raspberry Pi). Check the root of our docker hub for what is `currently available <https://hub.docker.com/u/openrisk>`_

Start by issuing a docker pull command:

.. code:: bash

    docker pull openrisk/equinox:latest
    docker run -p 8001:8080 openrisk/equinox:latest

If all went well you have now a running instance of equinox in your local machine. Access it by pointing your browser to ``http://localhost:8001`` and login with admin/admin credentials.

The API endpoints are accessible at ``http://localhost:8001/api``

.. note:: If you want to work with a different image check what is available at our `docker hub list <https://hub.docker.com/repository/docker/openrisk/equinox_web>`_

Step 2 (Alternative): Building a local docker image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Alternatively you can build your own *local* docker image of the equinox platfom. After you fetch the distribution from the `github repository <https://github.com/open-risk/equinox>`_ (as per manual installation instructions below), in the root directory of the distribution issue:

.. code:: bash

    cd equinox
    docker build -t equinox_web:latest .
    docker run -p 8001:8080 equinox_web:latest

Again, access the running instance of equinox by pointing your browser to ``http://localhost:8001`` and login with the default admin/admin credentials


Manual installation from sources
--------------------------------
The manual installation path is recommended if you want to use the latest release, dig into and inspect the equinox code base or if you want to contribute to equinox.



Step 1: Download the github sources to your preferred directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: bash

    git clone https://github.com/open-risk/equinox
    cd equinox


Step 2: Create a virtualenv for Python >= 3.9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is advisable to install the platform in a *virtualenv* so as not to interfere with your system's python distribution.

.. note:: If you do not have Python 3.9 please install it first into your system (either as a replacement of your previous 3.X version or as an alternative).

.. code:: bash

    virtualenv -p python3 venv
    source venv/bin/activate

Step 3: Install the required python dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The core dependency is Django and its own dependencies. In addition equinox uses the Jazzmin skin as the admin interface. Numpy and Pandas are also required.

.. code:: bash

    pip3 install -r requirements.txt

Step 4: Install the required system wide dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Equinox supports working with geospatial data and this requires some specific libraries

.. code:: bash

    sudo apt-get update && sudo apt-get install -y \
    gdal-bin \
    libgdal-dev \
    spatialite-bin\
    libsqlite3-mod-spatialite


.. note:: These are various C/C++ libraries that get installed system-wide (not in the virtualenv we create above). If you *don't* want to modify the host system you should go down the Docker route.

Step 5: Make the required django migrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The project is setup to use sqlite3 (spatialite). This step will ensure the database has the right tables.

.. code:: bash

    cd equinox
    python manage.py check
    python manage.py makemigrations
    python manage.py migrate

Step 6: Create a superuser.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suggestion: Use admin/admin as login/password as a reminder that this instance of equinox should NOT be used for sensitive!

.. code:: bash

    python3 createadmin

Step 7: Collect static files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is to ensure the interface will render properly

.. code:: bash

    python3 manage.py collectstatic --no-input

Step 8: Run the server.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default port is 8000 but if (by any chance) this port is already used in your computer there will be another assigned. Be sure to note the assigned port and use it instead.

.. code:: bash

    python3 manage.py runserver

Step 9: Login with your browser.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally in your favorite browser (e.g. Firefox from Mozilla), enter the url ``http://localhost:8000`` and login with admin/admin credentials.

.. note:: 8000 is the default port, if that is already in use, you can select an alternative one as follows:


.. code:: bash

    python3 manage.py runserver localhost:8081


Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~

The above steps are typical Django project installation steps. If you experience trouble at any point, the `Django online FAQ <https://docs.djangoproject.com/en/3.1/faq/>`_ should help you out.

.. Note:: The project uses an sqlite3 database for good reason! If things go pear-shaped with your database simply remove the file and start again.


We welcome your feedback and support. Please raise a `github ticket <https://github.com/open-risk/equinox/issues>`_ if you want to report a bug or need a new feature. For contributions check our Contribution and Code of Conduct docs.


Setup (Initialization)
=======================

Creating the database
----------------------

* load an emissions factor csv file into equinox
* create Project categories
* create GPC Sector categories

Let us insert some dummy data (optional). Without this the database will be completely empty.

.. code:: bash


    python createsectors.py
    bash loadfixtures.sh