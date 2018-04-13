# return_values.py
# coding:utf-8

# 让一个函数返回两个或多个不同的值

def get_morevalues():
	shoplist = ['apple','mango','carrot']
	str = 'This is the second value'
	a = 3
	# 通过一个元组就可以返回多个值
	return(shoplist,str,a)

# Unpackage 要注意数量要对应

first_value,second_value,third_value = get_morevalues()

print(first_value)
print(second_value)
print(third_value)

# Python中交换两个变量的方法
# a,b = some expression 会把表达式的结果解释为具有两个值的一个元组
a = 5
b = 8
print('a = {}, b = {}'.format(a,b))
a,b = b,a
print('a = {}, b = {}'.format(a,b))

# 单个语句块
# 如果语句块只包括单独的一句语句 那么你可以在同一行指定它
# 当然这种方法不建议使用
flag = True
if flag: print('Yes')









































































