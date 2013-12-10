#!/usr/bin/env python
from distutils.core import setup

setup(
    name            = 'pyTries',
    version         = '0.0.1',
    author          = 'Lauris Jullien',
    author_email    = 'lauris.jullien@gmail.com',
    url             = 'https://github.com/laucia/pyTries',
    description     = 'A pure python implementation of diverse trie structures for autocompletion problems',
    long_description= 'A pure python implementation of diverse trie structures',
    classifiers     = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules      = ['pytries'],
)