# module_using_name.py
# coding:utf-8



# 为了降低导入模块的代价
# Python创建按照字节码编译的文件，后缀名为.pyc
# 字节码编译的文件是独立于运行平台的

#尽量使用improt 而不是 from...import

from math import sqrt
print('Square root of 16 is', sqrt(16))



# 模块的名字可以确定它是独立运行的还是被导入进来运行的
# 通过模块的__name__属性来实现

if __name__ == '__main__':
	print('This program is being run by itself')
else:
	print('I am being imported from another module')

	




























