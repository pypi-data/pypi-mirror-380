#! -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='cutword-lite',
    version='0.2.0',
    python_requires='>=3',
    description='Just Cut Word Faster',
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    license_files=[],
    url='https://github.com/basicv8vc/cutword-lite',
    author='basicv8vc',
    install_requires=['numpy', 'pyahocorasick'],
    packages=find_packages(),
    package_data={'cutword': ['*.txt']},
    include_package_data=True
)
