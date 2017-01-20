#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='undirected_graph',
      version='0.1',
      description='Undirected Graph Kata',
      author='Graham Greenfield',
      author_email='grahamg@gmail.com',
      packages=find_packages(exclude=[]),
      test_suite='undirected_graph.tests',
      entry_points = {
          'console_scripts': [
              'undirected_graph=undirected_graph:main',
          ]
      }
)
