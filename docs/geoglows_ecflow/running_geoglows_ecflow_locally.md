Running geoglows_ecflow Locally
===============================

In order to run the geoglows_ecflow package you will need to 
create and set up the following configuration files.

* config.yml
* aws_config.yml
* local_ecflow_start.sh

These configuration files are detailed below.

geoglows_ecflow Configuration File (config.yml)
-----------------------------------------------


    # ecflow variables
    python_exec: /path/to/python
    ecflow_home: /path/to/ecflow_home
    ecflow_bin: /path/to/ecflow_client  # Required for local run
    workspace: /path/to/workspace
    local_run: false
    ecflow_entities:
    suite:
        name: geoglows_forecast
        logs: /path/to/suite_log
    family:
        - name: rapid_forecast_family
        suite: geoglows_forecast
        - name: init_flows_family
        suite: geoglows_forecast
        - name: esri_table_family
        suite: geoglows_forecast
        - name: nc_to_zarr_family
        suite: geoglows_forecast
        - name: archive_to_aws_family
        suite: geoglows_forecast
        - name: day_one_family
        suite: geoglows_forecast
    task:
        - name: forecast_prep_task
        variables:
            - PYSCRIPT
            - WORKSPACE
        suite: geoglows_forecast
        - name: esri_table_task
        variables:
            - PYSCRIPT
            - WORKSPACE
            - VPU
            - NCES_EXEC
        suite: geoglows_forecast
        - name: day_one_forecast_task
        variables:
            - PYSCRIPT
            - WORKSPACE
            - VPU
            - OUTPUT_DIR
        suite: geoglows_forecast
        - name: rapid_forecast_task
        variables:
            - PYSCRIPT
            - WORKSPACE
            - JOB_ID
            - RAPID_EXEC
        suite: geoglows_forecast
        - name: init_flows_task
        variables:
            - PYSCRIPT
            - WORKSPACE
            - VPU
        suite: geoglows_forecast
        - name: nc_to_zarr_task
        variables:
            - PYSCRIPT
            - WORKSPACE
            - VPU
        suite: geoglows_forecast
        - name: archive_to_aws_task
        variables:
            - PYSCRIPT
            - WORKSPACE
            - AWS_CONFIG
        suite: geoglows_forecast

    # rapid variables
    rapid_exec: /path/to/rapid_exec
    rapid_exec_dir: /path/to/rapid_exec_dir
    rapid_subprocess_dir: /path/to/rapid_subprocess_dir

    # forecast records variables
    forecast_records_dir: /path/to/forecast_records_dir

    # nco variables
    nces_exec: /path/to/nces_exec

    # aws variables
    aws_config: /path/to/aws_config.yml


AWS Configuration File (aws_config.yml)
---------------------------------------


    # aws credentials
    aws_access_key_id: AWS_ACCESS_KEY_ID
    aws_secret_access_key: AWS_SECRET_ACCESS_KEY

    # aws s3 bucket
    bucket_forecast_archive: S3_BUCKET_NAME
    bucket_maptable_archive: S3_BUCKET_NAME

Custom ecflow Server Start (local_ecflow_start.sh)
--------------------------------------------------


    #!/bin/bash
    export ECF_PORT=2500
    export ECF_HOST=localhost

    ecflow_start.sh -d /path/to/ecflow_home

Local Run Example
-----------------


    import subprocess
    from geoglows_ecflow import geoglows_forecast_job, client

    # Start server
    subprocess.run(['bash', '/path/to/local_server_start.sh'])

    # Create definition
    geoglows_forecast_job.create("/path/to/config.yml")

    # Add definition to server
    client.add_definition("/path/to/definition.def", "<HOST>:<PORT>")

    # Begin definition
    client.begin("definition_name")

Run Tests
---------

Run the following commands in your terminal


    cd geoglows_ecflow/
    pip install -e .[test]

    # run tests
    pytests tests/

    # run tests with coverage
    pytests --cov geoglows_ecflow tests/
