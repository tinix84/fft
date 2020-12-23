from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.1'

setup(
    name='rockstar',
    version=version,


setup(
    name='fft',
    version='0.0.0',
    description='collection of fft, spectrum utilities for power electronic',
    long_description=readme,
    author='riccardo tinivella',
    author_email='tinix84@gmail.com',
    url='https://github.com/tinix84/fft',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'mfiles')),
    install_requires=requirements
)
