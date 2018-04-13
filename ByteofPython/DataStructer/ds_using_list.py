# ds_using_list.py
# coding:utf-8

# This is my shopping list

# list is mutable but string is immutable
# create a list using list = []
# at least has append() sort() method
# want to see more,please help(list) 
# list is a sequence 


shoplist = ['apple','mango','carrot','banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:',end=' ')
for item in shoplist:
	print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('Now my shopping list is',shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shop list is',shoplist)

print('The first item I will buy is', shoplist[0])

olditem = shoplist[0]	# list取元素是用list[Number]
del shoplist[0]

print('I bought the', olditem)
print('My shop list is now',shoplist)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	