Convert html5-slides into PDF slide
===================================

**Badges**

.. image:: https://img.shields.io/pypi/v/deck2pdf.svg
   :target: https://pypi.python.org/pypi/deck2pdf
   :alt: PyPI latest

.. image:: https://img.shields.io/circleci/project/attakei/deck2pdf.svg
   :target: https://circleci.com/gh/attakei/deck2pdf
   :alt: CircleCI Status (not all tests)

.. image:: https://img.shields.io/codeclimate/github/attakei/deck2pdf.svg
   :target: https://codeclimate.com/github/attakei/deck2pdf
   :alt: CodeClimate GPA


deck2pdf is batch application that will convert your `Google html5slides <http://code.google.com/p/html5slides/>`_ into PDF format keeping slide layout.


Install
-------

deck2pdf is required `PySide <http://pyside.github.io/docs/pyside/index.html>`_ for `Ghost.py <https://github.com/jeanphix/Ghost.py>`_ .


::

   $ pip install pyside
   $ pyside_postinstall.py -install
   $ pip install https://github.com/attakei/deck2pdf


Usage
-----

Simply usage::

   $ deck2pdf <slide-url>
   $ ls
   slide.pdf

Specify slide name (but not work...)::

   $ deck2pdf -o myslide.pdf <slide-url>
   $ ls
   myslide.pdf


Batch architecture
------------------

It is a simple.

#. Capture slide screenshot.
#. Merge slides and save pdf format.


Future
------

I want to ...

* Adjust to be able to save html slide of other styles (reveal.js, impress.js).
* Deliver makefile setting to make slidepdf
