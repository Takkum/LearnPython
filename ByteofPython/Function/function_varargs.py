# funciton_varargs.py
# coding:utf-8

# ����ĺ�����Ĳ��������ǿɱ��
# ͨ��(*)ʵ��

# ����һ������*param���ǺŲ���ʱ���Ӵ˴���ʼ������������λ�ò���parameters
# �����㼯��һ��param��Ԫ��Tuple

# ����һ������**param��˫�ǺŲ���ʱ���Ӵ˴���ʼ�����������йؼ��ֲ���
# �����㼯��һ��param���ֵ�Dictionary

def total(a=5, *numbers, **phonebook):
	print('a', a)
	
	#����Ԫ����������Ŀ
	for single_item in numbers:
		print('single_item', single_item)
	
	#�����ֵ���������Ŀ
	for first_part,second_part in phonebook.items():
		print(first_part,second_part)

total(10,15,21,aa=1,bb=2,cc=4)
print(total(10,15,21,aa=1,bb=2,cc=4))	#�����None������ô���£�






















