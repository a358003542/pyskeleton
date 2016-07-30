#!/usr/bin/env python
#-*-coding:utf-8-*-

from setuptools import setup, find_packages

#+BEGIN_DELETE
import os.path
# anditional to make  a tar.gz file
import tarfile
with tarfile.open("skeleton.tar.gz", "w:gz") as tar:
    for name in ["setup.py", "LICENSE", "README.md", "requirements.txt",
                 "pyskeleton", "tests","setup.cfg","pytest.ini","MANIFEST.in"]:
        tar.add(name)

from pyskeleton.compat import replace
replace('skeleton.tar.gz', 'pyskeleton/skeleton.tar.gz')
#+END_DELETE

import pyskeleton
import codecs


def long_description():
    with codecs.open('README.md', encoding='utf-8') as f:
        return f.read()

REQUIREMENTS = ['pytest-runner']

import sys
if sys.platform == "win32":
    REQUIREMENTS.append('pyosreplace')


setup(
    name='pyskeleton',
    version=pyskeleton.__version__,
    description='quickly create a python module, have some other good concern.',
    url='https://github.com/a358003542/pyskeleton',
    long_description=long_description(),
    author='wanze',
    author_email='a358003542@gmail.com',
    maintainer='wanze',
    maintainer_email='a358003542@gmail.com',
    license='GPL 2',
    platforms='Linux',
    keywords=['skeleton', 'python'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX :: Linux',
                 'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    package_data={"pyskeleton": ['skeleton.tar.gz'], },
    setup_requires=REQUIREMENTS,
    install_requires=REQUIREMENTS,
    test_require=['pytest'],
    entry_points={
        'console_scripts': ['pyskeleton=pyskeleton.__main__:main', ],
    }
)
