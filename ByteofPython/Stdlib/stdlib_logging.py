# stdlib_logging.py
# coding:utf-8

# 日志模块

import os
import platform 
import logging

if platform.platform().startswith('Windows'):
	# 找出主驱动器（C盘）
	# 找出主文件夹
	# 我们希望储存信息的文件名
	# 将这三部分汇聚一起
	logging_file =  os.path.join(os.getenv('HOMEDRIVE'),os.getenv('HOMEPATH'),'test.log')
else:
	# 对于其他操作系统 秩序要知道主文件夹位置就OK了
	logging_file = os.path.join(os.getenv('HOME'),'test.log')

print(os.getenv('HOMEDRIVE'))
print(os.getenv('HOMEPATH'))
print('Logging to', logging_file)


# 下面开始组织log文件
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s : %(levelname)s : %(message)s',
	filename=logging_file,
	filemode='w',
)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')






























































