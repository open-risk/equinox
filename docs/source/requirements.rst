Requirements
=======================

Dependencies / Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: A Linux based system is recommended but with minor tweaks it is in principle also possible to deploy in Windows systems

- equinox requires a working Python 3 installation (including pip)
- Python >= 3.6
- Django >= 3.0
- The precise python library dependencies are listed in the :doc:`requirements`.txt file.
- equinox may work with earlier versions of these packages but this has not been tested
- A linux based system is recommended. Some tweaks are required for Windows but is in principle also possible to deploy there

.. note:: The current User Interface (UI) of equinox is desktop oriented and might not work properly in smaller (mobile) screens. Mobile clients are in the roadmap

Full List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List of python requirements. At this point the main dependencies are related to django and sphinx

::

    Django>=3.1.9
    django-debug-toolbar>=2.2.1
    django-grappelli>=2.14.2
    djangorestframework>=3.11.2
    drf-yasg>=1.20.0
    Sphinx>=3.1.1
    sphinx-rtd-theme>=0.5.0
