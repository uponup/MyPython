
import requests
import re
import csv

def spider(num_start):
    url = 'https://movie.douban.com/top250?start=' + str(num_start*25) + '&filter='
    html = request_url(url)
    return response_parse(html)



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
    pattern = re.compile(r'<li>.*?<img.*?src="(.*?)".*?<a href="(.*?)".*?<span class="title">(.*?)</span>.*?<p class="">(.*?)<br>(.*?)</p>.*?v:average">(.*?)</span>.*?</div>.*?<span class="inq">(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    print(items)
    return items

def save_csv(items):
    with open('./python爬虫实战/douban_movie.csv', 'a') as csv_file:
        filed_name = ['封皮', '详情', '电影名', '导演主演', '类型', '评分', '一句话评价']
        writer = csv.DictWriter(csv_file, filed_name)
        writer.writeheader()
        for item in items:
            row = {"封皮": item[0], "详情": item[1], "电影名": item[2], "导演主演": item[3], "类型": item[4], "评分": item[5], "一句话评价": item[6]}
            writer.writerow(row)
        csv_file.close()


if __name__ == "__main__":
    items = []
    for i in range(0, 10):
        print("正在爬取第" + str(i) + "页")
        items.extend(spider(i))
    
    save_csv(items)