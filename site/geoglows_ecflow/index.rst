.. Root page for the geoglows_ecflow section of the documentation.

GEOGLOWS ECFLOW
================

The **geoglows_ecflow** package provides an easy way to create a GEOGLOWS RAPID forecast ecFlow job, submit the job to an ecFlow server, and run the job.


For instructions on how to install the package, see :ref:`geoglows_ecflow.installation`. 

For a guide on running geoglows_ecflow locally and setting up the configuration files see :ref:`geoglows_ecflow.running_geoglows_ecflow_locally`. 

If you are new to ecFlow, you may want to read the :ref:`geoglows_ecflow.ecflow` page to get an overview of the ecFlow concepts that the geoglows_ecflow package uses.

:ref:`geoglows_forecast_job <geoglows_ecflow.geoglows_forecast_job>` covers the functions and classes that the geoglows_ecflow package provides for creating the GEOGLOWS RAPID forecast job.

:ref:`client <geoglows_ecflow.client>` covers the functions that can be used to communicate with and submit jobs to the ecFlow server.

:ref:`utils <geoglows_ecflow.utils>` covers the utility functions that the geoglows_ecflow package uses.

The :ref:`resources <geoglows_ecflow.resources>` module holds the scripts that are run as tasks in the GEOGLOWS RAPID forecast job.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   ecflow
   running_geoglows_ecflow_locally
   geoglows_forecast_job
   client
   utils
   resources/index