# ds_set.py
# coding:utf-8

# 集合(Set)是无序容器(Collection)
# 当容器中的项目是否存在比起次序，即出现次数更重要的我们就会使用集合
# 集合可以测试某些对象的资格 检查他们是否是其他集合的子集
# 找到两个集合的交集等

bri = set(['brazil','russia','india'])
print('Is India in bri?', 'india' in bri)
print('Is usa in bri?', 'usa' in bri)

bric = bri.copy()
bric.add('China')
print('Is bric the superset of bri?',bric.issuperset(bri))

bri.remove('russia')
# bri & bric 
print("bri and bric 's intersection is", bri.intersection(bric))

















