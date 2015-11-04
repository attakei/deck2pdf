#!/usr/bin/env python
import sys
import os
import logging
import argparse
import urllib2
import time
from selenium import webdriver


__version__ = '0.1.2'


Logger = logging.getLogger('slide2pdf')

TEMP_CAPTURE_DIR = '.slide2pdf'


def find_phantomjs_path():
    """Find path of PhantomJS

    :returns: Path of PhantomJS (If it is not found, return None)
    :rtype: str or None
    """
    candidate_path = [d+'/phantomjs' for d in os.getenv('PATH', '').split(':')]
    for path in candidate_path:
        if os.path.exists(path):
            return path
    return None


class CaptureEngine(object):
    """Slide capturing engine (abstract)
    """
    def __init__(self, url):
        self._url = url

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

    def capture_all(self):
        """Capture per page of slide, and save as pdf
        """
        raise NotImplementedError()


def count_slide_from_dom(body):
    # FIXME: Too bad know-how
    import re
    return len(re.split('<\/slide>', body)) - 1


parser = argparse.ArgumentParser()
parser.add_argument('path', help='Slide endpoint file path', type=str)
parser.add_argument('-o', '--output', help='Output slide file path', type=str, default='./slide.pdf')


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = parser.parse_args(argv)
    args.path = os.path.abspath(args.path)
    args.output = os.path.abspath(args.output)

    root_dir = os.getcwd()
    cache_dir = os.path.join(root_dir, TEMP_CAPTURE_DIR)
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    elif not os.path.isdir(cache_dir):
        # TODO: Modify custom exception?
        raise Exception('{} is not directory.'.format(cache_dir))

    # Capture
    phantomjs_path = find_phantomjs_path()
    Logger.debug(phantomjs_path)
    driver = webdriver.PhantomJS(phantomjs_path)
    driver.set_window_size(960, 720)

    resp_ = urllib2.urlopen('file://' + args.path)
    slides = count_slide_from_dom(resp_.read())
    Logger.debug('{} slides'.format(slides))

    slide_captures = []
    for slide_idx in range(1, slides):
        url_ = 'file://' + args.path + '#' + str(slide_idx)
        FILENAME = os.path.join(cache_dir, "screen_{}.png".format(slide_idx))
        Logger.debug(url_)
        Logger.debug(FILENAME)

        # Open Web Browser & Resize 720P
        driver.get(url_)
        driver.refresh()
        time.sleep(2)

        # Get Screen Shot
        driver.save_screenshot(FILENAME)

        slide_captures.append(FILENAME)

    # https://github.com/SeleniumHQ/selenium/issues/767
    import signal
    driver.service.process.send_signal(signal.SIGTERM)
    driver.quit()

    # Merge
    pdf_path = os.path.join(os.getcwd(), 'slide.pdf')

    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.pdfgen import canvas

    slide_size = landscape(A4)
    pdf = canvas.Canvas(pdf_path, pagesize=slide_size)
    idx = 0
    for slide in slide_captures:
        pdf.drawImage(slide, 0, 0, slide_size[0], slide_size[1])
        pdf.showPage()
        idx += 1
    pdf.save()


if __name__ == '__main__':
    main()
