# function_local.py
# coding:utf-8

# �ں����ڲ���������ʱ���������뺯���ⲿ��ͬ������������ϵ
# ����������Scope���ں����ڲ�

x = 50
def func(x):
	print('global x is', x)
	x = 2
	print('change local x to', x)

func(x)
print('global x is still', x)








