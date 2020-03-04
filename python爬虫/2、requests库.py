# requests库是在urllib基础上封装的第三方库，非常好用。

import requests

response = requests.get('https://api.github.com/events')
print(response)

response = requests.post('https://httpbin.org/post', data= {'key':'value'})
print(response)

# # 携带更多参数
payload = { "key1": "value1", "key2": "value2", "key3": "value3" }
response = requests.get("https://httpbin.org/get", data= payload)

# 假装自己是浏览器
header = { "user-agent" : "my-app/0.1.1" }
url = 'https://api.github.com/some/endpoint'
response = requests.get(url, header=header)
# 获取响应文本内容
print(response.text)
# 获取更过响应信息
print(response.content)
# 获取返回状态吗
print(response.status_code)
# 获取响应头
print(response.headers)
# 获取json响应内容
print(response.json)
# 获取socket流响应内容
r = requests.get('https://api.github.com/events', stream=True)
print(r.raw.read(10))


# post请求中一个key加多个值
param = [("key", "value1"), ("key", "value2")]
response1 = requests.post("https://httpbin.org/post", data=param)

param2 = { "key" : ["value1", "value2"]}
response2 = requests.post("http://httpbin.org/post", data=param2)

print(response1.text == response2.text)


# 请求的时候，使用json作为参数
param = { "key": "value", "key2": "value2"}
response = requests.post(url, json=param)

# 想上传文件？
url = 'https://httpbin.org/post'
file = {"file": open('rs.txt', 'rb')}
response = requests.post(url, files = file)

# 获取cookie信息
url = 'http://example.com/some/cookie/setting/url'
response = requests.get(url)
print(response.cookies)


# 发送cookie信息
url = 'http://httpbin.org/cookies'
cookies = dict(cookie_are = 'working')
response = requests.get(url, cookie=cookies)


# 设置超时
requests.get(url, timeout=0.01)

