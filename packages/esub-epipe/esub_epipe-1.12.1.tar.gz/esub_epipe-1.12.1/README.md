esub-epipe
==========

[![image](https://cosmo-gitlab.phys.ethz.ch/cosmo_public/esub-epipe/badges/master/pipeline.svg)](https://cosmo-gitlab.phys.ethz.ch/cosmo_public/esub-epipe)
[![image](http://img.shields.io/badge/arXiv-2006.12506-orange.svg?style=flat)](https://export.arxiv.org/abs/2006.12506)
[![image](http://img.shields.io/badge/arXiv-2110.10135-orange.svg?style=flat)](https://export.arxiv.org/abs/arXiv:2110.10135)
[![image](https://img.shields.io/badge/arXiv-2206.01450-orange)](https://export.arxiv.org/abs/arXiv:2206.01450)

esub-epipe is part of the Non-Gaussian Statistics Framework
([NGSF](https://cosmo-gitlab.phys.ethz.ch/cosmo_public/NGSF)).

If you use this package in your research please cite (Zuercher et al.
2020, [arXiv-2006.12506](https://arxiv.org/abs/2006.12506)), (Zuercher
et al. 2021, [arXiv-2110.10135](https://arxiv.org/abs/2110.10135)) and
(Zuercher et al. 2022,
[arXiv-2206.01450](https://arxiv.org/abs/2206.01450)).

[Source](https://cosmo-gitlab.phys.ethz.ch/cosmo_public/esub-epipe)

[Documentation](http://cosmo-docs.phys.ethz.ch/esub-epipe)

Introduction
------------

-   Are you tired of rewriting the same kind of submission scripts to
    sumbit your code to a computer cluster?
-   Do you not want to rewrite different versions of your code for
    serial, parallel or MPI execution, but instead use the same
    executable everytime?
-   Do you wish there would be an easy way to submit large numbers of
    dependent jobs to a computer cluster without writing the same kind
    of pipeline scripts and worrying about resource allocation every
    time?

If any of these points applies to you, you have come to the right place
:)

When using this package you will only need to write a single python
executable file. The same file can then be used to run your code
serially, in parallel or in an MPI environement on your local machine.
You can also use the same file to submit your code to a computer cluster
that runs IBMs LSF system or SLURM (experimental).

Even more, if you are building large pipelines with many dependent jobs,
or even tasks which have to be executed multiple times you will just
have to write a single YAML file in which you state what you want to run
and esub will submit all those jobs to the computer cluster such that
you can continue working on your amazing projects while waiting for the
results :)

Getting Started
---------------

The easiest and fastest way to learn about esub is to have a look at the
Examples Section in the documentation. If you wish to learn more also
have a look at the Usage Section in the documenation in which we
documented all the things you can do with esub.

Disclaimer
----------

At the moment only IBMs bsub and slurm systems is supported but we hope to include
other queing systems in the future.

Credits
-------

This package was created on May 12 2019 by Dominik Zuercher (PhD student
at ETH Zurich in Alexandre Refregiers [Cosmology Research
Group](https://cosmology.ethz.ch/)). It is inspired by the jobchainer
code written by Tomasz Kacprzak.

The package is maintained by Silvan Fischbacher
<silvanf@phys.ethz.ch>.

Contributing
------------

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.
