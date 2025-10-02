Version 0.10 Updates
/////////////////////////


Version 0.10.11
===============

Changes
+++++++

- Requires ``covjsonkit>=0.0.28``


Version 0.10.10
===============

Changes
+++++++

- Use ``covjsonkit`` instead of ``ecccovjson`` to read coverage json data retrieved from the  :ref:`data-sources-polytope` source (:pr:`445`).


Version 0.10.9
===============

Fixes
++++++

- Fixed issue when setting up :ref:`data-sources-cds` source credentials via the prompt did not work.
- Fixed issue when setting up :ref:`data-sources-ads` source credentials via the prompt did not work.
- Increased ``cdsapi`` dependency to version 0.7.2 to be compatible with the new CDS/ADS services.


Version 0.10.8
===============

Fixes
++++++

- Fixed issue when tried to import "ecmwf-api-client" unnecessarily when the standalone MARS client was invoked for retrieving data from MARS.


Version 0.10.7
===============

Fixes
++++++

- When "param" or "shortName" in a namespace is "~" in the GRIB header :func:`metadata` now returns the value of "paramId" as a str for both these keys in the relevant namespaces. Previously "~" was returned.


Version 0.9.0

Version 0.10.4
===============

Fixes
++++++

- Fixed issue when pandas was unnecessarily imported (:pr:`468`).



Version 0.10.3
===============

Fixes
++++++

- Fixed issue when building a FieldCube crashed while generating error message due to missing "number" metadata key in input GRIB data (:pr:`456`).


Version 0.10.2
===============

Fixes
++++++

- Fixed issue when generating output with reduced Gaussian surface GRIB data did not work


Version 0.10.1
===============

Fixes
++++++

- Fixed memory leak in GRIB field metadata cache


Version 0.10.0
===============

New features
++++++++++++++++

- Refined :ref:`GRIB` data memory management when reading from a file (:pr:`428`). See :ref:`grib-memory` for an overview.
- Refined how GRIB the metadata object manages the GRIB handle (:pr:`430`). See the :ref:`/examples/grib_metadata_object.ipynb` notebook example for details.
- Added the ``index`` keyword argument for data subsetting to the following methods (:pr:`407`):

  -  field:  :meth:`~data.core.fieldlist.Field.to_numpy`, :meth:`~data.core.fieldlist.Field.to_array`, :meth:`~data.core.fieldlist.Field.data`, :meth:`~data.core.fieldlist.Field.to_latlon`, :meth:`~data.core.fieldlist.Field.to_points`
  - fieldlist:  :meth:`~data.core.fieldlist.FieldList.to_numpy`, :meth:`~data.core.fieldlist.FieldList.to_array`, :meth:`~data.core.fieldlist.FieldList.data`, :meth:`~data.core.fieldlist.FieldList.to_latlon`, :meth:`~data.core.fieldlist.FieldList.to_points`

- Removed normalisation of GRIB metadata keys when passed to methods like :meth:`~data.core.fieldlist.FieldList.sel`,  :meth:`~data.core.fieldlist.FieldList.isel`, :meth:`~data.core.fieldlist.FieldList.order_by` and :func:`unique_values` (:pr:`429`).

- Improved the implementation of :meth:`~data.core.fieldlist.FieldList.indices` and :meth:`~data.core.fieldlist.FieldList.index` (:pr:`436`)
- Changed the default to False for the ``progress_bar`` keyword argument in :func:`unique_values`

Installation
++++++++++++

Increased minimum version of `cdsapi` to be compatible with the new CDS beta services (:pr:`433`).
