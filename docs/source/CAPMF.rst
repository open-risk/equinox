The CAPMF Policy Data
======================

CAPMF Policy Data provide input for setting up and testing the Policy module of Equinox.

The internal representation is simplified / mapped as follows:

Dataflows
---------------------

The original single dataflow structure of the CAPMF data (**Climate actions and policies measurement framework** with ID OECD.ENV.EPI:DSD_CAPMF@DF_CAPMF(1.0)) is segmented into multiple "virtual" dataflows.

The new dataflows groups are by country:

* REF_AREA
* Reference area

Each dataseries belongs to one of the above.

Dataseries
---------------------

A measurement of a policy dataseries is identified by

* CLIM_ACT_POL, machine-oriented identifier
* Climate actions and policies, human readable form of identifier (text)


Dataseries Attributes
--------------------------

Each Dataseries has

* a set of associated attributes

  * Measurement Type
  * Frequency

* a temporally annotated value

  * Action
  * Units


Measurement Type
^^^^^^^^^^^^^^^^^^^^^^^^^

There are two measurement field types

* POL_STRINGENCY / Policy stringency (normalized ordinal scale)
* POL_COUNT	Adopted policies (count)

The ACTION field is uniformly set to I, hence discarded.

The FREQ field (Frequency of observation) is uniforly A (Annual) so discarded but imputed programmatically.


Data Values
^^^^^^^^^^^^^^^^^^^^^^^^^

TIME_PERIOD (Year) 1990 - 2022, always populated even if there is no data.

OBS_VALUE, the actual value (if measured)


Value Annotations
^^^^^^^^^^^^^^^^^^^^^^^^^

OBS_STATUS:

* A Normal value
* E Estimated value
* K Data included in another category
* M Missing value; data cannot exist
* N Not significant
* Q Missing value; suppressed

The UNIT_MEASURE (Unit of measure) field is either:

* 0_TO_10 (0-10 scale) for POL_STRINGENCY type
* PL (Policies) for POL_COUNT  type

Here redundant and ignored.

The UNIT_MULT field (Unit multiplier) is always set to 0 (Units) so discarded.

The DECIMALS (Decimals) fields (capturing numerical accuracy) is either 2 or 0

* POL_STRINGENCY -> 2 (not enforced)
* POL_COUNT	-> 0 (valid)


Policy Type Hierarchy
---------------------

The actual dataseries are at Level 4 of a hierarchy of policies (policy variables):

* Level1_BuildingBlock:	Level 1 (includes 3 building blocks)
* Level2_Module: Level 2 (includes 15 modules)
* Level3_Policy: Level 3 (includes 56 policies)
* Level4_PolicyVariable* Level 4 (includes 130 policy variables)

NB: In the first iteration we will flatten this hierarchy: all dataseries within a dataflow (country based) are grouped at the same level


