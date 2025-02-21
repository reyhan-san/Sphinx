Sphinx Documentation
=====================

* Sphinx is a powerful documentation generator primarily used for Python projects but also supports other languages.
* It allows developers to write documentation in reStructuredText or Markdown and generates output formats like HTML.

How to install Sphinx and Sphinx-needs
---------------------------------------

.. code-block:: bash

    pip install sphinx
    pip install sphinx-needs # is an extension of sphinx


Activation of extensions
-------------------------

To activate various extensions in sphinx, we need to add them in the list of extensions in **conf.py** file

.. code-block:: python

    extensions = ['extension_1', 'extension_2']
