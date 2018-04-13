# io_input.py
# coding:utf-8

# �û��������

# ͨ����Ƭ�������������ת�õ�tip
def reverse(text):
	return text[::-1]
	
# �ж��ǲ��ǻ���	
def is_palindrome(text):
	text = preprocess(text)
	return text == reverse(text)

# �����ı��Ŀո񡢱��ʹ�Сд
def preprocess(text):
	# �����Сд
	text = text.lower()
	
	# ɾ���ո�
	# strip() "   xyz   "  -->  "xyz"
	# lstrip() "   xyz   "  -->  "xyz   "
	# rstrip() "   xyz   "  -->  "   xyz"
	# replace(' ','')  "   x y z   "  -->  "xyz"
	text = text.replace(' ','')
	
	# ɾ��Ӣ�ı�����
	# ��Ҫ����string���punctuation����
	import string
	for char in string.punctuation:
		# Ϊʲô����һ��Ҫ������ȥ�滻
		# text1 = text.replace(char,'')
		text = text.replace(char,'')
	return text
	
something = input("Enter text: ")

if is_palindrome(something):
	print('Yes, it is a palindrome.')
else:
	print('No, it is not a palindrome')


























































