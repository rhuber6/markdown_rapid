geoglows_ecflow.resources.netcdf_to_zarr
========================================

Functions
---------

The function ``netcdf_forecasts_to_zarr`` is run as a task in the ecFlow job.

.. automodule:: geoglows_ecflow.resources.netcdf_to_zarr
    :members:
    :undoc-members:

Running as a Script
-------------------

When running ``netcdf_to_zarr.py`` as a script, the following command line argument is available:

* **workspace** - Path to the suite home directory

The following is an example of how `netcdf_to_zarr.py` could be run as a script:

.. code-block:: bash

    python netcdf_to_zarr.py /path/to/workspace