# core-ftp
===============================================================================

This project/library provides a comprehensive set of common components and 
interfaces designed to facilitate and streamline FTP connections, 
ensuring efficient communication and data transfer...

===============================================================================

.. image:: https://img.shields.io/pypi/pyversions/core-ftp.svg
    :target: https://pypi.org/project/core-ftp/
    :alt: Python Versions

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://gitlab.com/bytecode-solutions/core/core-ftp/-/blob/main/LICENSE
    :alt: License

.. image:: https://gitlab.com/bytecode-solutions/core/core-ftp/badges/release/pipeline.svg
    :target: https://gitlab.com/bytecode-solutions/core/core-ftp/-/pipelines
    :alt: Pipeline Status

.. image:: https://readthedocs.org/projects/core-ftp/badge/?version=latest
    :target: https://readthedocs.org/projects/core-ftp/
    :alt: Docs Status

.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security

|

Execution Environment
---------------------------------------

Install libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    pip install --upgrade pip 
    pip install virtualenv
..

Create the Python Virtual Environment.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    virtualenv --python={{python-version}} .venv
    virtualenv --python=python3.11 .venv
..

Activate the Virtual Environment.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    source .venv/bin/activate
..

Install required libraries.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    pip install .
..

Check tests and coverage.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    python manager.py run-tests
    python manager.py run-coverage
..


How to Use
---------------------------------------

Installation.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    pip install core-ftp
..

Examples.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from core_ftp.clients.sftp import SftpClient

    with SftpClient("test.rebex.net", 22, "demo", "password") as client:
        for x in client.list_files("/"):
            print(x)
..

.. code-block:: python

    from core_ftp.clients.sftp import SftpClient

    with SftpClient(
            host="localhost", port=23,
            user="foo", private_key_path="key_path") as client:

        for x in client.list_files("/"):
            print(x)
..

Docker
---------------------------------------

You can use docker to create an SFTP server to test the client using the functional 
tests via command `python manager.py run-tests --test-type functional --pattern "*.py"` and the following docker
image: <atmoz/sftp> (https://hub.docker.com/r/atmoz/sftp/).

Authentication via user & password.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    docker run \
      -v ./tests/resources/upload:/home/foo/upload:rw \
      -p 22:22 -d atmoz/sftp foo:pass:::upload
..

Authentication via SSH key.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    docker run \
      -v ./tests/resources/ssh_keys/id_rsa.pub:/home/foo/.ssh/keys/id_rsa.pub:ro \
      -v ./tests/resources/upload:/home/foo/upload:rw \
      -p 23:22 -d atmoz/sftp foo::1001
..
