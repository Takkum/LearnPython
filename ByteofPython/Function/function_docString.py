# function_docString.py
# coding:utf-8

def print_max(x,y):
	# �����Ǹú������ĵ��ַ���DocString
	# ��һ���Դ�д��ĸ��ͷ���Ծ�Ž���������������������á�
	# �ڶ����ǿ��С�
	# �����п�ʼ����ϸ�Ľ���˵��
	# ���ĵ��г������Ļᱨ�� ��һ���⻹û���
	'''Prints the maximum of two number.
	
		The two values must be integers.'''
	
	x = int(x)
	y = int(y)
	
	if x > y:
		print(x, 'is maximum')
	else:
		print(y, 'is maximum')
		
print_max(3,5)
print(print_max.__doc__)
help(print_max)


# ������__doc__���Կ��Ի�ȡ�ĵ��ַ������ݡ�
# ��ΪPython���еĶ������ǿ�������һ������ 
	
	
	
	
	
	
	
	
	
	
	
	
	