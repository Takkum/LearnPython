# exceptions_handle.py
# coding:utf-8

# 异常的处理
# try...except
# 通常的语句在try块里  错误处理器放在except块里


try:
	text = input('Enter something --> ')
except EOFError:
	print('Why did you do an EOF on me?')
except KeyboardInterrupt:
	print('You cancelled the operation.')
else:
	print('You entered {}'.format(text))
	
# 如果 except 后面不指定错误名称 那么就是处理所有错误
# else 将在没有发生异常的时候执行


	





































