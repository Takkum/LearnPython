# 在Python里 逗号(,) 是将前后字符串连接起来 然后用一个空格隔开
# 所以逗号(,)其实和字符串连接符号(+)效果是差不多的
# 所以用.format(a,b,c) 进行输出
# .format()还能进行输出格式控制

print('I' + 'am' + 'DK.')#没空格
print()

print('I','am','DK'+'.')#最后的.用来判断(,)在最后一个字符串后面会不会加空格
print()
#对浮点数输出的小数点进行控制
fisrtNum = 5.0/3
secondNum = 10.0/4
print('one:{0:.2f},two:{1:.5f}'.format(fisrtNum,secondNum))

#使用(#)填充文本，并使文字尽量处于中间位置
#(^)定义'___hello___'字符串长度为11
print('{0:#^10}'.format('hello'))

#基于关键词输出，主要是在{}里面指定了输出的关键词
#外面的同名变量name sex 不影响输出的值 
name = 'DK'
sex = 'male'
print('{name} is a {sex}'.format(name='DK1',sex='female'))

#print()默认以(\n)结尾
print('a')
print('a',end=' ')
print('b',end='')
print('c')
#tip:最后一个没有空格的话可以这样输出
output = [10,11,12,13,14];
length = len(output);
# for( int i=0; i<length; i++ ):
	# if( i!=length-1 ):
		# print('{}'.format(output[i]),end=' ')
	# print('{}'.format(output([i]))
	

#转义符号
print('This is the first line\nThis is the second line')
print('This is the first line\tThis is also the first line')

#原始字符串 
#在使用正则表达式的时候要使用原始字符串
print('Newlines are indicated by \n')
print('Newlines are indicated by \\n')#或者对转义字符再进行转义
print(r'Newlines are indicated by \n')































