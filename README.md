# pyskeleton

## 更新说明
### 1.0.0
移除c语言扩展，本项目保持这样一个快速生成中小型python模块项目的功能的样子，不会再更新了。

### 0.4.0

updated to new structure and add a simple ctest submodule writed in c.

按照setuptools最新建议更新了新的结构写法，并加入了一个ctest小子模块用于测试c语言写的扩展。

### 0.3.6

小优化，还是加入了setup.cfg，某些情况下用户自行决定是否使用 `python setup.py test` 这样的测试方法。

### 0.3.5
现在pypi支持markdown了，做了一些调整。然后移除setup.cfg了。然后试着用twine来完善整个制作过程，和上传wheel包。

### 0.3.3
移除pyosreplace依赖，之前是为了解决python2的兼容性引入的，现在移除了，这样本模块现在不依赖任何模块了，
因为pyosreplace模块还需要调用c编译工具，所以决定移除了。

### 0.3.2
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


