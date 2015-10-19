import os
import codecs
import re
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

package_requires = [
    'selenium',
    'reportlab',
]

# Use README.rst for long description.
readme_path = os.path.join(here, 'README.rst')
long_description = ''
if os.path.exists(readme_path):
    with codecs.open(readme_path, encoding='utf-8') as fp:
        long_description = fp.read()


# Origin URL: http://tell-k.github.io/pyconjp2015/#28
def find_version(*file_paths):
    version_file_path = os.path.join(*file_paths)
    try:
        with codecs.open(version_file_path) as fp:
            version_file = fp.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
        if version_match:
            return version_match.group(1)
    except OSError:
        raise RuntimeError("Unable to find version string.")
    raise RuntimeError("Unable to find version string.")


setup(
    name='slide2pdf',
    version=find_version('slide2pdf.py'),
    url='https://github.com/attakei/slide2pdf',
    description='Convert html5-slide into pdf',
    long_description=long_description,
    author='attakei',
    author_email='attakei@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
    ],
    keywords='html5slide pdf',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=package_requires,
    entry_points = {
        "console_scripts": [
            "slide2pdf=slide2pdf:main",
        ]
    }
)
