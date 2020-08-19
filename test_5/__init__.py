"""
    __init__方法在类的一个对象被建立时，马上运行
    这个方法可以用来对你的对象做一些你希望的初始化
    注意，这个名称的开始和结尾都是双下划线
    
"""
class Test:
    gender = 'male'
    def __init__(self, name = "Lily"):
        self.nam = name

    def tell(self):
        print(f"please tell me who is {self.nam} and his/her gender is {self.gender}")

p = Test()
p.tell()
