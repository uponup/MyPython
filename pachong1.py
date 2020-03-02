# from urllib import request
# url = "http://www.baidu.com"
# response = request.urlopen(url, timeout=1)
# print(response.read().decode('utf-8'))

from urllib import request
url = "http://www.baidu.com"
response = request.urlopen(url, timeout=1)

# print(response.read().decode('utf-8'))

# Python爬虫架构：调度器，url管理器，网页下载器，网页解析器，应用程序

# 调度器：负责url管理器，网页下载器，网页解析器之间的工作
# url管理器：包括待爬取的url和已爬取的url，防止重复抓取url和循环抓取url，主要通过内存，数据库，缓存数据库来实现
# 网页下载器：通过传入一个url，将网页转换成一个字符串，来下载网页内容。例如：urllib2
# 网页解析器：将字符串的网页数据进行解析
# 应用程序：将从网页中抓取到的有用数据组成一个应用

from urllib.request import Request
from urllib.request import urlopen
from http import cookiejar

# 爬虫的三种方式：
# 1、直接爬取
response = request.urlopen(url, timeout=1)
print(response.code)
print(len(response.read()))

# 2、模拟MMozilla浏览器爬取
request = Request(url)
request.add_header("user-agent", "Mozilla/5.0")
request.add_header("GET", url)
response2 = urlopen(request)
print(response2.code)
print(len(response2.read()))

# 3、添加cookie