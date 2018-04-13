# oop_methond.py
# coding:utf-8

# 类的方法与普通函数不一样的地方在于  它的参数列表必须带有一个self(参数名字叫self是约定俗成的)参数，而且必须是开头
# 不需要为self赋值 
# example:	Myclass 类下面有一个实例 myobject 
# 			你去调用它的方法 myobject.method(arg1,arg2)
# 			Python会把它自动转成Myclass().(myobject,arg1,arg2)
# 所以即使你没有其他的参数，self参数也是必须的。self参数相当于Java的this指针		  	

class Person:
	# @classmethod
	# 在加了上面那句装饰器以后就可以通过Person.say_hi()直接调用了
	# 否则就要用Person().say_hi()来调用
	def say_hi(self):
		print('Hello, how are you?')
	
p = Person()
p.say_hi()
# 上面两句也等价于 Person().say_hi()
Person().say_hi()







































