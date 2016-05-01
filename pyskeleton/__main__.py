#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys
import argparse

from pyskeleton import __version__ , __softname__


class Parser(argparse.ArgumentParser):
    def __init__(self,**kwargs):
        super(Parser,self).__init__(**kwargs)

DESCRIPTION = '''
will create a python module skeleton
'''

def main():
    parser = Parser(description=DESCRIPTION)
    parser.add_argument('name',help='the target proejct name')
    parser.add_argument('-v','--version',action='version',version=__version__)
    args = parser.parse_args()
    project_name = args.name

#+BEGIN_DELETE
    import os , os.path
    import zipfile ,tarfile
    import re

    os.mkdir(project_name)
    os.chdir(project_name)
#tar unzip
    from pkg_resources import resource_filename
    with tarfile.open(resource_filename("pyskeleton","skeleton.tar.gz")) as tar:
        tar.extractall()

    #delete the tar.gz file
    os.remove("pyskeleton/skeleton.tar.gz")

    ## delete some line use the #+BEGIN_DELETE and #+END_DELETE as a sign.
    files = ['setup.py','pyskeleton/__main__.py']
    for fname in files:

        f = open(fname,'r')
        lines = f.readlines()
        f.close()
        with open(fname,'w') as f:
            delete_block = False
            for line in lines:
                if delete_block:
                    pass
                else:
                    f.write(line)

                if re.search('^#\+BEGIN_DELETE',line):
                    delete_block = True
                elif re.search('^#\+END_DELETE',line):
                    delete_block = False

    # rename directory
    os.rename('pyskeleton',project_name)

#+END_DELETE

#if __name__ == '__main__':

