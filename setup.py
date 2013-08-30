#!/usr/bin/env python
from setuptools import setup
from distutils.core import Command
from sys import stdout, version_info
import logging

VERSION = '0.9'
DESCRIPTION = "A wrapper for comicvine.com"

with open('README.md', 'r') as f:
   LONG_DESCRIPTION = f.read()

extra = {}
if version_info >= (3,):
    extra['use_2to3'] = True
    extra['convert_2to3_doctests'] = ['README.md']

if version_info >= (3,2,) and version_info < (3,3,):
    extra['install_requires'] = ['python-dateutil >= 2.0']
else:
    extra['install_requires'] = ['simplejson', 'python-dateutil >= 2.0']

logging.basicConfig(stream=stdout)
logging.getLogger("tests").setLevel(logging.DEBUG)

setup(
        name='PyComicVine',
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author='Martin Lenders',
        author_email='authmillenon@gmail.com',
        url='http://www.github.com/authmillenon/pycomicvine/',
        packages=['pycomicvine', 'pycomicvine.tests'],
        license="MIT License",
        test_suite='pycomicvine.tests',
        **extra
    )
