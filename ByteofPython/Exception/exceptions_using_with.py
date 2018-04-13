# exceptions_using_with.py
# coding:utf-8

# 在try块中获取资源（也就是open） 然后在finally块中释放资源（也就是close()）
# with语句可以很简单做到这一模式

with open('opem.txt') as f:
	for line in f:
		print(line,end='')

# 文件的关闭交由with ... open来完成
# with 会获取open返回的对象f
# 然后在代码块开始之前调用 f.__enter__函数 
# 在代码块结束之后调用 f.__exit__函数




























