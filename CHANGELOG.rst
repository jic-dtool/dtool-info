CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added
^^^^^

- ``-f/--full`` flag to ``dtool diff`` command to include checking of file
  hashes  
- ``-f/--full`` flag to ``dtool verify`` command to include checking of file
  hashes  


Changed
^^^^^^^

- ``dtool diff`` now only compares identifiers and file sizes by default
- ``dtool verify`` now only compares identifiers and file sizes by default


Deprecated
^^^^^^^^^^


Removed
^^^^^^^


Fixed
^^^^^


Security
^^^^^^^^


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
