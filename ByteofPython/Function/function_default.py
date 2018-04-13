# function_default.py
# coding:utf-8

# 为函数提供默认值
# 通过(=)来为参数指定默认参数值
# 默认参数值是不可变的，即字面值常量

def say(message='Hi',times=1):
	print(message * times)

say()
say('Hello\t')
say('Hello\t',5)

#只有位于参数列表末尾的参数才能被赋予参数值，即在参数列表中
#有默认参数值的参数不能在没有默认参数值的参数前面  因为值是按照参数位置依次分配的
#example：
#def func(a,b=5) right
#def func(a=5,b) wrong


#如果你定义的函数没有形参 但是你调用的时候传递了实参那也会报错

























