# more_list_comprehension.py
# coding:utf-8

# 用现有的列表中得到一份新列表

listone = [2,3,4]
listtwo = [2*i for i in listone if i > 2]
print(listone)	# listone不变
print(listtwo)




# 在函数中接受元组与字典
# 用 * 作为元组前缀
# 用 ** 作为字典前缀

def powersum(power, *args):
	'''Return the sum of each argument raised to the specified power.'''
	total = 0
	for i in args:
		total += pow(i,power)
	return total

print(powersum(2,3,4,5)) 
print(powersum(2,10))



# Assert语句
# assert用来断言某事是真
# ex：你非常确定你正在使用的列表中至少包含一个元素，想确认这一点，
# 如果其不是真的就跑出一个错误

mylist = ['item']
assert len(mylist) >= 1
print(mylist.pop())

assert len(mylist) >= 1





































