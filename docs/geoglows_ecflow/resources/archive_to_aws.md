geoglows_ecflow.resources.archive_to_aws
========================================

Functions
---------

The function ``upload_to_s3`` is the main function that is run for this task in the ecFlow job.

For information on the expected contents of the AWS config file see :ref:`aws_config.yml <aws_config_yml_ref>`.

Running as a Script
-------------------

When running ``archive_to_aws.py`` as a script, the following command line arguments are available:

* **workspace** - Path to suite home directory
* **aws_config_file** - Path to AWS config file (:ref:`aws_config.yml <aws_config_yml_ref>`)

The following is an example of how `archive_to_aws.py` could be run as a script:


    python archive_to_aws.py /path/to/workspace /path/to/aws_config.yml
