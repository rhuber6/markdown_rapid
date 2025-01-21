geoglows_ecflow.resources.generate_esri_table
=============================================

Functions
---------

The function ``postprocess_vpu_forecast_directory`` is run as a task in the ecFlow job.

.. automodule:: geoglows_ecflow.resources.generate_esri_table
    :members:
    :undoc-members:

Running as a Script
-------------------

When running ``generate_esri_table.py`` as a script, the following command line arguments are available:

* **workspace** - Path to the daily workspace directory, named in YYYYMMDDHH format
* **vpu** - ID number of vpu to process

The daily workspace directory should contain the following:

1. \*.runoff.nc IFS forecast files
2. An output directory of routed discharge netcdfs
3. symlinks to the rapid inputs and return periods directories

The following is an example of how `generate_esri_table.py` could be run as a script:

.. code-block:: bash

    python generate_esri_table.py /path/to/daily_forecast_workspace 713