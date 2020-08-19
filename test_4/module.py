"""
    模块基本是一个包含了所有你定义的函数和变量的文件。为了在其他程序中重用模块，模块的文件名必须以.py为扩展名。
    利用import语句输入sys模块。sys模块包含了与Python解释器和它的环境有关的函数
    sys.argv变量是一个字符串的列表。特别sys.argv包含了命令行参数的列表。
    记住：脚本的名称总是sys.argv列表的第一个参数。
"""

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print(f'\n\nThePYTHONPATH is{sys.path}\n')

print(__name__)