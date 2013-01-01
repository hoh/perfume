#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import perfume

setup(
    name='perfume',
    version=perfume.__version__,

    author="Hugo Herter",
    author_email="hugoherter.com",
    url='http://github.com/hoh/perfume',
    license="BSD",

    packages=find_packages(),

    description="Simple Object Oriented layer for Flask.",
    long_description=open('README.md').read(),

    install_requires=["Flask"],
    include_package_data=True,

    classifiers=[
        "Intended Audience :: Developers",
        "Environment :: Web Environment",

        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "License :: OSI Approved",
        "Operating System :: OS Independent",

        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",

        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)