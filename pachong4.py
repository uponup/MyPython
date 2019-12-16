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