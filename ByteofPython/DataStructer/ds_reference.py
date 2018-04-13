# ds_reference.py
# coding:utf-8


# 创建了一个对象以后并将其分配给某个变量后 变量会查阅Refer该对象
# 但是变量不会代表对象本身 
# 变量名指向计算机内存中存储了该对象的那一部分
# 即将名称绑定Binding给那个对象


print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

# mylist 只是指向同一对象的另一种名称
mylist = shoplist

# 将第一项删掉
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# shoplist 和 mylist 二者都没有了apple
# 因此我们可以确定它们指向了同一个对象

print('Copy by making a full slice')
# 通过切片来制作一份副本
mylist = shoplist[:]

#再次删除第一个项目
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 现在他们出现了不同
# 因此如果你希望创建一份序列的副本，那么必须用切片操作。
# 仅仅将一个变量名赋予给另一个名称，那么它们都将查阅同一个对象。


















































