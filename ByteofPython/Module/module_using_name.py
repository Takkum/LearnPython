# module_using_name.py
# coding:utf-8



# Ϊ�˽��͵���ģ��Ĵ���
# Python���������ֽ��������ļ�����׺��Ϊ.pyc
# �ֽ��������ļ��Ƕ���������ƽ̨��

#����ʹ��improt ������ from...import

from math import sqrt
print('Square root of 16 is', sqrt(16))



# ģ������ֿ���ȷ�����Ƕ������еĻ��Ǳ�����������е�
# ͨ��ģ���__name__������ʵ��

if __name__ == '__main__':
	print('This program is being run by itself')
else:
	print('I am being imported from another module')

	




























