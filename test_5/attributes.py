"""
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
"""

class Myobject:
    def __init__(self, name):
        Myobject.name = name
        self.gender = "male"

    def __getattr__(self, item):
        return item + ' is auto generated.'

o = Myobject('Tom')
print(o.name)

o1 = Myobject('LiMing')
print(o1.gender)

print(getattr(o1, 'name'))  # 获取指定对象的某个属性值
print(hasattr(o1, 'genders'))  # 判断指定对象是否含有某个属性(返回bool值)
setattr(o1, 'name', 'Lily')  # 设置指定对象的某个属性的值
print(getattr(o1, 'name'))

print()
print("==================================================================================")
print()
"""
__getattr__
    正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
    要避免这个错误，除了可以加上一个属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
    可以在__getattr__方法种进行处理
    此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
"""
print(o1.a)
print(o1.b)

print()
print("==================================================================================")
print()





