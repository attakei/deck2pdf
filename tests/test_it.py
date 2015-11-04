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


class TestForCaptureEngine(object):
    def test_init(self):
        engine = slide2pdf.CaptureEngine('test')
        assert engine.url == 'test'
        assert engine.save_dir == os.path.join(current_dir, '.slide2pdf')

    def test_capture_page_is_abstract(self):
        engine = slide2pdf.CaptureEngine('test')
        raises(NotImplementedError, engine.capture_page, ())

    def test_capture_all_is_abstract(self):
        engine = slide2pdf.CaptureEngine('test')
        raises(NotImplementedError, engine.capture_all)
