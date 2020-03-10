import requests
import re
import csv

def spider(page_start):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page_start)
    html = request_html(url)
    return response_parse(html)


def request_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        return response.text
    except requests.RequestException:
        return None

def response_parse(html):
    pattern = re.compile(r'<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?"tuijian">(.*?)</span>.*?class="publisher_info"><span>(.*?)</span>.*?target="_blank">.*?</a>.*?class="biaosheng">(.*?)<span>(\d+).*?class="price">.*?class="price_n">(.*?)</span>.*?class="price_r">(.*?)</span>.*?class="price_s">(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    return items

def save_csv(items):
    with open('./python爬虫实战/dangdang_book.csv', 'a') as csv_file:
        filed_name = ['序号', '书籍封面', '书名', '推荐', '出版时间', '出版社', '五星评价人数', '现价', '原价', '折扣']
        writer = csv.DictWriter(csv_file, filed_name)
        writer.writeheader()
        for item in items:
            row = {"序号": item[0], "书籍封面": item[1], "书名": item[2], "推荐": item[3], "出版时间": item[4], "出版社": item[5], "五星评价人数": item[6], "现价": item[7], "原价": item[8], "折扣":item[9]}
            writer.writerow(row)
        csv_file.close()


if __name__ == "__main__":
    items = []
    for i in range(1, 26):
        items.extend(spider(i))
    save_csv(items)
