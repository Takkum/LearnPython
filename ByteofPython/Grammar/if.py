# if.py
# coding:utf-8

#Python��û��switch���
#built-in function ���ú��� input()
#int��һ���࣬���������ת��Ϊ������

number = 23
guess = int(input('Enter an integer: '))
if guess == number:
	# start new block
	print('Congratulations, you guessed it.')
	print('(but you do not win any prizes!)')
	# end new block
elif guess < number:
	# another block
	print('No, it is a little bigger than that')
	
else:
	print('No, it is a little smaller than that')
print('Done')
#�������һ�仰  ��if���ִ����Ϻ�ִ��



























































































