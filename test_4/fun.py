"""
    ##############################
    important:
        ①。参数的传递可以不按照顺序，指定好形参就可以
        ②。形参的有默认值的必须放在形参列表的最后
        ③。没有返回值的return语句等价于return None
    ##############################
"""

"""
    函数通过def关键字定义。def关键字后跟一个函数的表标识符名称，然后跟一对圆括号。
    圆括号之中可以包括一些变量名，该行以冒号结尾。接下来是一块语句，它们是函数体。
"""
def say():
    print("hello world.")

say()

version = '3.7.2'
# 函数形参是在函数定义的圆括号对内指定，用逗号分隔。
def say1(a, b, c):
    print(a, b, c)

say1(10,2,30)

# 默认参数值 【只有在形参表末尾的那些参数可以有默认参数值，即你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。】
# def say2(a, b = 4, c):  # 会报错
def say2(a, b, c = 4):
    print(a, b, c)

say2(10,2)


#
def func():
    global x

    print(f'x is {x}')
    x = 2
    print(f'Changed local x to {x}')

x = 50
func()
print(f'Value of x is {x}')

"""
关键参数
    函数有多个参数，而你只想指定其中的一部分，则可以通过命名来为这些参数赋值----关键参数
    优势:1.不必担心参数的顺序，使用函数变得更加简单。
    　　 2.假设其他参数都有默认值，可以只给我们想要的参数赋值。
    
    def func(a,b=5,c=10):
        print 'a is',a,'and b is',b,'and c is',c
    func(3,7)
    func(25,c=24)
    func(c=50,a=100)
"""


def func(a, b=5, c=10):
    print(f'a is {a}, and b is {b}, and c is {c}')


func(3, 7)
func(25, c=24)
func(c=50, a=100)


"""
    # 文档字符串
    文档字符串的惯例是一个多行字符串，首行以大写字母开始，句号结束。第二行是空行，从第三行开始是详细的描述。
    使用——doc——（注意是双下划线）调用printMax函数的文档字符串属性（属于函数的名称）。
"""
def printMax(x, y):
    '''
        sssssssss
    '''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print(f"{x} is maximum")
    else:
        print(f"{y} is maximum")

printMax(3, 5)
print(printMax.__doc__)