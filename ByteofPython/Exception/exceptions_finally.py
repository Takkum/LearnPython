# exceptions_finally.py
# coding:utf-8

# try ... finally
# 主要是用在文件里面

import sys
import time

f = None
try:
	f = open('poem.txt')
	
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line,end='')
		# 以便print的内容可以被立即打印到屏幕上
		sys.stdout.flush()
		print('Press ctrl+c now')
		
		# 每打印一行后插入两秒休眠，让程序运行得比较缓慢
		time.sleep(2)
except IOError:
	print('Could not find file poem.txt')
except KeyboardInterrupt:
	print('!! You cancelled the reading from the file.')
finally:
	if f:	# 这句话记得要
		f.close()
	print('(Clearning up:Closed the file)')
































































