"""Setuptools entry point."""
import codecs
import os

from setuptools import setup

import pytest_cloud

dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, 'README.rst'), encoding='utf-8').read() + '\n' +
    codecs.open(os.path.join(dirname, 'AUTHORS.rst'), encoding='utf-8').read() + '\n' +
    codecs.open(os.path.join(dirname, 'CHANGES.rst'), encoding='utf-8').read()
)


setup(
    name='pytest-cloud',
    description='Distributed tests planner plugin for pytest testing framework.',
    long_description=long_description,
    author='Anatoly Bubenkov and others',
    license='MIT license',
    author_email='bubenkoff@gmail.com',
    version=pytest_cloud.__version__,
    include_package_data=True,
    url='https://github.com/pytest-dev/pytest-cloud',
    install_requires=[
        'psutil',
        'pytest>=2.7.0',
        'pytest-xdist>=1.22.1',
        'setuptools',
        'six',
        'timeout-decorator>=0.3.2',
    ],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ] + [('Programming Language :: Python :: %s' % x) for x in '2.7 3.0 3.1 3.2 3.3 3.4 3.5 3.6'.split()],
    tests_require=['tox'],
    entry_points={'pytest11': [
        'pytest-cloud=pytest_cloud.plugin',
    ]},
    packages=['pytest_cloud'],
)
