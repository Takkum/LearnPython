# io_pickle.py
# coding:utf-8

# Python中提供了一个Pickle Module
# 它可以将Python对象存储到一个文件中 这样可以 持久地Persistently存储对象
# dump 与 load

import pickle

# 存储对象的文件名
shoplistfile = 'shoplist.data'

# list里的东西
shoplist = ['apple','mango','carrot']

# 写到文件里
f = open(shoplistfile,'wb')	#以二进制模式写入

# Dump the object to a file		(Pickling)
pickle.dump(shoplist,f)
f.close()

# 销毁shoplist变量
del shoplist

# 从文件再次读入
f = open(shoplistfile,'rb')

# Load the object from the file		(Unpickling)
storedlist = pickle.load(f)

print(storedlist)
































































