# io_using_file.py
# coding:utf-8

# �ļ���д

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

# 'r'�Ķ� 'w'д�� 'a'׷��
# 't' �ı�ģʽ  'b'������ģʽ

# ���ļ��Ա༭('w')
f = open('poem.txt','w')

# ���ļ��б�д�ı�
f.write(poem)

# �ر��ļ�
f.close()
	
# ���û���ر�ָ�������ٶ�����Ĭ�ϵ�'r'ģʽ
f = open('poem.txt')
while True:
	# readline() ��ȡ�ļ���ÿһ�л���������ĩβ�Ļ��з�
	line = f.readline()
	# ����Ϊ��ָʾ EOF
	# ������һ�����ַ���ʱ����ʾ�����Ѿ������ļ�ĩβҪ�˳�ѭ��
	if len(line) == 0:
		break
	# ÿ��line��ĩβ���л��з���Ϊ�����Ǵ�һ���ļ��н��ж�ȡ��
	print(line,end='')

# �ر��ļ�
f.close()







































































