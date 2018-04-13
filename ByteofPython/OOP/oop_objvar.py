# oop_objvar.py
# coding:utf-8

# 字段是绑定到Bound类或者对象的命名空间Namesoace的变量
# 这些变量仅在类与对象所存在的上下文中有效 这就是他们被称作命名空间的原因


# 类变量是共享的  他们可以被属于该类的所有实例访问 它只有一个副本
# 对象变量由类的每一个独立的实例所拥有 它有属于自己的副本

class Robot:
	'''表示有一个带有名字的机器人。'''
	# 一个类变量，用来计数机器人数量
	population = 0
	
	def __init__(self,name):
		'''初始化数据'''
		self.name = name
		print('(Initializing {})'.format(self.name))
		
		# 当有机器人被创建时，机器人
		# 将会增加人口数量
		Robot.population += 1
	
	def die(self):
		'''我挂了。'''
		print("{} is being destroyed!".format(self.name))
		Robot.population -= 1
		
		if Robot.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {:d} robots working.".format(Robot.population))
	
	def say_hi(self):
		'''来自机器人的诚挚问候
			
		没问题，你做得到。'''
		print('Greetings, my masters call me {}.'.format(self.name))
		
	# 装饰器
	@classmethod
	def how_many(cls):
		'''打印出当前人口数量'''
		print("We have {:d} robots.".format(cls.population))
		
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
# 等价于 self.__class__.how_many()
# 在数据成员前面用双下划线作为前缀 __privatevar 
# Python会使用名称调整Name-mangling 使其成为一个私有变量


# 访问类的文档说明
# Robot.__doc__
# 访问类的方法的文档说明
# Robot.say_hi.__doc__
print(Robot.__doc__)
print(Robot.__init__.__doc__)
print(Robot.how_many.__doc__)





















