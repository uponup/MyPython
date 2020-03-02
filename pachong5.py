import requests
import re
url = 'http://www.cnu.cc/discoveryPage/hot-人像'
response = requests.get(url).text

# r代表python中的原始字符串
pattern = re.compile(r'<a href="(.*?)".*?author">(.*?)</div>', re.S)
result = re.findall(pattern, response)

# print(result)

for (url, author) in result:
    print(url, re.sub(r'\s', '', author))




# ===============
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d+')            # 用于匹配至少一个数字
print(pattern)
m = pattern.match('one12twothree34four') # 查找头部，没有匹配
print(m)

m = pattern.match('one12twothree34four', 2, 10) # 从e开始没有匹配
print(m)

m = pattern.match('one12twothree34four', 3, 10) # 从1开始，刚好匹配
print(m.group(0))
print(m.start(0))
print(m.end(0))