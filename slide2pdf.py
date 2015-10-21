#!/usr/bin/env python
import os
import logging
import argparse
import urllib2
import time
from selenium import webdriver


__version__ = '0.0.2'


Logger = logging.getLogger('slide2pdf')


def find_phantomjs_path():
    candidate_path = (
        # local node-modules path
        os.path.join(os.getcwd(), 'node_modules/phantomjs/bin/phantomjs'),
        # nodebrew current version path
        os.path.join(os.environ['HOME'], '.nodebrew/current/bin/phantomjs'),
    )
    for path in candidate_path:
        if os.path.exists(path):
            return path
    return None


def count_slide_from_dom(body):
    # FIXME: Too bad know-how
    import re
    return len(re.split('<\/slide>', body)) - 1


parser = argparse.ArgumentParser()
parser.add_argument('path', help='Slide endpoint file path', type=str)
parser.add_argument('-o', '--output', help='Output slide file path', type=str, default='./slide.pdf')


def main():
    args = parser.parse_args()
    args.path = os.path.abspath(args.path)
    args.output = os.path.abspath(args.output)

    # Capture
    phantomjs_path = find_phantomjs_path()
    Logger.debug(phantomjs_path)
    driver = webdriver.PhantomJS(phantomjs_path)
    driver.set_window_size(1280, 720)

    resp_ = urllib2.urlopen('file://' + args.path)
    slides = count_slide_from_dom(resp_.read())
    Logger.debug('{} slides'.format(slides))

    slide_captures = []
    for slide_idx in range(1, slides):
        url_ = 'file://' + args.path + '#' + str(slide_idx)
        FILENAME = os.path.join(os.getcwd(), "screen_{}.png".format(slide_idx))
        Logger.debug(url_)
        Logger.debug(FILENAME)

        # Open Web Browser & Resize 720P
        driver.get(url_)
        time.sleep(1)
        driver.refresh()
        time.sleep(1)

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
