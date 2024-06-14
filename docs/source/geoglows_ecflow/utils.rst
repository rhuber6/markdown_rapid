.. _geoglows_ecflow.utils:

geoglows_ecflow.utils
=====================

This module contains useful helper functions that are used by the geoglows_ecflow package.
It's likely that you won't need to use any of these functions yourself when using the geoglows_ecflow package.

.. _utils_load_config_ref:

geoglows_ecflow.utils.load_config
----------------------------------

The ``geoglows_ecflow.utils.load_config`` function is used to load the :ref:`config.yml <config_yml_ref>` configuration file that is used by the geoglows_ecflow package.

.. autofunction:: geoglows_ecflow.utils.load_config

The code below shows a brief example of how to use the ``geoglows_ecflow.utils.load_config`` function.
It also demonstrates how to access some of the configuration values that are loaded from the :ref:`config.yml <config_yml_ref>` configuration file.

.. code-block:: python

    from geoglows_ecflow.utils import load_config

    # Read in the configuration file
    config = load_config('path/to/config.yml')

    # Access some of the configuration values
    python_exec = config["python_exec"]
    ecflow_home = config["ecflow_home"]
    ecflow_bin = config.get("ecflow_bin")
    workspace = config["workspace"]
    local_run = config.get("local_run")
    ecflow_entities = config["ecflow_entities"]
    ecflow_suite = config["ecflow_entities"]["suite"]["name"]
    ...

geoglows_ecflow.utils.prepare_dir_structure
-------------------------------------------

The ``geoglows_ecflow.utils.prepare_dir_structure`` function is used to create the directory structure that is
used by the ecFlow job.

.. autofunction:: geoglows_ecflow.utils.prepare_dir_structure

The created directory structure will be based on the entities passed to the function through the entities argument.
Normally, this structure is defined in the :ref:`config.yml <config_yml_ref>` configuration file and can be loaded in using the 
:ref:`geoglows_ecflow.utils.load_config <utils_load_config_ref>` function.

geoglows_ecflow.utils.create_symlinks_for_tasks
-----------------------------------------------

.. autofunction:: geoglows_ecflow.utils.create_symlinks_for_tasks

geoglows_ecflow.utils.create_symlinks_for_family_tasks
------------------------------------------------------

The ``geoglows_ecflow.utils.create_symlinks_for_family_tasks`` function is used to create
symlinks for the tasks within a specific family.

.. autofunction:: geoglows_ecflow.utils.create_symlinks_for_family_tasks

It is used by geoglows_ecflow to create symlinks for all tasks as illustrated
in the code example below:

.. code-block:: python

    # Imports
    from geoglows_ecflow.utils import create_symlinks_for_family_tasks

    # Create symlinks for all tasks
    task_family_list = [
        (rapid_task_name, rapid_family_name),
        (init_flows_task_name, init_flows_family_name),
        (esri_table_task_name, esri_table_family_name),
        (nc_to_zarr_task_name, nc_to_zarr_family_name),
        (day_one_task_name, day_one_family_name),
        (aws_task_name, aws_family_name),
    ]

    create_symlinks_for_family_tasks(ecflow_home, ecflow_suite, task_family_list, vpu_list)

The variables ``ecflow_home`` and ``ecflow_suite`` both get their values from the :ref:`config.yml <config_yml_ref>` configuration file.
The geoglows_ecflow package finds the names that populate the ``task_family_list`` from the :ref:`config.yml <config_yml_ref>` configuration file as well.
The values in the variable ``vpu_list`` can be retrieved by using the :func:`geoglows_ecflow.resources.helper_functions.get_valid_vpucode_list` function.

geoglows_ecflow.utils.add_variables
-----------------------------------

The ``geoglows_ecflow.utils.add_variables`` function is a convienence function that can be used to add variables to an ecFlow entity.

.. autofunction:: geoglows_ecflow.utils.add_variables

Suites, families, and tasks can all have variables added to them. This function allows you to add multiple variables to an entity
with a single function call.

.. code-block:: python

    # Imports
    from ecflow import Suite
    from geoglows_ecflow.utils import add_variables

    # Create our suite
    suite = ecflow.Suite("s1")

    # Add variables to the suite using add_variables
    suite_variables = {
        "ECF_INCLUDE": 'path/to/directory',
        "WORKSPACE": 'path/to/workspace/'
    }

    add_variables(suite, suite_variables)

geoglows_ecflow.utils.validate
-------------------------------

The ``geoglows_ecflow.utils.validate`` function can be used to validate your job definition.

.. autofunction:: geoglows_ecflow.utils.validate
