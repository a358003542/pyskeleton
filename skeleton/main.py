#!/usr/bin/env python3

import sys
import getopt

from skeleton import __version__ , __softname__

def show_usage():
    print('''usage: skeleton [option]
    1. skeleton --help or --version
    2. skeleton your_new_project_name

-V    :  print the version number and exit(also --version)
-h    :  print this help message and exit(also --help)
''')

def console():
    try:
        opts , args = getopt.getopt(sys.argv[1:],"hV",["help","version"])
    except getopt.GetoptError as err:
        print(err)
        show_usage()
        sys.exit(2)

    for o , a in opts:
        if o in ('-V','--version'):
            print(__softname__ , __version__)
            sys.exit()
        elif o in ('-h','--help'):
            show_usage()
            sys.exit()
        else:
            sys.exit("unhandle options")


    import os , os.path
    import zipfile ,tarfile
    import re
#new directory   ; tar unzip ;
    if len(args) > 1:
        show_usage()
        sys.exit("too many inputs")
    elif len(args) == 1:
        project_name = args[0]
    else:
        project_name = 'skeleton'

    os.mkdir(project_name)
    os.chdir(project_name)
    for egg in sys.path:
        if re.search('skeleton',egg):
            zip=zipfile.ZipFile(egg)
            zip.extract('skeleton.tar.gz')
            with tarfile.open("skeleton.tar.gz") as tar:
                tar.extractall()
            break

    #delete the tar.gz file
    os.remove("skeleton.tar.gz")

    if project_name == 'skeleton':
        sys.exit()
    # rename directory
    os.rename('skeleton',project_name)

    #replace the file contents :skeleton -> project_name
    import fileinput
    allfile = [os.path.join(path,f) for path,dirs,files in os.walk('.') if files for f in files]
    def process(line):
        return line.replace('skeleton',project_name)
    with fileinput.input(files=allfile,inplace=1) as f:
        for line in f:
            print(process(line),end='')



#if __name__ == '__main__':

