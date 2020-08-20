"""
    Python提供一个标准的模块：pickle。它可以在一个文件中存储任何python对象，之后你又可以把它完整无缺地读取出来。称为“持久地储存对象”
    另一个模块cpickle，功能和pickle模块完全相同，不过用C语言编写，因此要快很多（比pickle快1000倍）。【python3中无此模块】

    注意：import...as语法，是一种便利方法，以便可以使用更短的模块名称。
    在这个程序的其余部分，我们简称这个模块为p。
    首先以写模式打开一个file对象，调用储存器模块的dump函数，把对象储存到打开的文件中，这个过程称为储存。
    接下来使用pickle模块的load函数的返回来取回对象，称为取储存。
"""
import pickle as p
str = """\
    aaa
    bbbbb
    ccccccc
    ddddddddd
"""
f = open("poem1.txt", 'wb')
p.dump(str, f)
f.close()


f = open("poem1.txt", 'rb')
print(p.load(f))
print('aaa')
f.close()
