# return_values.py
# coding:utf-8

# ��һ��������������������ͬ��ֵ

def get_morevalues():
	shoplist = ['apple','mango','carrot']
	str = 'This is the second value'
	a = 3
	# ͨ��һ��Ԫ��Ϳ��Է��ض��ֵ
	return(shoplist,str,a)

# Unpackage Ҫע������Ҫ��Ӧ

first_value,second_value,third_value = get_morevalues()

print(first_value)
print(second_value)
print(third_value)

# Python�н������������ķ���
# a,b = some expression ��ѱ��ʽ�Ľ������Ϊ��������ֵ��һ��Ԫ��
a = 5
b = 8
print('a = {}, b = {}'.format(a,b))
a,b = b,a
print('a = {}, b = {}'.format(a,b))

# ��������
# �������ֻ����������һ����� ��ô�������ͬһ��ָ����
# ��Ȼ���ַ���������ʹ��
flag = True
if flag: print('Yes')









































































