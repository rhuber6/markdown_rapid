geoglows_ecflow.resources.day_one_forecast
==========================================

Functions
---------

The function ``postprocess_vpu`` is the main function that is run for this task in the ecFlow job.
It utilizes the other functions in this module as helpers to accomplish its task.

.. automodule:: geoglows_ecflow.resources.day_one_forecast
    :members: postprocess_vpu
    :undoc-members:

.. automodule:: geoglows_ecflow.resources.day_one_forecast
    :members: merge_forecast_qout_files, check_for_return_period_flow, get_time_of_first_exceedance, update_forecast_records
    :undoc-members:

Running as a Script
-------------------

When running ``day_one_forecast.py`` as a script, the following command line arguments are available:

* **workspace** - Path to the daily workspace directory
* **vpu** - VPU number
* **output_dir** - Path to the forecast records output directory

The directory specified by the **workspace** argument should contain directories
named `input`, `output`, and `return_periods_dir`. These directories should hold the inputs,
outputs, and return period files for RAPID, respectively.

The following is an example of how `day_one_forecast.py` could be run as a script:

.. code-block:: bash

    python day_one_forecast.py /path/to/daily_workspace 713 /path/to/forecast_records_output_directory
