# if.py
# coding:utf-8

#Python中没有switch语句
#built-in function 内置函数 input()
#int是一个类，将别的类型转化为整数型

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
#这是最后一句话  在if语句执行完毕后执行



























































































