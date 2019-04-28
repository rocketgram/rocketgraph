# Copyright (C) 2019 by Vd.
# This file is part of Rocketgraph, the powerful asynchronous library for telegra.ph.
# Rocketgraph is released under the MIT License (see LICENSE).


from os.path import join, dirname

import setuptools

from rocketgram.version import version

setuptools.setup(
    name='rocketgraph',
    version=version(),
    author='Vd',
    author_email='vd@vd2.org',
    url='https://github.com/vd2org/rocketgraph',
    license='MIT',
    description='Modern and powerful asynchronous telegram bot framework.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    extras_require={
        'aiohttp': ["aiohttp >= 3.5.4"],
        'tornado': ["tornado >= 6.0.2"],
        'ujson': ["ujson >= 1.35"],
        'uvloop': ["uvloop >= 0.12.1"]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
