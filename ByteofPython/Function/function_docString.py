# function_docString.py
# coding:utf-8

def print_max(x,y):
	# 下面是该函数的文档字符串DocString
	# 第一行以大写字母开头，以句号结束。阐述这个函数的作用。
	# 第二行是空行。
	# 第三行开始是详细的解释说明
	# 在文档中出现中文会报错 这一问题还没解决
	'''Prints the maximum of two number.
	
		The two values must be integers.'''
	
	x = int(x)
	y = int(y)
	
	if x > y:
		print(x, 'is maximum')
	else:
		print(y, 'is maximum')
		
print_max(3,5)
print(print_max.__doc__)
help(print_max)


# 函数的__doc__属性可以获取文档字符串内容。
# 因为Python所有的东西都是可以视作一个对象 
	
	
	
	
	
	
	
	
	
	
	
	
	