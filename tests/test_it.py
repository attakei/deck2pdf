import os
import deck2pdf
from pytest import raises
from . import (
    current_dir,
    test_dir,
)


def test_help():
    raises(SystemExit, deck2pdf.main, [])
    raises(SystemExit, deck2pdf.main, ['-h'])


def test_files():
    test_slide_path = os.path.join(test_dir, 'testslide/_build/slides/index.html')
    deck2pdf.main([test_slide_path, '-c', 'stub'])
    assert os.path.exists(os.path.join(current_dir, '.deck2pdf'))


def test_output_file_by_name():
    output_path = os.path.join(current_dir, '.deck2pdf', 'test.output')
    test_slide_path = os.path.join(test_dir, 'testslide/_build/slides/index.html')
    deck2pdf.main([test_slide_path, '-c', 'stub', '-o', output_path])
    assert os.path.exists(output_path)
