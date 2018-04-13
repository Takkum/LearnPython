# function_global.py
# coding:utf-8

# 要想定义一个global变量必须要使用global关键字

x = 50
def func():
	global x #定义此处的x为global变量 global x,y,z
	
	print('global x is', x)
	x = 2
	print('change global x to', x)

func()
print('Now global x is', x)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	