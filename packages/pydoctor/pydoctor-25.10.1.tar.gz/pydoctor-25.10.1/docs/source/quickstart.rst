Quick Start
===========

Installation
------------

Pydoctor can be installed from PyPI::

   $ pip install -U pydoctor

For Debian and derivatives, pydoctor can be installed with ``apt``::
   
   $ sudo apt install pydoctor

Example
-------

The following example uses most common options to generate pydoctor's own
API docs under the ``docs/api`` folder. It will add a link to the project website
in the header of each page, show a link to its source code beside every documented object
and resolve links to Python standard library objects.

The result looks like `this <api/index.html>`_.

::

    pydoctor \
        --project-name=pydoctor \
        --project-version=20.7.2 \
        --project-url=https://github.com/twisted/pydoctor/ \
        --html-viewsource-base=https://github.com/twisted/pydoctor/tree/20.7.2 \
        --html-base-url=https://pydoctor.readthedocs.io/en/latest/api \
        --html-output=docs/api \
        --docformat=epytext \
        --intersphinx=https://docs.python.org/3/objects.inv \
        ./pydoctor

.. note:: This example assume that you have cloned and installed ``pydoctor``
    and you are running the ``pydoctor`` build from Unix and the current directory
    is the root folder of the Python project.

.. tip:: First run pydoctor with ``--docformat=plaintext`` to focus on eventual
   python code parsing errors. Then, enable docstring parsing by selecting another `docformat <docformat/index.html>`_.

.. warning:: The ``--html-viewsource-base`` argument should point to a tag or a
    commit SHA rather than a branch since line numbers are not going to match otherwise
    when commits are added to the branch after the documentation has been published.

Publish your documentation
--------------------------

Output files are static HTML pages which require no extra server-side support.

Here is a `GitHub Action example <publish-github-action.html>`_ to automatically
publish your API documentation to your default GitHub Pages website.

Here is a `ReadTheDocs configuration <publish-readthedocs.html>`_ to automatically
publish your API documentation to ReadTheDocs

Return codes
------------

Pydoctor is a pretty verbose tool by default. It’s quite unlikely that you get a zero exit code on the first run. 
But don’t worry, pydoctor should have produced useful HTML pages no matter your project design or docstrings. 

Exit codes includes:

- ``0``: All docstrings are well formatted (warnings may be printed).
- ``1``: Pydoctor crashed with traceback (default Python behaviour).
- ``2``: Some docstrings are mal formatted.
- ``3``: Pydoctor detects some warnings and ``--warnings-as-errors`` is enabled.
