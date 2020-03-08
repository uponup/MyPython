
import requests
import re
import json

def main(page):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page)
    html = request_dandan(url)
    request_parse(html)


def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def request_parse(html):
    pattern = re.compile(r'<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        print(item)


def save_book_list(item):
    print('====> 开始写入数据: ' + str(item))
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close

if __name__ == "__main__":
    for i in range(1, 26):
        main(i)


