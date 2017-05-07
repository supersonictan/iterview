#!/usr/bin/python
# -*- coding=utf-8-*-
from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://movie.douban.com/coming'

# 参考：http://www.jb51.net/article/65287.htm
def get_url_result():
    session = requests.session()
    r = session.get(url)
    print r.text

def parse_html():
    with open('test_html.html', 'r') as f:
        soup = BeautifulSoup(f,'lxml')
        print soup.find('ul').li.div.string
        #print first_ul.li.div.string



if __name__ == '__main__':
    parse_html()