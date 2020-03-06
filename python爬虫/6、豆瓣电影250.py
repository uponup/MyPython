from bs4 import BeautifulSoup
import requests

def spider(num_start):
    url = 'https://movie.douban.com/top250?start=' + str(num_start*25) + '&filter='
    html = request_douban(url)
    parse_response(html)

def request_douban(url):
    try:
       response = requests.get(url)
       if response.status_code == 200:
           return response.text
    except requests.RequestException:
       return None

def parse_response(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find(class_='grid_view').find_all('li')
    for item in items:
        item_name = item.find(class_='title').string
        # item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        # item_author = item.find('p').text
        item_intr = item.find(class_='inq').string
        print('爬取电影：' + item_index + ' | ' + item_name  +' | ' + item_score  +' | ' + item_intr )


if __name__ == "__main__":
    for i in range(0, 10):
        spider(i)
