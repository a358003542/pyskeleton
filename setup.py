#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
from setuptools import setup, find_packages
import pyskeleton
import codecs

REQUIREMENTS = []
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# +BEGIN_DELETE
# anditional to make  a tar.gz file
import tarfile

with tarfile.open("pyskeleton.tar.gz", "w:gz") as tar:
    for name in ["setup.py", "LICENSE", "README.md", "requirements.txt",
                 "tests", "MANIFEST.in", ".gitignore"]:
        tar.add(name)

from pyskeleton.compat import replace

replace('pyskeleton.tar.gz', 'pyskeleton/pyskeleton.tar.gz')

# +END_DELETE


setup(
    name='pyskeleton',
    version=pyskeleton.__version__,
    description='quickly create a python module, have some other good concern.',
    url='https://github.com/a358003542/pyskeleton',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='wanze',
    author_email='a358003542@gmail.com',
    maintainer='wanze',
    maintainer_email='a358003542@gmail.com',
    license='MIT',
    platforms='Linux',
    keywords=['skeleton', 'python'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX :: Linux',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    setup_requires=REQUIREMENTS,
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': ['pyskeleton=pyskeleton.__main__:main', ],
    }
)
