# import os

# 数学
import random

print(random.sample(range(100), 10))
print(random.choice(['Apple', 'HUAWEI', 'XiaoMi', 'SUMSANG']))
print(random.random())
print(random.randrange(6))


# 访问互联网
import urllib

# 时间和日期
from datetime import date

now = date.today()
print('今天：', now)

print(date(2003, 12, 2))

birthday = date(1964, 7, 31)
age = now - birthday
print(age.days / 365)



# 数据压缩
import zlib

s = b'witch whitch has wiht is age older watchwitch whitch has wiht is age older watchwitch whitch has wiht is age older watchwitch whitch has wiht is age older watchwitch whitch has wiht is age older watchwitch whitch has wiht is age older watchwitch whitch has wiht is age older watchwitch whitch has wiht is age older watch'

print('文本长度：', len(s))

t = zlib.compress(s)
print('压缩后长度：', len(t), '\n', '压缩后文本：', t)

print('解压后文本：', zlib.decompress(t))



# 性能度量
from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a, b = b, a', 'a=1; b=2').timeit())



# 测试模块
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests