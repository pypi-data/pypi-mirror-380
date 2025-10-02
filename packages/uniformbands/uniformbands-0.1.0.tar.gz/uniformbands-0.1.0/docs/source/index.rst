Uniform Bands
=============

**uniform_bands** is a simple Python package providing a function that computes uniform confidence bands from initial high probability lower and upper bounds using either the **uniform** or **student** method with theoretical covering guarantees.

Features
--------

- **Multiple Methods**: Choose between `"uniform"` and `"student"` bands depending on the desired statistical properties.
- **Input Flexibility**: Works with 2D or higher-dimensional arrays, supporting potentially different lower and upper bounds.

Installation
------------

You can install the package via pip:

.. code-block:: bash

   pip install uniformbands

API Reference
-------------

.. autofunction:: uniformbands.get_bands

