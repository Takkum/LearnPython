# ds_using_tuple.py
# coding:utf-8

# Tuple 可以近似看做列表，但是元组功能没有列表丰富
# 元组类似于字符串 所以 Tuple is immutable
# create a tuple tuple = ()
# tuple is a sequence

zoo = ('python','elephant','penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey','camel',zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are',new_zoo[2])	#Tuple取元素也是 tuple[Number]
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

# 空的元组由一堆圆括号构成 myempty = ()
# 但是只拥有一个项目的元组 必须在第一个（唯一一个）项目后面加上一个逗号
# 这是为了区别这到底是一个元组 还是 只是一个被括号所环绕的对象 
# example：singleton = (2,) sigleton is a tuple object
#          singleton = (2) sigleton is a int object















































 