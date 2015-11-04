#!/usr/bin/env python
import sys
import os
import logging
import argparse


__version__ = '0.1.2'


Logger = logging.getLogger('slide2pdf')

TEMP_CAPTURE_DIR = '.slide2pdf'


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
    from slide2pdf.captures.phantomjs import CaptureEngine
    capture = CaptureEngine(args.path)
    capture.capture_all()

    # Merge
    pdf_path = os.path.join(os.getcwd(), 'slide.pdf')

    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.pdfgen import canvas

    slide_size = landscape(A4)
    pdf = canvas.Canvas(pdf_path, pagesize=slide_size)
    idx = 0
    for slide in capture._slide_captures:
        pdf.drawImage(slide, 0, 0, slide_size[0], slide_size[1])
        pdf.showPage()
        idx += 1
    pdf.save()


if __name__ == '__main__':
    main()