#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='interview_project',
      version='0.1',
      description='Python Interview Project',
      author='Graham Greenfield',
      author_email='grahamg@gmail.com',
      packages=find_packages(exclude=[]),
      test_suite='interview_project.tests',
)
