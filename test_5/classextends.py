"""
继承：类之间的类型和子类型关系
    支持多继承，但不建议 (当一个子类有多个直接父类时，该子类会继承得到所有父类的方法，但是如果其中有多个父类包含同名方法会发生什么？此时排在前面的父类中的方法会“遮蔽”后面父类中的方法。)
    例如类A继承类B,C,D
        class A(B,C,D):
代码重用：SchoolMember类被称为 基本类或超类，而Teacher和Student类被称为导出类或者子类

注意：为了使用继承，把基本类的名称作为一个元组跟在定义类时的类名称之后。
"""
class SchoolMember:
    'Represents any school member.'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember:%s)' % self.name)

    def tell(self):
        'Tell my details.'
        print('Name:"%s" Age:"%s"' % (self.name, self.age))


class Teacher(SchoolMember):
    'Represents a teacher.'

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # 调用父类的构造方法
        self.salary = salary
        print('(Initialized Teacher:%s)' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "%d"' % self.salary)


class Student(SchoolMember):
    'Represents a student.'

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student:%s)' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"%d"' % self.marks)


t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

print  # prints a blank line

members = [t, s]
for member in members:
    member.tell()

