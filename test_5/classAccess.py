"""
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
"""

class Student(object):

    def __init__(self, name, score):
        self.__name = name  # 私有属性(外部不可访问，不可修改)
        self.__score = score  # 私有属性(外部不可访问，不可修改)
        self.name = name  # 公有属性(外部可访问，可修改)
        self.score = score  # 公有属性(外部可访问，可修改)

    def print_score(self):
        print('public------->%s: %s' % (self.name, self.score))
        print('private------>%s: %s' % (self.__name, self.__score))


    def get__name(self):
        return self.__name

    def get__score(self):
        return self.__score

    def setName(self, name):
        self.__name = name

    def setSCore(self, score):
        self.__score = score

t = Student('Tom', 98)
t.print_score()

print(t.name)  # Tom
# print(t.__name)  # 报错 ttributeError: 'Student' object has no attribute '__name'
print()
t.name = 'Lily'
t.print_score()


# 如果想在外部获取私有属性的值，需要增加相应的公有方法去获取
print()
print(t.get__name())
print(t.get__score())


# 同理，如果想在外部修改私有属性，可以增加相应的公有方法去修改设置
print()
t.setName('wuqibao')
t.setSCore(100)
t.print_score()

print()
print(dir(t))