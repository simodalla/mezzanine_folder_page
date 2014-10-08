# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from setuptools import setup, find_packages

readme = open('README.rst', encoding='utf-8').read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'mezzanine',
]

from mezzanine_folder_page import __version__ as version

setup(
    name='mezzanine-folder-page',
    version=version,
    author='Simone Dalla',
    author_email='simodalla@gmail.com',
    description='A Mezzanine module for add new content type named FolderPage.',
    long_description=readme,
    license='BSD License',
    url='https://github.com/simodalla/mezzanine_page_folder/',
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    # test_suite='runtests.runtests',
    # tests_require=['mock', 'pep8', 'pyflakes'],
    classifiers=[
        'Development Status :: 5 - Production/Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
