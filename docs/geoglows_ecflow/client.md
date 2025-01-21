.. _geoglows_ecflow.client:

geoglows_ecflow.client
======================

The client module provides functions for working with the ecFlow server.

geoglows_ecflow.client.ping
---------------------------

The ``geoglows_ecflow.client.ping`` function can be used to ping the ecFlow server.
This can be done to check if the ecFlow server is running.

geoglows_ecflow.client.add_definition
-------------------------------------

The ``geoglows_ecflow.client.add_definition`` function can be used to add the GEOGLOWS definition to the ecFlow server.

The code example assumes your config files are set up and your server is running.

geoglows_ecflow.client.begin
----------------------------

The ``geoglows_ecflow.client.begin`` function can be used to begin the GEOGLOWS definition on the ecFlow server.
The definition should first be added using :ref:`geoglows_ecflow.client.add_definition <client_add_definition_ref>`.

The code example assumes your config files are set up and your server is running.
