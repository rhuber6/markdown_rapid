geoglows_ecflow.resources.compute_init_flows
============================================

Functions
---------

The function ``compute_all_rapid_init_flows`` is the main function that is run for this task in the ecFlow job.
It utilizes the other functions and classes in this module as helpers to accomplish its task.

.. autofunction:: geoglows_ecflow.resources.compute_init_flows.compute_all_rapid_init_flows

.. autofunction:: geoglows_ecflow.resources.compute_init_flows.compute_init_rapid_flows

Classes
-------

.. autoclass:: geoglows_ecflow.resources.compute_init_flows.StreamNetworkInitializer
    :members:
    :undoc-members:
    :private-members:

.. autoclass:: geoglows_ecflow.resources.compute_init_flows.StreamSegment
    :members:
    :undoc-members:
    :private-members:

Private Functions
-----------------

.. autofunction:: geoglows_ecflow.resources.compute_init_flows._cleanup_past_qinit

Running as a Script
-------------------

When running ``compute_init_flows.py`` as a script, the following command line arguments are available:

* **workspace** - Path to rapid_run.json base directory
* **vpu** - VPU number to process

The following is an example of how `compute_init_flows.py` could be run as a script:

.. code-block:: bash

    python compute_init_flows.py /path/to/workspace 713