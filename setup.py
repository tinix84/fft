# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fft',
    version='0.0.0',
    description='collection of fft, spectrum utilities for power electronic',
    long_description=readme,
    author='riccardo tinivella',
    author_email='tinix84@gmail.com',
    url='https://github.com/tinix84/fft',
    license=license,
    #packages=['fft'],
    packages=find_packages(exclude=('tests', 'docs', 'mfiles')),
    install_requires=['numpy', 'scipy'],  
)
