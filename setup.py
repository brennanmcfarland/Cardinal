# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


setup(
    name='cardinal',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    author='Emilio Lopez and Brennan McFarland',
    author_email='eil11@case.edu',
    url='https://github.com/eLopez6/Cardinal',
    packages=find_packages(exclude=('tests', 'docs'))
)
