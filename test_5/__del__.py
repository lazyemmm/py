"""
    我们知道，Python 通过调用 __init__() 方法构造当前类的实例化对象，而本节要学的 __del__() 方法，功能正好和 __init__() 相反，其用来销毁实例化对象。
    事实上在编写程序时，如果之前创建的类实例化对象后续不再使用，最好在适当位置手动将其销毁，释放其占用的内存空间（整个过程称为垃圾回收（简称GC））。
    大多数情况下，Python 开发者不需要手动进行垃圾回收，因为 Python 有自动的垃圾回收机制（下面会讲），能自动将不需要使用的实例对象进行销毁。
    无论是手动销毁，还是 Python 自动帮我们销毁，都会调用 __del__() 方法。举个例子：
"""
class CLanguage:
    def __init__(self):
        print("调用 __init__() 方法构造对象")
    def __del__(self):
        print("调用__del__() 销毁对象，释放其空间")
clangs = CLanguage()
del clangs




"""
    但是，读者千万不要误认为，只要为该实例对象调用 __del__() 方法，该对象所占用的内存空间就会被释放。举个例子：
"""
class CLanguage1:
    def __init__(self):
        print("调用 __init__()1 方法构造对象")
    def __del__(self):
        print("调用__del__()1 销毁对象，释放其空间")
clangs1 = CLanguage1()
# 添加一个引用clangs对象的实例对象
cl = clangs1
del clangs1
print("***********")
"""
分析：
    可以看到，当程序中有其它变量（比如这里的 cl）引用该实例对象时，即便手动调用 __del__() 方法，该方法也不会立即执行。这和 Python 的垃圾回收机制的实现有关。
    Python 采用自动引用计数（简称 ARC）的方式实现垃圾回收机制。该方法的核心思想是：每个 Python 对象都会配置一个计数器，
    初始 Python 实例对象的计数器值都为 0，如果有变量引用该实例对象，其计数器的值会加 1，依次类推,反之，每当一个变量取消对该实例对象的引用，计数器会减 1。
    如果一个 Python 对象的的计数器值为 0，则表明没有变量引用该 Python 对象，即证明程序不再需要它，此时 Python 就会自动调用 __del__() 方法将其回收。
    以上面程序中的 clangs 为例，实际上构建 clangs 实例对象的过程分为 2 步，
        先使用 CLanguage() 调用该类中的 __init__() 方法构造出一个该类的对象（将其称为 C，计数器为 0），并立即用 clangs 这个变量作为所建实例对象的引用（ C 的计数器值 + 1）。
        在此基础上，又有一个 clang 变量引用 clangs（其实相当于引用 CLanguage()，此时 C 的计数器再 +1 ），
        这时如果调用del clangs语句，只会导致 C 的计数器减 1（值变为 1），因为 C 的计数器值不为 0，因此 C 不会被销毁（不会执行 __del__() 方法）。
"""






class CLanguage2:
    def __init__(self):
        print("调用 __init__()2 方法构造对象")
    def __del__(self):
        print("调用__del__()2 销毁对象，释放其空间")
clangs2 = CLanguage2()
# 添加一个引用clangs对象的实例对象
cl2 = clangs2
del clangs2
print("***********")
del cl2
print("------------")
"""
分析：
    当执行 del cl 语句时，其应用的对象实例对象 C 的计数器继续 -1（变为 0），对于计数器为 0 的实例对象，Python 会自动将其视为垃圾进行回收
"""