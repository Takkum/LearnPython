# ds_reference.py
# coding:utf-8


# ������һ�������Ժ󲢽�������ĳ�������� ���������Refer�ö���
# ���Ǳ��������������� 
# ������ָ�������ڴ��д洢�˸ö������һ����
# �������ư�Binding���Ǹ�����


print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

# mylist ֻ��ָ��ͬһ�������һ������
mylist = shoplist

# ����һ��ɾ��
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# shoplist �� mylist ���߶�û����apple
# ������ǿ���ȷ������ָ����ͬһ������

print('Copy by making a full slice')
# ͨ����Ƭ������һ�ݸ���
mylist = shoplist[:]

#�ٴ�ɾ����һ����Ŀ
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# �������ǳ����˲�ͬ
# ��������ϣ������һ�����еĸ�������ô��������Ƭ������
# ������һ���������������һ�����ƣ���ô���Ƕ�������ͬһ������


















































