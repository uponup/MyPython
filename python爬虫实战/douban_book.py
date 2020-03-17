import requests
import re

def spider(page):
    url = "https://read.douban.com/j/kind/"
    html = request_html(url, page)
    items = request_parse(html)
    return items

def request_html(url, page):
    param = {
        "sort": "hot",
        "page": 2,
        "kind": 105,
        "query": "",
        "variables": {}
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    response = requests.post(url, data=param, headers=headers)

    print(response)
    return response.text

def request_parse(html):
    print(html)
    pattern = re.compile(r'<li(.*?)data-works-id=.*?</li>', re.S)
    items = re.findall(pattern, html)
    return items

def save_csv(items):
    print("保存..")

if __name__ == "__main__":
    spider(1)