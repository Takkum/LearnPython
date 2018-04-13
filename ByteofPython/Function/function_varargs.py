# funciton_varargs.py
# coding:utf-8

# 定义的函数里的参数变量是可变的
# 通过(*)实现

# 声明一个诸如*param的星号参数时，从此处开始到结束的所有位置参数parameters
# 将被汇集成一个param的元组Tuple

# 声明一个诸如**param的双星号参数时，从此处开始到结束的所有关键字参数
# 都被汇集成一个param的字典Dictionary

def total(a=5, *numbers, **phonebook):
	print('a', a)
	
	#遍历元组中所有项目
	for single_item in numbers:
		print('single_item', single_item)
	
	#遍历字典中所有项目
	for first_part,second_part in phonebook.items():
		print(first_part,second_part)

total(10,15,21,aa=1,bb=2,cc=4)
print(total(10,15,21,aa=1,bb=2,cc=4))	#这里的None又是怎么回事？






















