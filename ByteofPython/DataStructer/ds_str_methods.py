# ds_str_methods.py
# coding:utf-8

# str更多方法可以help(str)

name = 'Swaroop'

if name.startswith('Swa'):	#startswith()用于查找字符串是否以给定的字符串内容开头
	print('Yes, the string starts with "Swa"')

if 'a' in name:		#in运算符用以检查给定的字符串是否是查询的字符串中的一部分
	print('Yes, it contains the string "a"')
	
if name.find('war') != -1:	#find()用于定位字符换中给定的子字符串的位置
							#如果找不到，则返回-1。
	print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print(delimiter.join(mylist))	#join()用以联结序列中的项目，其中字符串会作为每一项目间的
								#分隔符，并以此返回一串更大的字符串
































