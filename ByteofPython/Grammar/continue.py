# continue.py
# coding:utf-8

while True:
	s = input('Enter something: ')
	if s == 'quit':
		break
	if len(s) < 3:
		print('The sentence is too small!')
		continue
	print('Input is of sufficent length')
print('Done')