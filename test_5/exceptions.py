"""
    使用try...except语句来处理异常。我们把通常的语句放在try-块中，而把错误处理语句放在except-块中
    把所有可能引发错误的语句放在try块中，然后在except从句/块中处理所有的错误和异常。
    except从句可以专门处理单一的错误或异常，或者一组包括在圆括号内的错误/异常。
    如果没有给出错误或者异常的名称，它会处理所有的错误和异常。
    对于每个try从句，至少都有一个相关联的except从句。
    如果某个错误或异常没有被处理，默认的python处理器就会被调用。它会终止程序的运行，并且打印一个消息。
    还可以让try..catch块关联上一个else从句。当没有异常发生的时候，else从句将被执行。


    引发异常:
        可以使用raise语句引发异常，你需要指明错误/异常的名称和伴随异常触发的异常对象。你可以引发的错误和异常应该分别是一个Error或Exception类的直接或间接导出类。
"""

class ShortInputException(Exception):
    '''
        A user-defined exception class.
    '''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = input('Enter something-->')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException as x:
    print('ShortInputException: The input was of length %d,\n was expecting at least %d' % (x.length, x.atleast))
else:
    print('No exception was raised.')

