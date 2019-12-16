from urllib import request
from urllib import parse

#get方式
response1 = request.urlopen("http://httpbin.org/get", timeout=1)
# print(response1.read())

#post方式
data = bytes(parse.urlencode({"word": "hello"}), encoding="utf-8")
response2 = request.urlopen("http://httpbin.org/post", data=data)
# print(response2.read())

import socket
import urllib

try:
    response3 = urllib.request.urlopen("http://httpbin.org/get", timeout=0.001)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")
    else:
        print("Other")