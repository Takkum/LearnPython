# function_global.py
# coding:utf-8

# Ҫ�붨��һ��global��������Ҫʹ��global�ؼ���

x = 50
def func():
	global x #����˴���xΪglobal���� global x,y,z
	
	print('global x is', x)
	x = 2
	print('change global x to', x)

func()
print('Now global x is', x)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	