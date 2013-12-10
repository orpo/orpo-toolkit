#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Orpo Toolkit
from setuptools import setup, find_packages
from orpo_toolkit import __version__

long_description = """"""

setup(
	name='OrpoToolkit',
	version=__version__,
	description='Orpo Toolkit',
	long_description=long_description,
	author='Nick Snell',
	author_email='nick@orpo.co.uk',
	url='https://github.com/orpo/orpo-toolkit.git',
	license='BSD',
	platforms=['Linux',],
	packages=find_packages(exclude=['tests',]),
	install_requires=[],
)