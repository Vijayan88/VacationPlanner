# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='module-save-db',
    version='0.0.1',
    description='Service Package for Vacation Planner',
    long_description=readme,
    author='Vijayan',
    author_email='vijayan.balasubramanian@gmail.com',
    url='https://github.com/Vijayan88/VacationPlanner/module-save-db',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

