CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added
^^^^^


Changed
^^^^^^^


Deprecated
^^^^^^^^^^


Removed
^^^^^^^


Fixed
^^^^^


Security
^^^^^^^^


[0.10.2] - 2018-07-26
---------------------

Fixed
^^^^^

- Fixed the documentation of the ``dtool verify`` command


[0.10.1] - 2018-05-18
---------------------

Fixed
^^^^^

- Defect where inventory html template is not included in Python package on PyPi


[0.10.0] - 2018-05-18
---------------------

Added
^^^^^

- ``dtool inventory`` command for generating csv/tsv/html inventories of collections
  of datasets

Fixed
^^^^^

- Fixed defect where running ``dtool item properties`` with an invalid identifier
  resulted in a KeyError exception being propagated to the user
- Fixed defect where ``dtool verify`` did not compare file sizes


[0.9.0] - 2018-02-05
--------------------

Added
^^^^^

- ``--quiet`` and ``--verbose`` options to ``dtool ls`` and improved formatting


[0.8.0] - 2018-01-18
--------------------

Changed
^^^^^^^

- Updated code to make use of dtoolcore version 3 API


[0.7.0] - 2017-10-23
--------------------

Added
^^^^^

- ``dtool overlay ls`` command to list the overlays in dataset
- ``dtool overlay show`` command to show the content of a specific overlay


[0.6.0] - 2017-10-09
--------------------

Added
^^^^^

- ``dtool ls`` can now be used to list the relpaths of the items in a dataset
- ``-f/--full`` flag to ``dtool diff`` command to include checking of file
  hashes  
- ``-f/--full`` flag to ``dtool verify`` command to include checking of file
  hashes  


Changed
^^^^^^^

- ``dtool ls`` now works with URIs rather than with prefix and storage arguments
- ``dtool diff`` now only compares identifiers and file sizes by default
- ``dtool verify`` now only compares identifiers and file sizes by default


[0.5.1] - 2017-10-04
--------------------

Fixed
^^^^^

- ``dtool ls`` now works with relative paths


[0.5.0] - 2017-09-25
--------------------

Added
^^^^^

- ``frozen_at`` to ``dtool summary`` command output


Changed
^^^^^^^

- Better validation of dataset URI; proto dataset now return informative error
  message instead of stack trace


[0.4.1] - 2017-09-19
--------------------

Fixed
^^^^^

- ``verify`` no longer hanging off ``dtool item`` command


[0.4.0] - 2017-09-19
--------------------

Added
^^^^^

- ``dtool identifiers`` command
- ``dtool summary`` command
- ``dtool verify`` command
- ``dtool item properties`` command
- ``dtool item fetch`` command


[0.3.0] - 2017-09-15
--------------------

Added
^^^^^

- ``dtool ls`` command


[0.2.0] - 2017-09-13
--------------------

Added
^^^^^

- Progress bar to ``dtool diff``


[0.1.0] - 2017-09-12
--------------------

Added
^^^^^

- ``dtool diff`` command
