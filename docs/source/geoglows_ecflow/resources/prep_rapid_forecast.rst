geoglows_ecflow.resources.prep_rapid_forecast
=============================================

Functions
---------

The function ``rapid_forecast_preprocess`` is run as a task in the ecFlow job.

.. automodule:: geoglows_ecflow.resources.prep_rapid_forecast
    :members:
    :undoc-members:

Running as a Script
-------------------

When running ``prep_rapid_forecast.py`` as a script, the following command line argument is available:

* **workspace** - Path to workspace directory

The following is an example of how `prep_rapid_forecast.py` could be run as a script:

.. code-block:: bash

    python prep_rapid_forecast.py /path/to/workspace

When run as a script, :func:`rapid_forecast_preprocess <geoglows_ecflow.resources.prep_rapid_forecast.rapid_forecast_preprocess>`
uses the paths formed by concatenating `"input"` and `"output"` to the given workspace for the `rapid_input` and `rapid_output` arguments.
The path given as the workspace is used for the `runoff_dir` argument.