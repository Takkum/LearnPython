# io_input.py
# coding:utf-8

# 用户输入输出

# 通过切片将序列里的内容转置的tip
def reverse(text):
	return text[::-1]
	
# 判断是不是回文	
def is_palindrome(text):
	text = preprocess(text)
	return text == reverse(text)

# 忽略文本的空格、标点和大小写
def preprocess(text):
	# 都变成小写
	text = text.lower()
	
	# 删掉空格
	# strip() "   xyz   "  -->  "xyz"
	# lstrip() "   xyz   "  -->  "xyz   "
	# rstrip() "   xyz   "  -->  "   xyz"
	# replace(' ','')  "   x y z   "  -->  "xyz"
	text = text.replace(' ','')
	
	# 删掉英文标点符号
	# 需要导入string里的punctuation属性
	import string
	for char in string.punctuation:
		# 为什么这里一定要用自身去替换
		# text1 = text.replace(char,'')
		text = text.replace(char,'')
	return text
	
something = input("Enter text: ")

if is_palindrome(something):
	print('Yes, it is a palindrome.')
else:
	print('No, it is not a palindrome')


























































