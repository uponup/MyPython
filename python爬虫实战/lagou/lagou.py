import requests
import logging
import re
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
BASE_URL = 'https://static1.scrape.cuiqingcai.com'
TOTAL_PAGE = 10

def scrape_page(url):
    logging.info('scrape start ...: %s ', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        logging.error('error %s', exc_info=True) #打印tracetraceback错误堆栈信息

def scrape_index(page):
    url = f'{BASE_URL}/page/{page}'
    return scrape_page(url)

def parse_page(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info('detail url：%s', detail_url)
        yield detail_url

def main():
    for page in range(1, TOTAL_PAGE):
        index_html = scrape_index(page)
        detail_urls = parse_page(index_html)
        logging.info('detail urls: %s', list(detail_urls))

if __name__ == "__main__":
    main()
