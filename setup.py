import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

setup(
    name="csv2sqlite",
    version="0.1",
    author="Matthew Perry",
    author_email="perrygeo@gmail.com",
    description=("Convert csvs to sqlite tables"),
    license="MIT",
    keywords="csv sql sqlite",
    url="https://github.com/perrygeo/csv2sqlite",
    #package_dir={'': 'src'},
    #packages=['rasterstats'],
    #long_description=read('README.rst'),
    install_requires=[
        'docopt',
    ],
    scripts=['csv2sqlite'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
