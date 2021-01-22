#!/usr/bin/env python
# -*-coding:utf-8-*-


from distutils.core import setup, Extension


def main():
    setup(
        ext_modules=[Extension("pyskeleton.ctest", ["src/ctest/ctest.c"])]
    )


if __name__ == "__main__":
    main()
