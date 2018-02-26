#!/usr/bin/env python
# -*-coding:utf-8-*-



import sys
if sys.version_info >= (3, 3):
    from os import replace
else:
    # POSIX rename() is always atomic
    from os import rename as replace
