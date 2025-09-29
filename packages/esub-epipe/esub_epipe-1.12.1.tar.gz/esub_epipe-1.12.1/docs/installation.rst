============
Installation
============

Either install the PyPI version via pip::

    $ pip install esub-epipe

or install the development version from GitLab::

    $ git clone git@cosmo-gitlab.phys.ethz.ch:cosmo_public/esub-epipe.git
    $ cd esub-epipe
    $ python setup.py install

(optional) If run-mpi mode should be used also require a local openmpi environement.
Example of how to setup a working MPI environemnt (tested for Linux Ubuntu 18.04 LTS)::

    $ apt-get install lam-runtime mpich openmpi-bin slurm-wlm-torque
    $ pip install mpi4py
