# mymodule_demo2.py
# coding:utf-8

from mymodule import say_hi,__version__

say_hi()
print('Version', __version__)

# 还可以使用 from mymodule import *
# 它可以导入say_hi等所有公共名称，但不会导入__version__这种双下划线开头的

















