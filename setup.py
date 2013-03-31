#!/usr/bin/env python
from setuptools import setup
from distutils.core import Command

VERSION = '0.8'
DESCRIPTION = "A wrapper for comicvine.com"

with open('README.md', 'r') as f:
   LONG_DESCRIPTION = f.read()

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        raise SystemExit(
                subprocess.call([
                        sys.executable,
                        # Turn on deprecation warnings
                        '-Wd',
                        # Use module unittest
                        '-m',
                        'unittest',
                        'tests'
                    ])
            )

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
        license="MIT License",
        cmdclass={'test': TestCommand}
    )