from setuptools import setup ,find_packages
import os.path
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#anditional to make  a tar.gz file
#include the setup.py LICENSE README.md tests skeleton examples docs
import tarfile
with tarfile.open("skeleton.tar.gz", "w:gz") as tar:
    for name in ["setup.py","LICENSE","README.md","examples","skeleton", "tests", "docs"]:
        tar.add(name)

setup(
  name='skeleton',
  version='0.01',
  description='the software short description',
  long_description=read('README.md'),
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
  data_files = [('',['skeleton.tar.gz'])],
#  package_data = {"skeleton":['*.txt'],},
#  zip_safe=False,
#  install_requires=['click'],
#  extras_require={'test': ['pytest'],},
  entry_points = {
  'console_scripts' :[ 'skeleton=skeleton.main:console',],
#  'gui_scripts':['xskeleton=skeleton.main:gui'],
  }
)



