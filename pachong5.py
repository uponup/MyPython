import requests
import re
url = 'http://www.cnu.cc/discoveryPage/hot-人像'
response = requests.get(url).text

pattern = re.compile(r'<a href="(.*?)".*?author">(.*?)</div>', re.S)
result = re.findall(pattern, response)

# print(result)

for (url, author) in result:
    print(url, re.sub(r'\s', '', author))


