#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='classbasedmodule',
    version='0.1.0',
    description="Decorator overwriting sys.modules with a class instance as the module.",
    author="Sjoerd Job Postmus",
    author_email='sjoerdjob@sjec.nl',
    url='https://github.com/sjoerdjob/python-classbasedmodule',
    py_modules=['classbasedmodule'],
    include_package_data=True,
    install_requires=[],
    license="MIT license",
    zip_safe=False,
    keywords='classbasedmodule',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
