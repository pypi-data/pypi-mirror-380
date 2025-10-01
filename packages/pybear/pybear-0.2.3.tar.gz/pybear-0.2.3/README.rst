pybear
======

|Tests|
|Coverage|
|Test Status 313|
|Test Status 312|
|Test Status 311|
|Test Status 310|

.. |Tests| image:: https://raw.githubusercontent.com/PylarBear/pybear/main/.github/badges/tests-badge.svg
   :target: https://github.com/PylarBear/pybear/actions

.. |Coverage| image:: https://raw.githubusercontent.com/PylarBear/pybear/main/.github/badges/coverage-badge.svg
   :target: https://github.com/PylarBear/pybear/actions

.. |Test Status 313| image:: https://github.com/PylarBear/pybear/actions/workflows/matrix-tests-py313.yml/badge.svg
   :target: https://github.com/PylarBear/pybear/actions/workflows/matrix-tests-py313.yml

.. |Test Status 312| image:: https://github.com/PylarBear/pybear/actions/workflows/matrix-tests-py312.yml/badge.svg
   :target: https://github.com/PylarBear/pybear/actions/workflows/matrix-tests-py312.yml

.. |Test Status 311| image:: https://github.com/PylarBear/pybear/actions/workflows/matrix-tests-py311.yml/badge.svg
   :target: https://github.com/PylarBear/pybear/actions/workflows/matrix-tests-py311.yml

.. |Test Status 310| image:: https://github.com/PylarBear/pybear/actions/workflows/matrix-tests-py310.yml/badge.svg
   :target: https://github.com/PylarBear/pybear/actions/workflows/matrix-tests-py310.yml

|Doc Status|

.. |Doc Status| image:: https://readthedocs.org/projects/pybear/badge/?version=latest
   :target: https://pybear.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

|TestPyPI Build Status|

.. |TestPyPI Build Status| image:: https://github.com/PylarBear/pybear/actions/workflows/testpypi-publish.yml/badge.svg
   :target: https://github.com/PylarBear/pybear/actions/workflows/testpypi-publish.yml

|PyPI Build Status|
|Version|
|PyPI Downloads|

.. |PyPI Build Status| image:: https://github.com/PylarBear/pybear/actions/workflows/pypi-publish.yml/badge.svg
   :target: https://github.com/PylarBear/pybear/actions/workflows/pypi-publish.yml

.. |Version| image:: https://img.shields.io/pypi/v/pybear
   :target: https://pypi.org/project/pybear
   :alt: PyPI Version

.. |PyPI Downloads| image:: https://static.pepy.tech/badge/pybear
   :target: https://pepy.tech/project/pybear
   :alt: PyPI Downloads

|DOI|

.. |DOI| image:: https://zenodo.org/badge/780637275.svg
   :target: https://doi.org/10.5281/zenodo.16547172
   :alt: DOI

|BMC|

.. |BMC| image:: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
   :target: https://www.buymeacoffee.com/pybear
   :alt: Buy Me A Coffee

.. _documentation: https://pybear.readthedocs.io/

.. |PythonVersion| replace:: >=3.10
.. |JoblibVersion| replace:: >=1.3.0
.. |NumpyVersion| replace:: >=2.1.0
.. |PandasVersion| replace:: >=2.2.3
.. |PolarsVersion| replace:: >=1.19.0
.. |PsutilVersion| replace:: >=5.7.0
.. |PytestVersion| replace:: >=7.0.0
.. |ScipyVersion| replace:: >=1.15.0
.. |ScikitLearnVersion| replace:: >=1.5.2
.. |TypingExtensionsVersion| replace:: >=4.12.0



Cool, but not frozen, packages to augment your Python data analytics experience.

pybear is a scikit-learn-style Python computing library that augments data
analytics functionality found in popular packages like scikit-learn and xgboost.

See documentation_ for more information.

Website: https://pybear.readthedocs.io/en/stable/index.html

License
-------

BSD 3-Clause License. See `License File <https://github.com/PylarBear/pybear/blob/main/LICENSE>`__.

=======

Installation
------------

Dependencies
~~~~~~~~~~~~

pybear requires:

- Python (|PythonVersion|)
- joblib (|JoblibVersion|)
- numpy (|NumPyVersion|)
- pandas (|PandasVersion|)
- polars (|PolarsVersion|)
- psutil (|PsutilVersion|)
- scikit-learn (|ScikitLearnVersion|)
- scipy (|ScipyVersion|)
- typing_extensions (|TypingExtensionsVersion|)

User installation
~~~~~~~~~~~~~~~~~

Install pybear from the online PyPI package repository using ``pip``::

   (your-env) $ pip install pybear

Conda distributions are expected to be made available sometime after release to
PyPI.

=======

Usage
-----
The folder structure of pybear is nearly identical to scikit-learn. This is so
those that are familiar with the scikit layout and have experience with writing
the associated import statements have an easy transition to pybear. The pybear
subfolders are *base*, *feature_extraction*, *model_selection*, *new_numpy*,
*preprocessing*, and *utilities*. For the full layout, see the API section of
the pybear website on Read The Docs.

You can import pybear's packages in the same way you would with scikit. Here
are a few examples of how you could import and use pybear modules:

.. code-block:: console

    from pybear.preprocessing import InterceptManager as IM

    trfm = IM()
    trfm.fit(X, y)

    from pybear import preprocessing as pp

    trfm = pp.ColumnDeduplicator()
    trfm.fit(X, y)


=======

Major Modules
-------------

AutoGridSearchCV
~~~~~~~~~~~~~~~~
Perform multiple uninterrupted passes of grid search with sci-kit learn 
GridSearchCV utilizing progressively narrower search grids.

- Access via pybear.model_selection.AutoGridSearchCV.

autogridsearch_wrapper
~~~~~~~~~~~~~~~~~~~~~~
Create your own auto-gridsearch class. A function that wraps any scikit-learn,
pybear, or dask_ml GridSearchCV module to create an identical GridSearch class
that performs multiple passes of grid search using progressively narrower
search grids.

- Access via pybear.model_selection.autogridsearch_wrapper.

GSTCV (GridSearchThresholdCV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Perform conventional grid search on a classifier with concurrent threshold 
search. Finds the global optima for the passed parameters and thresholds. Fully
compliant with the scikit-learn GridSearchCV API.

- Access via pybear.model_selection.GSTCV.

AutoGSTCV
~~~~~~~~~
Perform multiple uninterrupted passes of grid search with pybear GSTCV 
utilizing progressively narrower search grids.

- Access via pybear.model_selection.AutoGSTCV.

MinCountTransformer
~~~~~~~~~~~~~~~~~~~
Perform minimum frequency thresholding on numerical or categorical data 
simultaneously across an entire array of data. Violates the scikit-learn API 
in that datasets are modified along the example axis (examples may be deleted.)
Otherwise is fully compliant with the sci-kit learn transformer API, with fit, 
transform, and partial_fit methods.

- Access via pybear.preprocessing.MinCountTransformer.

ColumnDeduplicator
~~~~~~~~~~~~~~~~~~
Identify and selectively remove duplicate columns in numerical or categorical 
data. Fully compliant with the scikit-learn transformer API, with fit,
transform, and partial_fit methods. Perfect for removing duplicate columns from
one-hot encoded data in a scikit-learn pipeline. Also fits and transforms data 
batch-wise, such as with dask_ml Incremental and ParallelPostFit wrappers.

- Access via pybear.preprocessing.ColumnDeduplicator.

InterceptManager
~~~~~~~~~~~~~~~~
A scikit-style transformer that identifies and manages constant columns in a 
dataset. IM can remove all, selectively keep one, or append a column of 
constants. Handles numerical & non-numerical data, and nan-like values. Does 
batch-wise fitting via a partial_fit method, and can be wrapped with dask_ml 
Incremental and ParallelPostFit wrappers.

- Access via pybear.preprocessing.InterceptManager.

SlimPolyFeatures
~~~~~~~~~~~~~~~~
Perform a polynomial feature expansion on a dataset omitting constant and 
duplicate columns. Follows the standard scikit-learn transformer API. Handles 
scipy sparse matrices/arrays. Suitable for sklearn pipelines. Has a partial_fit 
method for batch-wise training and can be wrapped with dask_ml Incremental and
ParallelPostFit wrappers.

- Access via pybear.preprocessing.SlimPolyFeatures.


The pybear Text Wrangling Suite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pybear has a wide selection of text wrangling tools for those who don't have a
PhD in NLP. Most modules have the dual capability of working with regular
expressions or literal strings (for those who don't know regular expressions!)
Most of the modules also accept data in 1D list-like format or (ragged!) 2D
array-like format. All of these are built in scikit transformer API style and
can be stacked in a scikit pipeline.

These modules can be found in pybear.feature_extraction.text.
The modules include:

- Lexicon - A class exposing 68,000+ English words and a stop words attribute
- NGramMerger - Join select adjacent tokens together to handle as a single token
- StopRemover - Remove pybear stop words from a body of text
- TextJoiner - Join tokenized text into a contiguous string with separators
- TextJustifier - Justify to a fixed margin; wrap on literals or regex patterns
- TextLookup - Compare words in a body of text against the pybear Lexicon
- TextLookupRealTime - Same as TextLookup but with in-situ save capability
- TextNormalizer - Normalize text to the same case
- TextPadder - Pad ragged text into shaped containers using fill
- TextRemover - Remove units of contiguous text
- TextReplacer - Remove substrings from contiguous text
- TextSplitter - Split contiguous text into tokens using literal strings or regex
- TextStatistics - Compile statistics about a body of text
- TextStripper - Remove leading and trailing spaces from text


=======

Related Resources
-----------------
pybear has a sister package called pybear-dask. A few of the pybear modules
have a corresponding twin in pybear-dask. You can pip install pybear-dask
from PyPI in the same way as pybear. There is no Read The Docs website for
pybear-dask, but it does have a GitHub repo.

https://github.com/PylarBear/pybear-dask/

Use the pybear documentation for guidance on how to use the pybear-dask modules.


=======

Changelog
---------

See the `changelog <https://github.com/PylarBear/pybear/blob/main/CHANGELOG.md>`__
for a history of notable changes to pybear.

=======

Development
-----------

Important links
~~~~~~~~~~~~~~~

- Official source code repo: https://github.com/PylarBear/pybear
- Download releases: https://test.pypi.org/project/pybear/ (pypi coming soon!)
- Issue tracker: https://github.com/PylarBear/pybear/issues

Source code
~~~~~~~~~~~

You can clone the latest source code with the command::

    git clone https://github.com/PylarBear/pybear.git

Contributing
~~~~~~~~~~~~

pybear is not ready for contributions at this time!

Testing
~~~~~~~

pybear 0.2 is tested via GitHub Actions to run on Linux, Windows, and MacOS,
with Python versions 3.10, 3.11, 3.12, and 3.13. pybear is not tested on earlier
versions, but some features may work.

If you want to test pybear yourself, you will need:

- pytest (|PytestVersion|)

The tests are not available in the PyPI pip installation. You can get
the tests by downloading the tarball from the pybear project page on
`pypi.org <https://pypi.org/project/pybear/>`_ or cloning the pybear repo from
`GitHub <https://github.com/PylarBear/pybear>`_. Once you have the source files
in a local project folder, create a poetry environment for the project and
install the test dependencies. After installation, open the poetry environment
shell and you can launch the test suite from the root of your pybear project
folder with::

    (your-pybear-env) you@your_computer:/path/to/pybear/project$ pytest tests/

Project History
---------------

The project originated in the early 2020's as a collection of miscellaneous 
private modules to enhance the python data analytics ecosystem. In 2025, the 
modules were formalized and bundled together for their first release as pybear.

Help and Support
----------------

Documentation
~~~~~~~~~~~~~

- HTML documentation: https://pybear.readthedocs.io/en/stable/api.html

Communication
~~~~~~~~~~~~~

- GitHub Discussions: https://github.com/PylarBear/pybear/discussions





