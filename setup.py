import os
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
    with open(readme_path) as fp:
        long_description = fp.read()


setup(
    name='slide2pdf',
    version='0.0.1',
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
