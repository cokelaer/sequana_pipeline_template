
.. image:: https://badge.fury.io/py/sequana-{{cookiecutter.name}}.svg
     :target: https://pypi.python.org/pypi/sequana_{{cookiecutter.name}}

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
    :target: http://joss.theoj.org/papers/10.21105/joss.00352
    :alt: JOSS (journal of open source software) DOI

.. image:: https://github.com/sequana/sequana_{{cookiecutter.name}}/actions/workflows/main.yml/badge.svg
   :target: https://github.com/sequana/sequana_{{cookiecutter.name}}/actions/workflows/main.yml

.. image:: https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg
    :target: https://pypi.python.org/pypi/sequana_{{cookiecutter.name}}
    :alt: Python 3.10 | 3.11 | 3.12



This is the **{{cookiecutter.name}}** pipeline from the `Sequana <https://sequana.readthedocs.io>`_ project

:Overview: TODO 
:Input: TODO
:Output: TODO
:Status: draft
:Citation: Cokelaer et al, (2017), ‘Sequana’: a Set of Snakemake NGS pipelines, Journal of Open Source Software, 2(16), 352, JOSS DOI doi:10.21105/joss.00352


Installation
~~~~~~~~~~~~

sequana_{{cookiecutter.name}} requires Python 3.10+. Install the package as follows::

    pip install sequana_{{cookiecutter.name}} --upgrade

You will need third-party tools. Please see below for details.

Usage
~~~~~

::

    sequana_{{cookiecutter.name}} --help
    sequana_{{cookiecutter.name}} --input-directory DATAPATH

This creates a directory with the pipeline and configuration file. You can then execute the pipeline::

    cd {{cookiecutter.name}}
    sh {{cookiecutter.name}}.sh  # for a local run

This launches a snakemake pipeline. If you are familiar with snakemake, you can 
retrieve the pipeline itself and its configuration files and then execute the pipeline yourself with specific parameters::

    snakemake -s {{cookiecutter.name}}.rules -c config.yaml --cores 4 --stats stats.txt

Or use `sequanix <https://sequana.readthedocs.io/en/main/sequanix.html>`_ interface.


Usage with apptainer / singularity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With Apptainer, initiate the working directory as follows (images are stored in the specified directory)::

    sequana_{{cookiecutter.name}} --apptainer-prefix ~/.sequana/apptainers

and then::

    cd {{cookiecutter.name}}
    sh {{cookiecutter.name}}.sh

if you decide to use snakemake manually, do not forget to add apptainer options::

    snakemake -s {{cookiecutter.name}}.rules -c config.yaml --cores 4 --stats stats.txt --software-deployment-method apptainer --apptainer-prefix ~/.sequana/apptainers --apptainer-args "-B /home:/home"

By default, the home is already set for you. Additional binding path can be set using environment variables e.g.::

    export APPTAINER_BINDPATH=" -B /pasteur"

Requirements
~~~~~~~~~~~~

This pipeline requires the following executable(s):

- TODO

.. image:: https://raw.githubusercontent.com/sequana/sequana_{{cookiecutter.name}}/main/sequana_pipelines/{{cookiecutter.name}}/dag.png


Details
~~~~~~~~~

This pipeline runs **{{cookiecutter.name}}** in parallel on the input fastq files (paired or not). 
A brief sequana summary report is also produced.


Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the `latest documented configuration file <https://raw.githubusercontent.com/sequana/sequana_{{cookiecutter.name}}/main/sequana_pipelines/{{cookiecutter.name}}/config.yaml>`_
to be used with the pipeline. Each rule used in the pipeline may have a section in the configuration file. 

Changelog
~~~~~~~~~

========= ====================================================================
Version   Description
========= ====================================================================
3.0.0     **Modern cookiecutter template with Poetry, Python 3.10+, GitHub Actions**
0.0.1     **First release.**
========= ====================================================================


Contribute & Code of Conduct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To contribute to this project, please take a look at the 
`Contributing Guidelines <https://github.com/sequana/sequana/blob/main/CONTRIBUTING.rst>`_ first. Please note that this project is released with a 
`Code of Conduct <https://github.com/sequana/sequana/blob/main/CONDUCT.md>`_. By contributing to this project, you agree to abide by its terms.

