# -*- coding:utf8 -*-
"""Capturing engins
"""
import os
import logging


Logger = logging.getLogger('slide2pdf.captures')

TEMP_CAPTURE_DIR = '.slide2pdf'


class CaptureEngine(object):
    """Slide capturing engine (abstract)
    """
    def __init__(self, url):
        self._url = url
        self._slide_captures = []

    @property
    def url(self):
        return self._url

    @property
    def save_dir(self):
        current_dir = os.path.abspath(os.getcwd())
        return os.path.join(current_dir, TEMP_CAPTURE_DIR)

    def capture_all(self):
        """Capture all pages of slide
        """
        raise NotImplementedError()

    def capture_page(self, page_options):
        """Capture per page of slide, and save as pdf
        """
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()

    def end(self):
        raise NotImplementedError()
