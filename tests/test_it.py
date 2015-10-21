import os
import shutil
import slide2pdf
import unittest


current_dir = os.path.abspath(os.getcwd())


class TestForMain(unittest.TestCase):
    def setUp(self):
        shutil.rmtree(os.path.join(current_dir, '.slide2pdf'), ignore_errors=True)

    def test_help(self):
        with self.assertRaises(SystemExit):
            slide2pdf.main()
        with self.assertRaises(SystemExit):
            slide2pdf.main(['-h'])
