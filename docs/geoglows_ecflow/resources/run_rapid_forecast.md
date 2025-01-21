geoglows_ecflow.resources.run_rapid_forecast
=============================================

Functions
---------

The function ``rapid_forecast_exec`` is run as a task in the ecFlow job.

The expected format for the **job_id** argument is **job_{vpu}_{ensemble_number}**
where vpu can be a number from 1 to 125 and ensemble_number can be a number from 1 to 52.
An example of a valid job_id is **"job_125_3"**.

Running as a Script
-------------------

When running ``run_rapid_forecast.py`` as a script, the following command line arguments are available:

* **workspace** - Path to suite home directory
* **job_id** - Job ID
* **rapid_executable_location** - Path to the RAPID executable

The following is an example of how `run_rapid_forecast.py` could be run as a script:

    python run_rapid_forecast.py /path/to/workspace job_125_3 /path/to/rapid/executable

When run as a script, :func:`rapid_forecast_exec <geoglows_ecflow.resources.run_rapid_forecast.rapid_forecast_exec>`
uses the paths formed by concatenating `"execute"` and `"subprocess"` to the given workspace for the `mp_execute_directory` 
and `subprocess_forecast_log_dir` arguments.
