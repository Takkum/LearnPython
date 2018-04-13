# function_param.py
# coding:utf-8

#参数在定义函数的圆括号中指定 通过(,)进行分隔
#定义函数时给定的名称叫形参Parameters 
#调用函数时提供给函数的值叫实参Arguments


def print_max(a,b):   #a,b为形参
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal to', b)
	else:
		print(b, 'is maximum')

#直接传递字面值
print_max(3,4)  

#以参数形式传递
#x y为实参
x = 5
y = 7
print_max(x,y)



























