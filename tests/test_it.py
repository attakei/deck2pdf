import os
import shutil
import slide2pdf
from pytest import raises


current_dir = os.path.abspath(os.getcwd())
test_dir = os.path.abspath(os.path.dirname(__file__))


class TestForMain(object):
    def setUp(self):
        shutil.rmtree(os.path.join(current_dir, '.slide2pdf'), ignore_errors=True)

    def test_help(self):
        raises(SystemExit, slide2pdf.main, [])
        raises(SystemExit, slide2pdf.main, ['-h'])

    def test_files(self):
        test_slide_path = os.path.join(test_dir, 'testslide/_build/slides/index.html')
        slide2pdf.main([test_slide_path, ])
        assert os.path.exists(os.path.join(current_dir, '.slide2pdf'))