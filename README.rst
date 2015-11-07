Convert html5-slides into PDF slide
===================================

deck2pdf is batch application that will convert your `Google html5slides <http://code.google.com/p/html5slides/>`_ into PDF format keeping slide layout.


Install
-------

deck2pdf is required `PySide <http://pyside.github.io/docs/pyside/index.html>`_ for `Ghost.py <https://github.com/jeanphix/Ghost.py>`_ .


.. code::

   $ pip install pyside
   $ pyside_postinstall.py -install
   $ pip install https://github.com/attakei/deck2pdf


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
