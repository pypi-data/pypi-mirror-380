.. _examples:

========
Examples
========

Some basic example use cases
============================

All the example scripts used here are included in the sections below for illustration. Note that the --something argument is not known to esub. Hence, it is just passed to your executable.

Running 10 tasks in the active shell serially. Also runs the watchdog and merge functions as well as rerun-missing. The something argument gets passed to the executable::

    $ esub exec_example.py --tasks='0 > 10' --function=all --mode=run --something=10

Running 21 tasks in the active shell in parallel using 10 of the cores on the local machine (each core running 2 jobs except for one running 3).::

    $ esub exec_example.py --tasks='0 > 21' --main_n_cores_per_job=10 --function=main --mode=run-tasks --something=10

Running 5 MPI jobs locally in your active shell serially. Each job has 10 cores available::

    $ esub exec_example.py --tasks='0 > 5' --main_n_cores_per_job=10 --function=main --mode=run-mpi --something=10

Submitting 10 tasks to the LSF system splitted over 5 jobs (each job executes 2 tasks). Each job runs on 1 core. Also runs the watchdog, merge and rerun-missing functions. The job has a maximum runtime of 10h and allocates 20GB of RAM for each core::

    $ esub exec_example.py --tasks='0 > 10' --n_jobs=5 --main_n_cores_per_job=1 --function=all --mode=jobarray --something=10 --main_time=10 --main_memory=20000

Splitting 20 tasks over 3 jobs. Launches a jobarray with 3 jobs and each job has 5 cores available.::

    $ esub exec_example.py --tasks='0 >  20' --n_jobs=3 --main_n_cores_per_job=5 --function=main --mode=jobarray --something=10

Submitting 4 individual MPI job using 5 cores each.::

    $ esub exec_example.py --tasks='0 > 4' --n_jobs=4 --n_jobs=1 --main_n_cores_per_job=5 --function=main --mode=mpi --something=10

Running 21 tasks in the active shell in parallel using 10 of the cores on the local machine (each core running 2 jobs except for one running 3).::
A more complex example. Runs 21 tasks splitted over 5 jobs (jobarray) with each job having 10 cores, 5GB RAM and a maximum runtime of 5h. Additionally, runs a watchdog on 20 cores alongside the main jobs, having 10GB. After the main functions and the watchdog finish the rerun-missing function is triggered and potentially reruns failed jobs. When the rerun-missing is done the merge function is launched. The merge function is an MPI job with 100 cores and 4GB of RAM.

    $ esub exec_example.py --tasks='0 > 21' --n_jobs=5 --main_n_cores_per_job=10 --function=all --mode=jobarray --something=10 --main_memory=5000 --main_time=5 --watchdog_memory=10000 --watchdog_n_cores=10 --mpi_merge --merge_n_cores=100 --merge_memory=4000

Submitting a whole pipeline with an arbitrary number of jobs, dependencies and loops to the system::

    $ epipe pipeline_example.yaml

.. _exec_example:

esub executable example
=======================

Below is an example of an executable script that can be used by esub. Please
check the :ref:`usage` section to find an explanation for the different elements.

.. literalinclude:: ../example/exec_example.py
   :language: python

.. _pipeline_example:

epipe pipeline example
======================

Below is an example of an epipe pipeline file that can be used by epipe. Please
check the :ref:`usage` section to find an explanation for the different elements.

.. literalinclude:: ../example/pipeline_example.yml
   :language: bash

.. _source_example:

source file example
===================

This is an example of a source file (simple shell script) that can be used by
esub to set up the environement for the task that one wants to run.

.. literalinclude:: ../example/source_file_example.sh
   :language: bash
