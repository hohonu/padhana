#!/usr/bin/env python

from setuptools import setup
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
version_file = open(os.path.join(dir_path, 'VERSION'))
version = version_file.read().strip()

setup(name='padhana',
      version=version,
      description='Padhana',
      author='Philip Dodds',
      author_email='philip@hohonu.com',
      url='https://www.github.com/hohonu/padhana',
      packages=['padhana', 'padhana.analysis', 'padhana.connectors', 'padhana.core', 'padhana.parsers',
                'padhana.stores', 'padhana.model'],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"])
