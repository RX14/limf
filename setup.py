#!/bin/env python
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name='limf',
    version='0.3.0',
    url='http://github.com/lich/limf',
    license='MIT',
    author='Mikołaj Halber',
    author_email='lich@openmailbox.com',
    description='A tool for uploading files to pomf.se clones',
    packages=['limf'],
    install_requires=[
        'Requests>=2.6.0',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points='''
        [console_scripts]
        limf=limf.cli:main
    '''
)


