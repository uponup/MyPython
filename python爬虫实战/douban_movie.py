import requests
import json
import re

def spider(page_start):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page_start)
    html = request_url(url)
    response_parse(html)



def request_url(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    try:
        html = requests.get(url, headers=header)
        return html.text
    except requests.RequestException:
        return None

def response_parse(html):
    print(html)
    pattern = re.compile(r'<a.*?href="(.*?)".*?<img src="(.*?)".*?alt="(.*?)".*?<strong>(.*?).*?</a>"', re.S)
    items = re.findall(pattern, html)
    print(items)
    for i in items:
        print(i)

if __name__ == "__main__":
    spider(1)