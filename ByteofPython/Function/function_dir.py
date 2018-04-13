# function_dir
# coding:utf-8

# dir()函数能够返回由对象所定义的名称列表 
# 如果对象是一个模块 则会包含模块内的函数 类 变量
# dir()函数返回参数模块的名称列表
# 如果没有参数 则返回当前模块的名称列表


import sys
# 给出sys模块的属性名称
print(dir(sys))

# 给出当前模块的属性名称
print(dir())

a = 5
print(dir())

del a
print(dir())


# dir()能对任何对象工作 dir(str)













