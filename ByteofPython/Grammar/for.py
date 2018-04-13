# for.py
# coding:utf-8


#内置函数  range() 返回一序列的数字 但是每次只会生成一个数字
#从第一个数字开始到第二个数字结束，默认步长为1。不包括第二个数字
#如果要生成完整的数字列表
#要用list(range(1,5)) 输出[1,2,3,4]
#list(range(1,5,2)) 输出[1,3]
#list(range(3)) 输出[0,1,2]
#else分支是optional     遇到break语句else分支不会被执行


for i in range(1,5): # equals for i in [1,2,3,4]:
	print(i)
else:
	print('The for loop is over')

print(list(range(1,5)))
print(list(range(1,5,2)))
print(list(range(3))) #3表示的是从0开始的数字个数
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	