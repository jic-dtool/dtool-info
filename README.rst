dtool CLI commands for getting information about datasets
=========================================================

.. image:: https://badge.fury.io/py/dtool-info.svg
   :target: http://badge.fury.io/py/dtool-info
   :alt: PyPi package

.. image:: https://codecov.io/github/jic-dtool/dtool-info/coverage.svg?branch=main
   :target: https://codecov.io/github/jic-dtool/dtool-info?branch=main
   :alt: Code Coverage


Installation
------------

.. code-block:: bash

    pip install dtool-info


Example usage
-------------

Listing datasets in ``~/my_dataset`` directory::

    dtool ls ~/my_datasets

Getting summary information about a dataset::

    dtool summary ~/my_datasets/example_dataset

See the `dtool documentation <http://dtool.readthedocs.io>`_ for more detail.


Related packages
----------------

- `dtoolcore <https://github.com/jic-dtool/dtoolcore>`_
- `dtool-cli <https://github.com/jic-dtool/dtool-cli>`_
- `dtool-create <https://github.com/jic-dtool/dtool-create>`_
