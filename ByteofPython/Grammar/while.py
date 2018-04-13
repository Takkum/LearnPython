# while.py
# coding:utf-8

#else分支是可选的 optional
#遇到break语句else分支不会被执行

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
	print('The while loop is over.')#这句语句在while循环条件为False的时候执行

print('Done')





























