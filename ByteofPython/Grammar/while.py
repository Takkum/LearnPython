# while.py
# coding:utf-8

#else��֧�ǿ�ѡ�� optional
#����break���else��֧���ᱻִ��

number = 23
running = True
while running:
	guess = int(input('Enter an integer: '))
	if guess == number:
		print('Congratulations, you guessed it.')
		print('(but you do not win any prizes!)')
		#change the Flag
		running = False
	elif guess < number:
		# another block
		print('No, it is a little bigger than that')
	else:
		print('No, it is a little smaller than that')
else:
	print('The while loop is over.')#��������whileѭ������ΪFalse��ʱ��ִ��

print('Done')





























