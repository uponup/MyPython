import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

url = 'http://www.baidu.com'
response = requests.get(url, headers=header)
print(response.text)