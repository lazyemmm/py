"""
logging模块可以非常容易地记录错误信息
日志级别： debug < info < warning < error < critical

    logging.basicConfig(
        level=logging.DEBUG,  # 控制台打印的日志级别
        filename='new.log',
        filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志，a是追加模式，默认如果不写的话，就是追加模式
        format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
    )
"""

import logging
logging.basicConfig(level=logging.ERROR, filename='new.log')


try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

print()

try:
    print('try...')
    r = 10 / int('0')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')


print()

print('-----------------')


def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except ZeroDivisionError as e:
        logging.exception(e)  # 虽然也会报错，但是程序会继续执行下去，可以通过配置logging 将错误消息输出到文件中

main()
print('END')
