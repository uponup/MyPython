import requests
from bs4 import BeautifulSoup



url = 'https://www.infoq.cn'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}

def craw2(url):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    print(response.text)
    result = soup.find_all('div', class_="article-item image-position-right")
    print(result)
    for rs in result:
        print(rs)

craw2(url)