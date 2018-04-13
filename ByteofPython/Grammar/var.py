# var.py
# coding:utf-8

i = 5
print(i)

i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)

#逻辑行(在shell里显示的一行)与物理行(在编辑器里看到的一行)
#如果代码很长，那可以使用(\)将其拆分成多个物理行  这叫做显式行连接
#在list里，即括号里的内容 直接回车可以被拆分成多个物理行 这叫做隐式行连接
s = 'This is a string.\
This continues the string.'
print(s)
    

#缩进indentation
#相同缩进的一组语句被称为块block
i = 5
print('value is ',i) 
print('I repeat, the value is ',i)

#  *乘号 不仅可以给出两个数的积，还可以返回字符串重复指定次数后的结果
print( '2 * 3 = ',2 * 3 )
print('hello,world!\t'*3)

# ** 乘方 返回x的y次方
print('2^10 = ',2 ** 10 )

# // 整除 x除以y并对结果向下取整至最接近的整数。
print('13 // 3 = ',13//3)
print('-13 // 3 = ',-13//3)

# << 左移1位在二进制里是*2   2<<1 = 4   10 100 
# >> 右移1位在二进制里是/2,小数部分舍去   2>>1 = 2   10 01; 11>>1 = 5  1011 101    
print('2 << 1 = ',2<<1)
print('2 >> 1 = ',2>>1)
print('11 >> 1 = ',11>>1)

#大于(<) 小于(>) 在Python里可以组成链接
#等于(==) 比较两个对象是否相等
#在比较时应该是同一类型 否则结果永远为False
#布尔运算 not and  or 
#按位或(|)位数不够的在高位补0   按位与(&) 按位异或(^) 按位取反(~)
#Python与C一样都遵循短路计算
print('2 < 3 < 4 is',2<3<4)
print('4 > 3 > 2 is',4>3>2)
print('2 < 3 > 4 is',2<3>4)
print('2 < 3 > 1 is',2<3>1)


























