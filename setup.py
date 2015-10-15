from setuptools import setup, find_packages

package_requires = [
    'selenium',
]

setup(
    name='slide2pdf',
    version='0.0.1',
    url='https://github.com/attakei/slide2pdf',
    description='Convert html5-slide into pdf',
    long_description='',
    author='attakei',
    author_email='attakei@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
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
