.. _geoglows_ecflow.client:

geoglows_ecflow.client
======================

The client module provides functions for working with the ecFlow server.

geoglows_ecflow.client.ping
---------------------------

The ``geoglows_ecflow.client.ping`` function can be used to ping the ecFlow server.
This can be done to check if the ecFlow server is running.

.. autofunction:: geoglows_ecflow.client.ping

.. _client_add_definition_ref:

geoglows_ecflow.client.add_definition
-------------------------------------

The ``geoglows_ecflow.client.add_definition`` function can be used to add the GEOGLOWS definition to the ecFlow server.

.. autofunction:: geoglows_ecflow.client.add_definition

.. code-block:: python
    :emphasize-lines: 7,8

    # Imports
    from geoglows_ecflow import geoglows_forecast_job, client

    # Create definition
    geoglows_forecast_job.create("/path/to/config.yml")

    # Add definition to server
    client.add_definition("/path/to/definition.def", "<HOST>:<PORT>")

    # Begin definition
    client.begin("definition_name")

The code example assumes your config files are set up and your server is running.

geoglows_ecflow.client.begin
----------------------------

The ``geoglows_ecflow.client.begin`` function can be used to begin the GEOGLOWS definition on the ecFlow server.
The definition should first be added using :ref:`geoglows_ecflow.client.add_definition <client_add_definition_ref>`.

.. autofunction:: geoglows_ecflow.client.begin

.. code-block:: python
    :emphasize-lines: 10,11

    # Imports
    from geoglows_ecflow import geoglows_forecast_job, client

    # Create definition
    geoglows_forecast_job.create("/path/to/config.yml")

    # Add definition to server
    client.add_definition("/path/to/definition.def", "<HOST>:<PORT>")

    # Begin definition
    client.begin("definition_name")

The code example assumes your config files are set up and your server is running.