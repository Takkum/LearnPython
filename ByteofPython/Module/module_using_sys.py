# module_using_sys.py
# coding:utf-8

# 通过函数我们可以重用代码
# 通过模块Modules我们可以重用函数

# 编写模块 一种方法是编写一个.py后缀的文件
# 还有就是使用编写Python解释器的本地语言来编写模块 
# 比如  使用C语言来撰写Python模块


# 标准库模块
import sys


print('The command line arguments are:')
for item in sys.argv:
	print(item)

print('The PYTHONPATH is', sys.path,'\n')
























