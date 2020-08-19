# import
import os
import random
import time

# os ###################################################################################################
print(os.listdir('../'))
print(__file__)

# random ###############################################################################################
# seed(种子)   生成随机数之前  先给随机数一个种子    如果种子相同   随机数也相同
random.seed(20)
print(random.randint(1, 9))  # 3
random.seed(20)
print(random.randint(1, 9))  # 3


# 从序列类型中随机返回一个元素
str = 'abcdef'
list = ['g', 'h', 'i', 'j']
tuple = ('g', 'h', 'i', 'j')
set ={'g', 'h', 'i', 'j'}
random.seed()  # 避免上面的seed值影响测试
print(random.choice(str))
print(random.choice(list))
print(random.choice(tuple))
# print(random.choice(set))  # 报错【因为set类型不支持下标】


# （洗牌）把序列中的元素随机排列，返回打乱后的序列
list1 = [1, 2, 3, 4, 5]
# print(random.shuffle.(list1))  # None
random.shuffle(list1)  # 打乱的是原序列
print(list1)


# (样品)     从pop中随机选取k个元素，以列表的形式返回
print(random.sample(list, 3))


# time ##################################################################################################
dir(time)
second = time.time()
print(second)  # 1597825940.6490638  时间戳
struct_time = time.localtime(second)
print(struct_time)  # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=19, tm_hour=16, tm_min=32, tm_sec=20, tm_wday=2, tm_yday=232, tm_isdst=0)
print(struct_time.tm_year)
print(struct_time.tm_mon)
print(struct_time.tm_mday)
print(struct_time.tm_hour)
print(struct_time.tm_min)
print(struct_time.tm_sec)

print(time.asctime())  # wed Aug 19 16:39:22 2020

# 作用相当于asctime(localtime(secs)),未给参数相当于asctime()
print(time.ctime())  # wed Aug 19 16:39:22 2020
print(time.ctime(1597825940.6490638))  # 可以格式化指定时间戳

# 返回的标准时间(格林尼治时间 时间格式同time.localtime()
print(time.gmtime())     # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=19, tm_hour=8, tm_min=45, tm_sec=52, tm_wday=2, tm_yday=232, tm_isdst=0)
print(time.gmtime(1597825940.6490638))
# 返回当前时区的时间
print(time.localtime())  # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=19, tm_hour=16, tm_min=45, tm_sec=52, tm_wday=2, tm_yday=232, tm_isdst=0)
print(time.localtime(1597825940.6490638))
# 将当前时间格式转为时间戳
print(time.mktime(time.localtime()))

# sleep * 秒
# time.sleep(4)

"""
strftime
    把一个代表时间的元组或者struct_time(如由time.localtime()和time.gmtime()返回)转化为格式化的时间字符串．如果t未指定，将传入time.localtime()，如果元组中任命一个元素越界，将会抛出ValueError异常
    strftime(format[, tuple]) -> string
    Convert a time tuple to a string according to a format specification.
    See the library reference manual for formatting codes. When the time tuple
    is not present, current time as returned by localtime() is used.
 
    Commonly used format codes:
    
    %Y  Year with century as a decimal number.===>完整的年份
    %m  Month as a decimal number [01,12].===>月份(01-12)
    %d  Day of the month as a decimal number [01,31].===>一个月中的第几天(01-31)
    %H  Hour (24-hour clock) as a decimal number [00,23].===>一天中的第几个小时(24小时制，00-23)
    %M  Minute as a decimal number [00,59].===>分钟数(00-59)
    %S  Second as a decimal number [00,61].===>秒(01-61)
    %z  Time zone offset from UTC.===>用+HHMM或者-HHMM表示距离格林威治的时区偏移(H代表十进制的小时数，M代表十进制的分钟数)
    %a  Locale's abbreviated weekday name.===>本地(local)简化星期名称
    %A  Locale's full weekday name.===>本地完整星期名称
    %b  Locale's abbreviated month name.===>本地简化月份名称
    %B  Locale's full month name.===>本地完整月份名称
    %c  Locale's appropriate date and time representation.===>本地相应的日期和时间表示
    %I  Hour (12-hour clock) as a decimal number [01,12].===>一天中的第几个小时(12小时制，01-12)
    %p  Locale's equivalent of either AM or PM.===>本地am或者pm的相应符
"""

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
