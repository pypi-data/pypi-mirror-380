# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='odoo-image-fetcher',
    version='0.1.9',
    author='Onyekelu Chukwuebuka',
    author_email='conyekelu@yahoo.com',
    description='A simple utility to fetch images from Odoo via XML-RPC.',
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cloudtechy/odoo-image-fetcher',
    download_url='https://github.com/cloudtechy/odoo-image-fetcher/archive/refs/tags/v0.1.9.tar.gz',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
        'urllib3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
