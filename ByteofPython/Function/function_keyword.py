# function_keyword.py
# coding:utf-8

# 如果函数有很多参数，但你只希望对其中的一些进行指定，
# 那么可以通过命名而不是位置来指定参数


def func(a, b=5, c=10):
	print('a is', a, 'and b is', b, 'and c is', c)

func(3,7)
func(25,c=24)
func(c=50,a=100)
func(a=50)

#一定要指定a的值 不管是通过命名还是通过位置指定 否则会报错




































