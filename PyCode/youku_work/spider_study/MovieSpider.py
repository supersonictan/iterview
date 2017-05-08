#!/usr/bin/python
# -*- coding=utf-8-*-
from bs4 import BeautifulSoup
import lxml
import requests
import re


#解析url到文本
def get_url_result(list_url, encoding):
    r = requests.get(list_url)
    r.encoding = encoding
    return r.text

def get_movies_link(html):
    soup = BeautifulSoup(html, 'lxml')
    list = soup.find_all(attrs={'class':"ulink"})
    for a_tag in list:
        print a_tag.string + "\thttp://www.ygdy8.net" + a_tag.get('href')

def parse_file_html():
    #html = get_url_result("http://www.ygdy8.net/html/gndy/dyzz/20170504/53865.html", 'gbk')
    r = requests.get("http://www.ygdy8.net/html/gndy/dyzz/20170504/53865.html")
    r.encoding = 'gbk'
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    p = str(soup.find_all('p')[4])
    print p
    pattern = re.compile('译　　名.*<br/>*?')
    matcher = re.search(pattern, p)
    #print matcher.group(1)
    # for ele in str(p).split('◎'):
    #     print  ele.strip()


    #print name


if __name__ == '__main__':
    #http://www.ygdy8.net/html/gndy/dyzz/list_23_161.html
    #res = get_url_result("http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html", 'gbk')
    #get_movies_link(res)
    parse_file_html()