#!/usr/bin/env python
# -*-coding:utf-8-*-

import sys
import argparse
import os
import os.path
import tarfile
import shutil
from pyskeleton import __version__
from pkg_resources import resource_filename


class Parser(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        super(Parser, self).__init__(**kwargs)


DESCRIPTION = """
will create a python module skeleton
"""


def main():
    parser = Parser(description=DESCRIPTION)
    parser.add_argument('name', help='the target proejct name')
    parser.add_argument('-v', '--version',
                        action='version', version=__version__)
    args = parser.parse_args()
    project_name = args.name

    try:
        os.mkdir(project_name)
        os.chdir(project_name)
    except FileExistsError as e:
        print('file exists error')
        sys.exit(1)

    # tar unzip
    with tarfile.open(
            resource_filename("pyskeleton", "pyskeleton.tar.gz")) as tar:
        tar.extractall()

    # make dir
    os.makedirs('src/module_name')

    pyfile = resource_filename("pyskeleton", "__init__.py")

    shutil.copy(pyfile, 'src/module_name')

    print('great, create {0} succeed'.format(project_name))
