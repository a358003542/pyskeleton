
import os
import sys
import tarfile

if sys.version_info >= (3, 3):
    from os import replace
else:
    # POSIX rename() is always atomic
    from os import rename as replace

with tarfile.open("pyskeleton.tar.gz", "w:gz") as tar:
    for name in ["setup.cfg", "LICENSE", "README.md", "requirements.txt",
                "pyproject.toml",
                 "tests", "MANIFEST.in", ".gitignore"]:
        tar.add(name)

replace('pyskeleton.tar.gz', 'src/pyskeleton/pyskeleton.tar.gz')

