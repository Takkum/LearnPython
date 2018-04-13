# function_local.py
# coding:utf-8

# 在函数内部声明变量时，它不会与函数外部的同名变量产生关系
# 它的作用域Scope仅在函数内部

x = 50
def func(x):
	print('global x is', x)
	x = 2
	print('change local x to', x)

func(x)
print('global x is still', x)








