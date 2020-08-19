"""
    from...import语句
    使用from sys import argv语句，可以避免每次使用sys.  来输入argv变量到你的程序中。
    如果你想输入所有sys模块使用的名字，那么你可以使用from sys import*语句。
"""
from module_import import say, version, version1
#Alternative:
#from mymodule import *
say()
print(f'Version is {version}')
print(f'Version1 is {version1}')



print('Simple Assignment')
shoplist = ['apple','mango','carrot','banana']
mylist = shoplist  # 指向同一地址，即同一份数据

del shoplist[0]

print(shoplist)
print(mylist)

print('Copy by making a full slice')
mylist = shoplist[:]  # 复制了一份数据，故指向了不同的地址，不再是同一份数据
del mylist[0]

print(shoplist)
print(mylist)
