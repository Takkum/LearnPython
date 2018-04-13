# ds_seq.py
# coding:utf-8

# 列表(list)  元组(tuple)  字符串(str)  都可以看做是序列(Sequence)的某种表现形式

# 序列(Sequence)的主要功能是资格测试 也就是 in and not in 和 索引操作
# 序列还有切片(Slicing)运算符  它使我们能够获得序列的一部分


shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'

# Indexing or 'Subscription' operation
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])
                                     
# Slicing on a list
# 切片中冒号(:)是必须的，但是数字是可选的
# 第一个数字是切片开始的位置，第二个数字是切片结束的位置。
# 如果第一个数字没有指定，Python将会从序列起始处开始操作
# 如果第二个数字留空，Python将会在序列的末尾结束操作
# 切片操作将包括起始位置，但不包括结束位置
print('Item 1 to 3 is', shoplist[1:3])	
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])	#不包括-1
print('Item start to end is', shoplist[:])

# Slice on a character
print('Characters 1 to 3 is', name[1:3])
print('Characters 2 to end is', name[2:])
print('Characters 1 to -1 is', name[1:-1])
print('Characters start to end is', name[:])

# Slice 第三个参数是Step 默认为1
print(shoplist[::1])
print(shoplist[::2])	#得到第0 2 4 ...个项目
print(shoplist[::3])	#得到第0 3 6 ...个项目
print(shoplist[::-1])	#得到第-1 -2 -3 ...个项目，即逆序了
print(shoplist[::-2])	#得到第-1 -3 -5 ...个项目
print(shoplist[::-3])	#得到第-1 -4 -7 ...个项目

















 
