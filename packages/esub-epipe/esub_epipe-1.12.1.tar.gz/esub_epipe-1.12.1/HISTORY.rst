.. :changelog:

History
-------

1.12.1 (2025-09-29)
+++++++++++++++++++

* Fix: additional args are now also passed to the rerun_missing function

1.12.0 (2024-03.27)
+++++++++++++++++++

* resources for rerun_missing can be specified to be different from the resources of main (default is still the same resources as main)
* jobids are also printed when using epipe

1.11.1 (2023-10-13)
+++++++++++++++++++

* Fix: n_jobs is set automatically from the get_tasks function

1.11.0 (2023-09-01)
+++++++++++++++++++

* GPU support

1.10.3 (2023-07-27)
+++++++++++++++++++

* Fix: bug introduced in 1.10.1. 

1.10.2 (2023-07-03)
+++++++++++++++++++

* Fix: correct type of commandline arguments

1.10.1 (2023-06-30)
+++++++++++++++++++

* Fix: overriding the resource function parameters by commandline works now also when overwriting with the esub default value

1.10.0 (2022-12-19)
+++++++++++++++++++

* Full slurm support

1.6.12 (2022-06-03)
+++++++++++++++++++

* New logic. Introduced n_jobs / n_cores. 

* Increased flexibility. Main, merge and watchdog can now have multiple cores even if not in MPI mode.

1.6.11 (2022-03-21)
+++++++++++++++++++

* Adapted to new ekit.logger module
* New banner
* Updated documentation with new features

1.6.6 (2021-03-31)
++++++++++++++++++

* Many minor fixes
* Experimental SLURM support
* Check missing function support
* Some additional options for jobarrays

1.6.4 (2020-06-24)
++++++++++++++++++

* First release on PyPI.

