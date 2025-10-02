.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/reeve_python_sdk.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/reeve_python_sdk
    .. image:: https://readthedocs.org/projects/reeve_python_sdk/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://reeve_python_sdk.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/reeve_python_sdk/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/reeve_python_sdk
    .. image:: https://img.shields.io/pypi/v/reeve_python_sdk.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/reeve_python_sdk/
    .. image:: https://img.shields.io/conda/vn/conda-forge/reeve_python_sdk.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/reeve_python_sdk
    .. image:: https://pepy.tech/badge/reeve_python_sdk/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/reeve_python_sdk
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/reeve_python_sdk

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

================
reeve_python_sdk
================


Python SDK for the Reeve API - A facial recognition service for person identification and verification.


This SDK provides a Python interface to interact with the Reeve API, enabling facial recognition capabilities including person management, face enrollment, face recognition, and face verification.

Features
========

* **Authentication** - Token-based authentication with Bearer JWT
* **Person Management** - Create, list, update, and delete persons
* **Face Management** - Add, list, and delete face images for persons
* **Face Recognition** - Identify unknown faces against enrolled persons
* **Face Verification** - Verify faces against specific persons or compare two faces

Installation
============

.. code-block:: bash

    pip install reeve_python_sdk

Development Installation
------------------------

.. code-block:: bash

    git clone https://github.com/qbit-codes/reeve-python-sdk.git
    cd reeve-python-sdk
    pip install -e .

Quick Start
===========

.. code-block:: python

    import asyncio
    from reeve_python_sdk import ReeveClient

    async def main():
        async with ReeveClient(
            api_url="https://api.reeve.example.com",
            api_key="your-api-key"
        ) as client:
            # Create a person
            person = await client.person.add(firstname="John", lastname="Doe")
            person_id = person["result"]["id"]

            # Add a face to the person
            with open("face.jpg", "rb") as f:
                await client.face.add(person_id=person_id, face=f)

            # Recognize a face
            with open("unknown_face.jpg", "rb") as f:
                result = await client.face.recognize(face=f)
                if result.get("result"):
                    print(f"Recognized: {result['result']['name']}")

    asyncio.run(main())

API Documentation
=================

Full API specification is available in ``docs/swagger.json``.

Testing
=======

Run tests with:

.. code-block:: bash

    pytest

Or with tox for comprehensive testing:

.. code-block:: bash

    tox


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
