Convert html5-slides into PDF slide
===================================

slide2pdf is batch application that will convert your `Google html5slides <http://code.google.com/p/html5slides/>`_ into PDF format keeping slide layout.

This application need phantomjs to capture screen shot of slide.


Install
-------

.. code::

   $ npm install -g phantomjs
   $ pip install https://github.com/attakei/slide2pdf


Batch architecture
------------------

It is a simple.

#. Run http.server for slide html to run JavaScript.
#. Capture slide screenshot.
#. Merge slides and save pdf format.


Future
------

I want to ...

* Remove dependency to PhantomJS.
* Adjust to be able to save html slide of other styles (reveal.js, impress.js).
