#!/usr/bin/env python
from setuptools import setup

VERSION = '0.8'
DESCRIPTION = "A wrapper for comicvine.com"

with open('README.md', 'r') as f:
   LONG_DESCRIPTION = f.read()

setup(
        name='PyComicVine',
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author='Martin Lenders',
        author_email='authmillenon@gmail.com',
        url='http://www.github.com/authmillenon/pycomicvine/',
        packages=['pycomicvine'],
        install_requires=['simplejson','python-dateutil >= 2.0'],
        license="MIT License"
    )
