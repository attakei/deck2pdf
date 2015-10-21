import os
import shutil
import slide2pdf
from pytest import raises


current_dir = os.path.abspath(os.getcwd())


class TestForMain(object):
    def setUp(self):
        shutil.rmtree(os.path.join(current_dir, '.slide2pdf'), ignore_errors=True)

    def test_help(self):
        raises(SystemExit, slide2pdf.main, [])
        raises(SystemExit, slide2pdf.main, ['-h'])
