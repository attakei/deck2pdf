import os
from pytest import raises
from slide2pdf import captures


current_dir = os.path.abspath(os.getcwd())
test_dir = os.path.abspath(os.path.dirname(__file__))


class TestForCaptureEngine(object):
    def test_init(self):
        engine = captures.CaptureEngine('test')
        assert engine.url == 'test'
        assert engine.save_dir == os.path.join(current_dir, '.slide2pdf')

    def test_capture_page_is_abstract(self):
        engine = captures.CaptureEngine('test')
        raises(NotImplementedError, engine.capture_page, ())

    def test_capture_all_is_abstract(self):
        engine = captures.CaptureEngine('test')
        raises(NotImplementedError, engine.capture_all)


class TestForPhantomJsCaptureEngine(object):
    @property
    def _class(self):
        from slide2pdf.captures import phantomjs
        return phantomjs.CaptureEngine

    def test_init(self):
        engine = self._class('test')
        assert engine.url == 'file://test'
        assert engine.save_dir == os.path.join(current_dir, '.slide2pdf')

    def test_capture_page(self):
        engine = captures.CaptureEngine('test')
        raises(NotImplementedError, engine.capture_page, (1))
