#!/usr/bin/python
# -*- coding=utf-8-*-
from bs4 import BeautifulSoup
import lxml
import requests
import re

url = 'https://movie.douban.com/coming'

# 参考：http://www.jb51.net/article/65287.htm
def get_url_result():
    session = requests.session()
    r = session.get(url)
    print r.text

def parse_html():
    with open('test_html.html', 'r') as f:
        soup = BeautifulSoup(f,'lxml')

        #搜标签
        print soup.find(name='ul').li.div.string
        #搜文本,不能模糊(可以正则)
        print soup.find(text='ants')
        emailid_regexp = re.compile("\w+@\w+\.\w+")
        print soup.find(text=emailid_regexp)

        #搜标签属性值(联合条件搜索)
        print soup.find(attrs={'class':'producerlist2', 'class':'name'})


def parse_aiqiyi():
    r = requests.get('http://www.iqiyi.com/a_19rrgja8xd.html')
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    list =  soup.find_all(attrs={'class':'site-piclist_info_describe'})
    for ele in list:
        print ele.a.string, ele.find('a').get('href')
        #print ele.find('a').get('href')

if __name__ == '__main__':
    parse_html()