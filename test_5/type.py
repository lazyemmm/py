"""
使用type创建类
    要创建一个class对象，type()函数依次传入3个参数：
        1.class的名称；
        2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
        3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
"""
def fn(self, name = "LiMing"):
    print(f"his name is {name}")

Hello = type('class', (object,), dict(hello = fn))  # 第二个参数必须为tuple, 尤其注意在只有一个元素的时候，逗号不可少，严格遵守tuple的写法

h = Hello()
h.hello('Lily')
