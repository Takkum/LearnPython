# stdlib_logging.py
# coding:utf-8

# ��־ģ��

import os
import platform 
import logging

if platform.platform().startswith('Windows'):
	# �ҳ�����������C�̣�
	# �ҳ����ļ���
	# ����ϣ��������Ϣ���ļ���
	# ���������ֻ��һ��
	logging_file =  os.path.join(os.getenv('HOMEDRIVE'),os.getenv('HOMEPATH'),'test.log')
else:
	# ������������ϵͳ ����Ҫ֪�����ļ���λ�þ�OK��
	logging_file = os.path.join(os.getenv('HOME'),'test.log')

print(os.getenv('HOMEDRIVE'))
print(os.getenv('HOMEPATH'))
print('Logging to', logging_file)


# ���濪ʼ��֯log�ļ�
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s : %(levelname)s : %(message)s',
	filename=logging_file,
	filemode='w',
)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')






























































