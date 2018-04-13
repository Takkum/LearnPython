# io_using_file.py
# coding:utf-8

# 文件读写

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

# 'r'阅读 'w'写入 'a'追加
# 't' 文本模式  'b'二进制模式

# 打开文件以编辑('w')
f = open('poem.txt','w')

# 向文件中编写文本
f.write(poem)

# 关闭文件
f.close()
	
# 如果没有特别指定，将假定启用默认的'r'模式
f = open('poem.txt')
while True:
	# readline() 读取文件的每一行还包括了行末尾的换行符
	line = f.readline()
	# 长度为零指示 EOF
	# 当返回一个空字符串时，表示我们已经到了文件末尾要退出循环
	if len(line) == 0:
		break
	# 每行line的末尾都有换行符因为他们是从一个文件中进行读取的
	print(line,end='')

# 关闭文件
f.close()







































































