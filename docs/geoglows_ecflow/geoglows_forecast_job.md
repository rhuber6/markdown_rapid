# geoglows_ecflow.geoglows_forecast_job

The geoglows_forecast_job module provides functions for creating the 
ecFlow job definition for running the GEOGLOWS forecast workflow.

## geoglows_ecflow.geoglows_forecast_job.create

The `geoglows_ecflow.geoglows_forecast_job.create` function creates the ecFlow job definition
for running the GEOGLOWS forecast workflow. It uses the rest of the functions in the module
to build the definition.

The return value is the [`ecflow.Defs`](https://ecflow.readthedocs.io/en/latest/python_api/Defs.html#ecflow.Defs) object
for the GEOGLOWS forecast workflow.  The function also creates the job definition file and the directory structure needed
by the job.  The job definition file and the directory structure will be created in the location specified in your `config.yml` file.

After using this function, the definition will be ready to be added to the ecFlow server. The following Python code shows how this function could be used.

```python
# Imports
from geoglows_ecflow import geoglows_forecast_job, client

# Create definition
geoglows_forecast_job.create("/path/to/config.yml")

# Add definition to server
client.add_definition("/path/to/definition.def", "<HOST>:<PORT>")

# Begin definition
client.begin("definition_name")
```

The code example assumes your config files are set up and your server is running.

## Family Definitions

The following functions are used to create the individual families that make up the ecFlow job definition.
The [`geoglows_ecflow.geoglows_forecast_job.create`](#geoglows_forecast_job_create_ref) function uses these 
functions to build the definition, so you do not need to call them directly when using that function.

.. automodule:: geoglows_ecflow.geoglows_forecast_job
    :members:
    :exclude-members: create

