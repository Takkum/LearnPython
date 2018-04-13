# function_return.py
# coding:utf-8

def maximum(x, y):
	if x > y:
		return x
	elif x == y:
		return 'The numbers are equal'
	else:
		return y

print(maximum(2,3))
print(maximum(2,2))
print(maximum(-5,-2))


# return 默认返回的值是None
# 每一个函数在其末尾隐含了一句 return None
# pass可以不使用return语句 它用于指示一个没有内容的语句块

















