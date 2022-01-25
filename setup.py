#!/usr/bin/env python

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(long_description=long_description,
      long_description_content_type="text/markdown",
      name='reldi-tokeniser',
      version='1.0.1',
      licence='apache-2.0',
      description='Sentence splitting and tokenization for South Slavic languages',
      author='CLARIN.SI',
      url='https://www.github.com/clarinsi/reldi-tokeniser',
      packages=['reldi_tokeniser'],
      package_data={'reldi_tokeniser': ['*.abbrev', 'punct']}
     )
