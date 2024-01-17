Installation
=======================

You can install and use the Equinox platform in any computing system that either directly supports a *Python* environment **or** does so indirectly (via *Docker*). Here you can find alternative ways to install Equinox.

Installation via Docker
-----------------------

Installation via docker is recommended as a long term production option as it provides a streamlined and fast setup of an equinox instance. If you do not want to use docker scroll further down for :ref:`Manual installation from sources`


Step 1: Install Docker
~~~~~~~~~~~~~~~~~~~~~~~

.. note:: A working Docker installation is required! Docker is available for many operating systems and platforms (Windows, MacOS, Linux, running on Intel/AMD or ARM chipsets among others). Follow the installation instructions `here <https://docs.docker.com/engine/install/>`_.

Once the docker installation is complete, make sure the docker service is running by testing that you can run a docker *'hello-world'* application.

.. code:: bash

    sudo service docker start
    sudo docker run hello-world

Now we are ready for the next step. You can either pull an image from our Docker Hub account or build a local docker image from the source code:

Step 2: Pull the equinox image from Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can pull and run the latest image from Docker Hub (This method is recommended if you do not want to work with the source distribution).

.. note:: The latest image is circa 1.5GB

.. note:: We are also providing images also for the ARM/v7 architecture (Raspberry Pi). Check the root of our docker hub for what is `currently available <https://hub.docker.com/u/openrisk>`_

Start by issuing a docker pull command:

.. code:: bash

    docker pull openrisk/equinox:latest
    docker run -p 8001:8080 openrisk/equinox:latest

If all went well you now have a running instance of equinox in your local machine. Access it by pointing your browser to ``http://localhost:8001`` and login with admin/admin credentials.

The Equinox API endpoints are accessible at ``http://localhost:8001/api``

.. note:: If you want to work with a different image check what is available at our `docker hub list <https://hub.docker.com/repository/docker/openrisk/equinox_web>`_


Step 2 (Alternative Path): Building a local docker image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Alternatively you can build your own *local* docker image of the equinox platform. After you fetch the distribution from the `github repository <https://github.com/open-risk/equinox>`_ (as per manual installation instructions below), in the root directory of the distribution issue the following commands:

.. code:: bash

    cd equinox
    docker build -t equinox_web:latest .
    docker run -p 8001:8080 equinox_web:latest

Again, access the running instance of equinox by pointing your browser to ``http://localhost:8001`` and login with the default admin/admin credentials


Manual installation from sources
--------------------------------

The manual installation path is recommended if you want to use the latest release, dig into and inspect the equinox code base and/or if you want to contribute to equinox development.


Step 1: Download the github sources to your preferred directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: For this step you need to have *git* installed in your system.

.. code:: bash

    git clone https://github.com/open-risk/equinox
    cd equinox


Step 2: Create a virtualenv for Python >= 3.10.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is advisable to run the equinox platform via a Python *virtualenv* so as not to interfere with your system's own Python distribution.

.. note:: If you do not have Python 3.10 please install it first into your system (either as a replacement of your previous 3.X version or as an alternative).

.. code:: bash

    virtualenv -p python3 venv
    source venv/bin/activate

Step 3: Install the required python dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The core dependency of Equinox is *Django* (and its own dependencies). In addition Equinox uses the *Jazzmin* skin as the admin interface and various Python libraries such as *Numpy* and *Pandas* are also required for calculations. You install all dependencies issuing the following:

.. code:: bash

    pip3 install -r requirements.txt

Step 4: Install the required system-wide dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Equinox supports working with *geospatial data* and this requires specific C/C++ libraries that must be installed system-wide.

The default Equinox project is setup to use sqlite3 (spatialite). On a linux system with apt installed issue the following:

.. note:: In other Linux distributions replace apt with your package manager

.. code:: bash

    sudo apt-get update && sudo apt-get install -y \
    gdal-bin \
    libgdal-dev \
    spatialite-bin\
    libsqlite3-mod-spatialite

.. note:: The above are geospatial C/C++ libraries that are installed system-wide (not in the isolated virtualenv we created above). If you *don not* want to modify the host system on which you install equinox you should go down the Docker route describe in the previous installation paths.

To use postgres/postgis as a backend, install first the following at the system level (assuming here the 14 version of postgres):

.. code:: bash

    sudo apt-get libpq-dev postgresql postgresql-contrib
    sudo apt-get install python3-psycopg2
    sudo apt install postgresql-14-postgis-scripts
    sudo apt install postgresql-plpython3-14

Subsequently setup the appropriate user / databases as follows (names are indicative):

.. code:: sql

   CREATE DATABASE equinox;
   CREATE USER equinoxuser WITH PASSWORD 'equinoxuser';
   ALTER ROLE equinoxuser SUPERUSER;
   ALTER ROLE equinoxuser SET client_encoding TO 'utf8';
   ALTER ROLE equinoxuser SET default_transaction_isolation TO 'read committed';
   ALTER ROLE equinoxuser SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE equinox TO equinoxuser;

Modify the database configuration section of the settings.py file

.. code:: python

    DATABASES = {
        # 'default': {
        #     "ENGINE": "django.contrib.gis.db.backends.spatialite",
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # }
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'equinox',
            'USER': 'equinoxuser',
            'PASSWORD': 'equinoxuser',
            'HOST': 'localhost',
            'PORT': '5433',
        }
    }

Step 5: Make the required Django migrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This step will ensure the database has the right tables. Issue the following command lines:

.. code:: bash

    cd equinox
    python manage.py check
    python manage.py makemigrations
    python manage.py migrate

Step 6: Create a superuser.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the next step we create an Equinox superuser (administrator).

.. note:: Suggestion: Use admin/admin as temporary login/password. A reminder that this instance of Equinox should NOT be used for production!

.. code:: bash

    python3 createadmin.py

Step 7: Collect static files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next step ensures that the Equinox user interface will render properly

.. code:: bash

    python3 manage.py collectstatic --no-input

Step 8: Run the Equinox server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are now ready to launch the Equinox web server. The default port is 8000 but if (by any chance) this port is already used in your computer there will be another assigned. Be sure to note the assigned port and use it instead.

.. code:: bash

    python3 manage.py runserver

Step 9: Login with your browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally!, in your favorite browser, enter the url ``http://localhost:8000`` and login with the admin/admin credentials (or any other credentials you used in step 6 above.

.. note:: 8000 is the default port, if that is already in use, you can select an alternative one as follows:

.. code:: bash

    python3 manage.py runserver localhost:8081


Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~

The above steps are typical Django project installation steps. If you experience an issue that appears to be generic Django trouble at any point, the `Django online FAQ <https://docs.djangoproject.com/en/4.2/faq/>`_ should help you out.

.. note:: The Equinox project uses an sqlite3 database for good reason! If things go pear-shaped with your database simply remove the sqlite file and start again.

.. warning:: The current User Interface (UI) of equinox is desktop oriented and might not work properly in smaller (mobile) screens. Mobile clients are in the roadmap for future development.

We welcome your feedback and support. Please raise a `github ticket <https://github.com/open-risk/equinox/issues>`_ if you want to report a bug or need a new feature.

For contributions check our Contribution and Code of Conduct docs.

Setup (Initialization)
=======================

The basic installation of equinox creates an empty database. If you want to initialize the database with some indicative data follow the steps below:

Creating the database
----------------------

* Create Project categories
* Create GPC Sector categories
* Load various fixtures with model data
* Load an emissions factor csv file into equinox

Let us insert some dummy data (optional). Without this the database will be completely empty.

.. code:: bash

    python3 createsectors.py
    python3 createcategories.py
    bash loadfixtures.sh