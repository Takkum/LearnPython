# ds_str_methods.py
# coding:utf-8

# str���෽������help(str)

name = 'Swaroop'

if name.startswith('Swa'):	#startswith()���ڲ����ַ����Ƿ��Ը������ַ������ݿ�ͷ
	print('Yes, the string starts with "Swa"')

if 'a' in name:		#in��������Լ��������ַ����Ƿ��ǲ�ѯ���ַ����е�һ����
	print('Yes, it contains the string "a"')
	
if name.find('war') != -1:	#find()���ڶ�λ�ַ����и��������ַ�����λ��
							#����Ҳ������򷵻�-1��
	print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print(delimiter.join(mylist))	#join()�������������е���Ŀ�������ַ�������Ϊÿһ��Ŀ���
								#�ָ��������Դ˷���һ��������ַ���
































