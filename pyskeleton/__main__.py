#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import argparse
import os
import os.path
import zipfile
import tarfile
import re
import shutil
from pyskeleton import __version__, __softname__
from pkg_resources import resource_filename, resource_string


class Parser(argparse.ArgumentParser):

    def __init__(self, **kwargs):
        super(Parser, self).__init__(**kwargs)

DESCRIPTION = '''
will create a python module skeleton
'''


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
    with tarfile.open(resource_filename("pyskeleton", "pyskeleton.tar.gz")) as tar:
        tar.extractall()

    # delete some line use the #+BEGIN_DELETE and #+END_DELETE as a sign.
    fname = 'setup.py'
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    with open(fname, 'w') as f:
        delete_block = False
        for line in lines:
            if delete_block:
                pass
            else:
                f.write(line)

            if re.search('^#\+BEGIN_DELETE', line):
                delete_block = True
            elif re.search('^#\+END_DELETE', line):
                delete_block = False

    # make dir
    os.mkdir(project_name)

    pyfile = resource_filename("pyskeleton", "__init__.py")

    shutil.copy(pyfile, project_name)

    print('great, create {0} succeed'.format(project_name))


# if __name__ == '__main__':
