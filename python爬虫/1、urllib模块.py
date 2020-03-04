
# import urllib.request
from urllib import request

response = request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# 一、request.urlopen中可以填入三个参数
# urllib.request.urlopen(url, data=None, [timeout, ]*)


# 二、模拟浏览器
# 给请求中添加header，可模拟浏览器请求

from urllib import request, parse
import ssl

url = 'https://biihu.cc//account/ajax/login_process/'
headers = {
    #假装自己是浏览器
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'xiaoshuaib@gmail.com',
    'password':'123456789',
    '_post_type':'ajax',
}
data = bytes(parse.urlencode(dict),'utf-8')
req = request.Request(url,data=data,headers=headers,method='POST')
context = ssl._create_unverified_context()
response = request.urlopen(req,context=context)
print(response.read().decode('utf-8'))

