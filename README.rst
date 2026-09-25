=========================
Sequana Pipeline Template
=========================

:version: 3.0

This repository is a Cookiecutter template to start a new `Sequana pipeline <https://sequana.readthedocs.io>`_ 
implementation from scratch.


Quickstart
----------

You first need to install the latest version of **cookiecutter** if you haven't installed it yet (requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Then, no need to install the sequana_pipeline_template package itself. You can call it directly from github as
follows::

    cookiecutter https://github.com/sequana/sequana_pipeline_template.git

you will be asked some questions in particular the name of the package. You can
change things later on. Except the name, most entries are populated in the
pyproject.toml file.

- The first question asks the name of the future pipeline. There is no strict
convention in Sequana but we usually use small caps and underscores to separate
words (e.g., sequana_rnaseq).

- The second question is the short description that will be added to your
pyproject.toml configuration file

- The third questions asked for keywords, also added to the pyproject.toml

That's it.


If your pipeline is called **varseq**, you should end up with a structure in the
directory **sequana_varseq** similar to::

    ├── test
    │   └── __init__.py
    ├── doc
    │   ├── conf.py
    │   ├── index.rst
    │   └── Makefile
    ├── README.rst
    ├── pyproject.toml
    ├── sequana_pipelines
    │   └── varseq
    │       ├── config.yaml
    │       ├── __init__.py
    │       ├── main.py
    │       ├── varseq.rules
    │       └── schema.yaml
    ├── environment.yml
    └── .github
        └── workflows
            ├── main.yml
            ├── pypi.yml
            └── apptainer.yml

You can install this new pipeline as follows::

    cd sequana_varseq
    pip install .

You can build the documentation as follows::

    cd sequana_varseq/doc
    make html  # under linux

Or test it::

    cd sequana_varseq
    pytest  # this tool (pytest) must be installed first (pip install pytest)

Of course, you now need to work a little bit by replacing the content of some
files with your code and/or documentation and tests.

The most important editing steps are then:

1. to edit the *config.yaml* and *varseq.rules* in the sequana_pipelines/varseq
   directory with your own snakemake pipeline and configuration file.
2. edit the main script **main.py** and adapt it to your needs. This will be the
   entry point of the user.
3. the documentation in ./doc
4. test in ./test
5. update the pyproject.toml file to add any external
   dependencies.

Once done, create a repository on https://github.com/sequana/sequana_varseq and
upload your files. 

This is not perfect and we will most probably edit this template in the future
to make it more robust and possibly add such features (help needed).

Once happy, you can create a local repository::

    git init

Create and switch to main branch: if you are on a different branch, 
you can create and switch to the main branch with::

    git checkout -b main

Add and commit changes: ensure you have at least one commit in your
repository. Make an initial commit::

    git add .
    git commit -m "Initial commit"

Push to Remote Repository: try pushing to the remote repository::

    git remote add origin git@github.com:sequana/your_repo
    git push -u origin main


Changelog

* v2: uses poetry
* v1: uses setuptools
