Asset
------------------------------
The Asset model holds asset specific data for each real asset, facility (plant, infrastructure etc) that is part of a **Project* (which may or may not be financed)

The assumption is that an Asset participates in only one Project at a time (if linked to a project object)

A special type of Asset is a **Building** (whether used for residential or commercial purposes).

.. note::  To further classify assets, the EBA Loan Asset Classes are used for correspondence, but those are *financial asset classes*.

.. automodule:: portfolio.Asset
   :members:
   :undoc-members:
   :noindex:

   .. automethod:: portfolio.Asset.ProjectAsset


   .. automethod:: portfolio.Asset.Building