# ds_using_dict.py
# coding:utf-8

# 字典将键值(Keys)与值(Values)联系到一起
# 键值必须是唯一的，而且键值必须是不可变(immutable)的对象(str)
# 值可以是可变或者不可变的对象
# create a dictionary dict = {key1:value1,key2:value2}
# 成对的键值-值不会排序
# 字典是属于dict类下的实例
# 字典不是序列
# 字典只能根据key来确定

# ab作为Address Book缩写
ab = {
	'Swaroop':'swaroop@swaroopch.com',
	'Larry':'larry@wall.org',
	'Matsumoto':'matz@ruby-lang.org',
	'Spammer':'spammer@hotmail.com'
}

# use key to find its value
print("Swaroop's address is",ab['Swaroop'])

# delete a pair of key-value
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():		#items() 返回一个包含元组的列表
	print('Contact {} at {}'.format(name,address))

# add a pair of key-value
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:		#in运算符 可以来检查某对键值-值配对是否存在
	print("\nGuido's address is", ab['Guido'])
	
# 了解更多的有关dict类的方法 help(dict)
# 其实在定义函数的参数列表时，就是指定了键值-值配对










































