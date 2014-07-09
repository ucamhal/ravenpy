#!/usr/bin/env python
from setuptools import setup


setup(
    name="ravenpy",
    version="0.1.0",
    description=(
        "A Python library for authenticating users with the University of "
        "Cambridge's Raven authentication service "
        "(https://raven.cam.ac.uk/)."),
    author="Hal Blackburn",
    author_email="hwtb2@cam.ac.uk",
    url="https://github.com/ucamhal/ravenpy",
    packages=['raven'],
    install_requires=[
        "pycrypto >=2.6.0, <2.7.0",
    ],
    license="BSD",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP",
    ],
    test_suite="test"
)
