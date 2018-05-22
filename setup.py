#!/usr/bin/env python

from finfin import __version__
from setuptools import  setup, find_packages

setup(
    name="finfin",
    version=__version__,
    author="M**** S****",
    author_email="M***@***.com",
    description=("FinFin"),
    keywords="finfin",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'static': 'finfin/static/*',
        'templates': 'finfin/templates/*'
    },
    entry_points={
        'console_scripts': [
            'run-finfin=finfin:main'
        ]
    },
)
