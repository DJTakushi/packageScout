#!/usr/bin/env python

from distutils.core import setup

setup(name='packageScout',
      version='0.0.1',
      description="Parses /var/lib/dpkg/status (and/or any other needed files) and displays a list of packages explicitly installed by the user.",
      author='Danny Takushi',
      author_email='dannytakushi@gmail.com',
      url='https://github.com/DJTakushi/packageScout"',
      py_modules=['src/packageScout/packageScout']
      # packages=['distutils', 'distutils.command'],
     )
