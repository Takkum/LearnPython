# oop_init.py
# coding:utf-8

# Python中有很多方法的名称具有特殊意义
# __init__方法在类的对象被实例化Instantiated时运行（类似Java构造函数）
# __init__方法用来初始化操作

class Person:
	def __init__(self,name):
		self.name = name
		
	def say_hi(self):
		print('Hello, my name is {0}'.format(self.name))

p = Person('takkum')
p.say_hi()






























