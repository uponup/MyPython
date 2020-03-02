# Python提供了内置的urllib等供Http请求，但是不好用。

# 因此，我们有了Requests模块，其在Python内置模块的基础上进行了高度的封装，从而使得Pythoner进行网络请求时，变得美好了许多，使用Requests可以轻而易举的完成浏览器可有的任何操作。

# Keep-Alive & 连接池
# 国际化域名和 URL
# 带持久 Cookie 的会话
# 浏览器式的 SSL 认证
# 自动内容解码
# 基本/摘要式的身份认证
# 优雅的 key/value Cookie
# 自动解压
# Unicode 响应体
# HTTP(S) 代理支持
# 文件分块上传
# 流下载
# 连接超时
# 分块请求
# 支持 .netrc

import requests

#get
url = "http://httpbin.org/get"
data = { 'key1' : 'value1', 'key2' : 'value2' }
response = requests.get(url, data)
# print(response.text)

#post

url = "http://httpbin.org/post"
data = { 'key1' : 'a', 'key2' : 'b' }
response = requests.post(url, data)
print(response.json())