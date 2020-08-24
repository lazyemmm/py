"""
__getattr__
    正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
    要避免这个错误，除了可以加上一个属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
    可以在__getattr__方法种进行处理
    此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误


链式调用
    类的实例化对象不可以被调用，如果想要被调用则需要实现一个__call__方法
"""
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))
    __repr__ = __str__

c = Chain()
print(c.name.age.gender)
print(callable(c))  # False
print(callable(Chain()))  # False
print(callable(Chain))  # True
print(c.users("LiMing").gender)  # 如果没有__call__方法  则会报错，因为类的实例化对象不可以被调用【TypeError: 'Chain' object is not callable】
"""
分析：
    1.第一步
    urls = c = Chain()
    初始化一个实例，此时urls等于，因为定义了默认值path=''；
    
    2.第二步
    urls = urls.users
    查找urls的属性users，没找到定义的属性，那就调用__getattr__方法，返回了一个函数调用：
    def __getattr__(self, users):
        return Chain('%s/%s' % (self.__path, users))
    这一步调用了Chain()，而且把要查找的属性users作为参数传递了进去，也就是Chain(users),那么根据Chain()的逻辑，最后返回的是：/users，然后跟上一步的结果拼接，最终返回：/users；
    
    3.第三步
    urls = urls('LiMing')
    对实例进行直接调用，就会走__call__方法
    def __call__(self, path):
        return Chain('%s/%s/' % (self.path, path))
        
    4.di
"""

