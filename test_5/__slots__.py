"""
使用__slots__可以规定内外部可设置的属性名称
"""
class AA:
    __slots__ = ('name', 'gender')
    def __init__(self, age):
        # self.age = self.age = age  # 报错 因为__slots__中未添加age属性
        pass

    def setAttribute(self, age):
        # self.age = age  # 报错 因为__slots__中未添加age属性
        pass


a = AA(19)
# a.setAttribute(29)


"""
    给类添加类方法则所有实例以及被继承类的实例都可访问该方法
"""
def setGender(self, gender):
    self.gender = gender

AA.setGender = setGender

a.setGender('ttttt')
print(a.gender)

class BB(AA):
    pass


b = BB(23)
b.setGender('bbbbbbbb')
print(b.gender)
