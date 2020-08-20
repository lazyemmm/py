"""
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
"""

class Myobject:
    def __init__(self, name):
        Myobject.name = name
        self.gender = "male"

o = Myobject('Tom')
print(o.name)

o1 = Myobject('LiMing')
print(o1.gender)

print(getattr(o1, 'name'))  # 获取指定对象的某个属性值
print(hasattr(o1, 'genders'))  # 判断指定对象是否含有某个属性(返回bool值)
setattr(o1, 'name', 'Lily')  # 设置指定对象的某个属性的值
print(getattr(o1, 'name'))

