#!/usr/bin/python
# -*- coding=utf-8-*-
from bs4 import BeautifulSoup
import lxml
import requests
import re

yiming_pattern = re.compile('译　　名.*?<br/>')
year_pattern = re.compile('年　　代.*?<br/>')
area_pattern = re.compile('国　　家.*?<br/>')
area2_pattern = re.compile('地　　区.*?<br/>')
type_pattern = re.compile('类　　型.*?<br/>')
type2_pattern = re.compile('类　　别.*?<br/>')
language_pattern = re.compile('语　　言.*?<br/>')
screan_pattern = re.compile('字　　幕.*?<br/>')
imdb_pattern = re.compile('IMDb评分.*?<br/>')
size_pattern = re.compile('视频尺寸.*?<br/>')
length_pattern = re.compile('片　　长.*?<br/>')
director_pattern = re.compile('导　　演.*?<br/>')
staring_pattern = re.compile('主　　演.*?◎简　　介')
desc_pattern = re.compile('简　　介.*?<br/>')





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

def parse_vdo_html():
    #html = get_url_result("http://www.ygdy8.net/html/gndy/dyzz/20170504/53865.html", 'gbk')
    r = requests.get("http://www.ygdy8.net/html/gndy/dyzz/20170504/53865.html")
    r.encoding = 'gbk'
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    vdo_res_link = soup.find_all(attrs={'bgcolor':"#fdfddf"})
    for td in vdo_res_link:
        print td.a.get('href')




    p = str(soup.find_all('p')[4])



    matcher = re.search(yiming_pattern, p)
    match_str = matcher.group(0)
    vdo_name_yiming = match_str.replace("译　　名　","").replace("<br/>", "").strip()

    matcher = re.search(year_pattern, p)
    match_str = matcher.group(0)
    vdo_year = match_str.replace('年　　代　', '').replace('<br/>', '').strip()

    #地区
    matcher = re.search(area2_pattern, p)
    vdo_area = ''
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_area = match_str.replace('地　　区　', '').replace('<br/>', '').strip()
    else:
        matcher = re.search(area_pattern, p)
        match_str = matcher.group(0)
        vdo_area = match_str.replace('国　　家　', '').replace('<br/>', '').strip()

    #类别
    matcher = re.search(type_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_type = match_str.replace('类　　型　', '').replace('<br/>', '').strip()
    else:
        matcher = re.search(type2_pattern, p)
        match_str = matcher.group(0)
        vdo_type = match_str.replace('类　　别　', '').replace('<br/>', '').strip()

    #语言
    matcher = re.search(language_pattern, p)
    match_str = matcher.group(0)
    vdo_language = match_str.replace('语　　言　', '').replace('<br/>', '').strip()

    #字幕
    matcher = re.search(screan_pattern, p)
    match_str = matcher.group(0)
    vdo_screan = match_str.replace('字　　幕　', '').replace('<br/>', '').strip()

    #imdb评分
    matcher = re.search(imdb_pattern, p)
    match_str = matcher.group(0)
    vdo_imdb = match_str.replace('IMDb评分  ', '').replace('<br/>', '').strip()

    #视频尺寸
    matcher = re.search(size_pattern, p)
    match_str = matcher.group(0)
    vdo_size = match_str.replace('视频尺寸　', '').replace('<br/>', '').strip()

    matcher = re.search(length_pattern, p)
    match_str = matcher.group(0)
    vdo_length = match_str.replace('片　　长　', '').replace('<br/>', '').strip()

    matcher = re.search(director_pattern, p)
    match_str = matcher.group(0)
    vdo_director = match_str.replace('导　　演　', '').replace('<br/>', '').strip()

    matcher = re.search(staring_pattern, p)
    match_str = matcher.group(0)
    vdo_staring = match_str.replace('主　　演　', '').replace('◎简　　介', '').replace('<br/>', '').strip()


    print 'name:' +vdo_name_yiming
    print vdo_year
    print vdo_area
    print vdo_type
    print vdo_language
    print vdo_screan
    print vdo_imdb
    print vdo_size
    print vdo_length
    print vdo_director
    print vdo_staring



if __name__ == '__main__':
    #http://www.ygdy8.net/html/gndy/dyzz/list_23_161.html
    #res = get_url_result("http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html", 'gbk')
    #get_movies_link(res)
    parse_vdo_html()