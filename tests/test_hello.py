#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyskeleton import print_version


def test_version():
    assert print_version() == '0.3.4'

# if __name__ == '__main__':
