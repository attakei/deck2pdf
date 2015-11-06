import os
from pytest import raises
from slide2pdf import errors


current_dir = os.path.abspath(os.getcwd())
test_dir = os.path.abspath(os.path.dirname(__file__))


class TestForCaptureEngine(object):
    @property
    def _class(self):
        from slide2pdf.captures import CaptureEngine
        return CaptureEngine

    def test_init_not_resource(self):
        raises(errors.ResourceNotFound, self._class, ('test'))

    def test_init_exists_resource(self):
        engine = self._class('tests/testslide/index.rst')
        assert engine.url == 'file://{}/{}'.format(test_dir, 'testslide/index.rst')
        assert engine.save_dir == os.path.join(current_dir, '.slide2pdf')

    def test_init_web_resource(self):
        engine = self._class('http://example.com/')
        assert engine.url == 'http://example.com/'
        assert engine.save_dir == os.path.join(current_dir, '.slide2pdf')

    def test_start_for_save_dir(self):
        engine = self._class('http://example.com/')
        engine.start()
        import glob
        files = glob.glob('{}/*'.format(engine.save_dir))
        assert len(files) == 0

    def test_capture_page_is_abstract(self):
        engine = self._class('http://example.com/')
        raises(NotImplementedError, engine.capture_page, ())

    def test_capture_all_is_abstract(self):
        engine = self._class('http://example.com/')
        raises(NotImplementedError, engine.capture_all)


class TestForPhantomJsCaptureEngine(object):
    @property
    def _class(self):
        from slide2pdf.captures import phantomjs
        return phantomjs.CaptureEngine

    def test_init(self):
        # Same to TestForCaptureEngine.test_init_web_resource
        engine = self._class('http://example.com/')
        assert engine.url == 'http://example.com/'
        assert engine.save_dir == os.path.join(current_dir, '.slide2pdf')


class TestForFindEngine(object):
    def test_not_found(self):
        from slide2pdf.captures import find_engine
        assert find_engine('noengine') is None

    def test_found_ghostpy(self):
        from slide2pdf.captures import find_engine
        from slide2pdf.captures.ghostpy import CaptureEngine
        engine = find_engine('ghostpy')
        assert engine == CaptureEngine


def test_resolve_path():
    from slide2pdf.captures import resolve_path
    assert resolve_path('http://example.com') == 'http://example.com'
    assert resolve_path('https://example.com') == 'https://example.com'
    assert resolve_path('tests/testslide/index.rst') == 'file://{}/{}'.format(test_dir, 'testslide/index.rst')
    raises(errors.ResourceNotFound, resolve_path, ('not_found'))
