#!/usr/bin/env python
from setuptools import setup
setup(
    name="pest",
    version="1.0.1",
    packages=['pest'],
    scripts=['pest/pester'],
    install_requires=['pyobjc-framework-FSEvents','growl-py'],
    description="Auto tester for python",
    author="Chuck Collins",
    author_email="chuck.collins@gmail.com",
    url="http://github.com/ccollins/pest",
)