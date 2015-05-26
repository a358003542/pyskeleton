#!/usr/bin/env python3
#-*-coding:utf-8-*-

from setuptools import setup ,find_packages
import os.path

#------------- this need removed------------#
#anditional to make  a tar.gz file
import tarfile
with tarfile.open("skeleton.tar.gz", "w:gz") as tar:
    for name in ["setup.py","LICENSE","README.md","skeleton"]:
        tar.add(name)
import os
os.replace('skeleton.tar.gz','skeleton/skeleton.tar.gz')
#-----------------------------#


setup(
    name='skeleton',
    version='0.11',
    description='the software short description',
    url='https://github.com/a358003542/skeleton',
    author='wanze',
    author_email='a358003542@gmail.com',
    maintainer = 'wanze',
    maintainer_email = 'a358003542@gmail.com',
    license='GPL 2',
    platforms = 'Linux',
    keywords =['skeleton','python'],
    classifiers = ['Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    package_data = {"skeleton":['skeleton.tar.gz'],},
#   install_requires=['click'],
#   setup_requires,
#   extras_require={'test': ['pytest'],},
    entry_points = {
        'console_scripts' :[ 'skeleton=skeleton.main:console',],
#       'gui_scripts':['xskeleton=skeleton.main:gui'],
        }
    )



