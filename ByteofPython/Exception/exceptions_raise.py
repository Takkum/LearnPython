# exceptions_raise.py
# coding:utf-8

# 引发raise异常
# 要提供错误名或异常名以及要抛出Thrown的对象

class ShortInputException(Exception):
	'''一个由用户定义的异常类'''
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something --> ')
	if len(text) < 3:
		raise ShortInputException(len(text),3)
except EOFError:
	print('Why did you do an EOF on me?')
except ShortInputException as ex:
	print('ShortInputException: The input was ' + '{0} long, excepted at least {1}'.format(ex.length,ex.atleast))
else:
	print('No exception was raised.')
	






































