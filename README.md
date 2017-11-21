# pyskeleton

## 更新说明
1. 移除python2支持
2. 移除pytest强制安装依赖，使用者如果有使用pytest需求，请自行安装之。推荐安装的有：`pytest` `pytest-runner`

不过  `setup.cfg` 这个文件还在，如果您有使用pytest需求，那么可以简单在tests文件夹下编写一些test文件，然后：
```
python setup.py test
```
这样做的好处是，其是直接利用本地修改的源码，也就是一边修改源码一边实时测试。

3. 一般pypi包依赖都推荐在 `requirements.txt` 文件中管理，这更加简便，通过setup.py 有的时候会出一些问题，使用者根据requirements 自行决定pypi包安装方式，这样更灵活一些。

4. 程序逻辑优化。

## description:
a small tool make you creat new python project quickly.

## install

    python setup.py install

or

    pip install pyskeleton


## usage

    pyskeleton newprojectname



## test
use pytest do the test thing, with a little tweak, you can directly test the module like that, even do not need to build the module.

    python setup.py test


