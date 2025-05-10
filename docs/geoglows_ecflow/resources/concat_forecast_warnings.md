geoglows_ecflow.resources.concat_forecast_warnings
==================================================

Functions
---------

The function ``concat_warnings`` is run as a task in the ecFlow job.

Running as a Script
-------------------

When running ``concat_forecast_warnings.py`` as a script, the following command line argument is available:

* **workspace** - Path to the daily workspace directory, named in YYYYMMDDHH format

The daily workspace directory should contain the following:

1. \*.runoff.nc IFS forecast files
2. An output directory of routed discharge netcdfs
3. Symlinks to the rapid inputs and return periods directories

The following is an example of how `concat_forecast_warnings.py` could be run as a script:


    python concat_forecast_warnings.py /path/to/daily_forecast_workspace
