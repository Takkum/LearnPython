# oop_subclass.py
# coding:utf-8

# 继承
# 基类 Base Class 或者超类 Superclass
# 派生类 Derived Class 或者子类 Subclass

class SchoolMember:
	'''代表任何学校里的成员。'''
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: {})'.format(self.name))
	
	def tell(self):
		'''告诉我有关的细节。'''
		print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ")
	
	
class Teacher(SchoolMember):
	'''代表一位老师。'''
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print('(Initialized Teacher: {})'.format(self.name))
	
	def tell(self):
		SchoolMember.tell(self)
		# {:d} 代表输出的是整数 C语言里面就是%d
		print('Salary: "{:d}"'.format(self.salary))
	
class Student(SchoolMember):
	'''代表一位学生。'''
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print('(Initialized Student:{})'.format(self.name))
		
	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs.Wang',40,30000)
s = Student('Swaroop',25,95)

# 打印一行空白
print()

members = [t,s]
for member in members:
	# 对师生
	member.tell()

















































