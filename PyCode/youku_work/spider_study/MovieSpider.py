#!/usr/bin/python
#encoding=utf-8
# -*- coding=utf-8-*-
from bs4 import BeautifulSoup
import lxml
import uniout
from requests.adapters import HTTPAdapter
import requests
import re
import MySQLdb
import sys
import time
import chardet
reload(sys)
sys.setdefaultencoding('utf-8')

# yiming_pattern = re.compile('译　　名.*?<br/>')
# year_pattern = re.compile('年　　代.*?<br/>')
# area_pattern = re.compile('国　　家.*?<br/>')
# area2_pattern = re.compile('地　　区.*?<br/>')
# type_pattern = re.compile('类　　型.*?<br/>')
# type2_pattern = re.compile('类　　别.*?<br/>')
# language_pattern = re.compile('语　　言.*?<br/>')
# screan_pattern = re.compile('字　　幕.*?<br/>')
# imdb_pattern = re.compile('IMDb评分.*?<br/>')
# size_pattern = re.compile('视频尺寸.*?<br/>')
# length_pattern = re.compile('片　　长.*?<br/>')
# director_pattern = re.compile('导　　演.*?<br/>')
# staring_pattern = re.compile('主　　演.*?◎简　　介')
# desc_pattern = re.compile('简　　介.*?<br/>')
yiming_pattern = re.compile('译　　名.*?<br *?/>')
year_pattern = re.compile('年.*?代.*?<br.*?/>')
area_pattern = re.compile('国　　家.*?<br *?/>')
area2_pattern = re.compile('地　　区.*?<br *?/>')
type_pattern = re.compile('类　　型.*?<br *?/>')
type2_pattern = re.compile('类　　别.*?<br *?/>')
language_pattern = re.compile('语　　言.*?<br *?/>')
screan_pattern = re.compile('字　　幕.*?<br *?/>')
imdb_pattern = re.compile('IMDb评分.*?<br *?/>')
size_pattern = re.compile('视频尺寸.*?<br *?/>')
length_pattern = re.compile('片　　长.*?<br *?/>')
director_pattern = re.compile('导　　演.*?<br *?/>')
staring_pattern = re.compile('主　　演.*?◎简　　介')
desc_pattern = re.compile('简　　介.*?<br *?/>')
vdoCoreName_pattern = re.compile('《.+?》')

conn= MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db ='great_china',charset='utf8')
cur = conn.cursor()

vdo_name = []
vdo_core_name = []
vdo_page_link = []
global pic_url
pic_url = ''
#!Q(gidUF,4pI
#解析url到文本
def get_url_result(list_url, encoding):
    r = requests.get(list_url)
    r.encoding = encoding
    return r.text

#将列表页的name和link保存到vdo_name-vdo_page_link
def get_movies_link(html):
    soup = BeautifulSoup(html, 'lxml')
    list = soup.find_all(attrs={'class':"ulink"})

    for a_tag in list:
        name_str = str(a_tag.string).decode('string_escape')
        vdo_name.append(name_str)

        #core_name
        matcher = re.search(vdoCoreName_pattern, name_str)
        if matcher is not None:
            match_str = matcher.group(0)
            v_core_name = match_str.replace('《', '').replace('》', '').strip()
            vdo_core_name.append(v_core_name)
        else:
            vdo_core_name.append(name_str)

        v_link = 'http://www.ygdy8.net' + a_tag.get('href')
        vdo_page_link.append(v_link)

        #print a_tag.string + "\thttp://www.ygdy8.net" + a_tag.get('href')

def downloadImageFile(picName, picUrl):
    session = requests.session()
    session.mount('http://', HTTPAdapter(max_retries=3))
    r = session.get(picUrl, stream=True)  # here we need to set stream = True parameter

    with open("F:\\pics\\"+ picName + ".jpg",'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    print 'Finished down pic'

def parse_vdo_html(detailUrl, vdo_name, vdo_core_name):
    #html = get_url_result("http://www.ygdy8.net/html/gndy/dyzz/20170504/53865.html", 'gbk')
    session = requests.session()
    #request_retry = requests.adapters.HTTPAdapaters(max_retries=3)
    session.mount('http://', HTTPAdapter(max_retries=3))
    r = session.get(detailUrl)

    #r = requests.get(detailUrl)
    if r.status_code != 200:
        print str(r.status_code) + ''
        return
    r.encoding = 'gbk'
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    vdo_res_link = soup.find_all(attrs={'bgcolor':"#fdfddf"})
    vdo_url = ''
    for td in vdo_res_link:
        if vdo_url != '':
            vdo_url += ';'
        vdo_url += td.a.get('href')
    if vdo_url == '':
        print 'No vdo_url:' + vdo_core_name + '\t'  + detailUrl





    #p = str(soup.find_all('p')[4])
    p = str(soup)


    #解析图片地址
    pic_urls = re.findall('http:.*?jpg', p)
    if pic_urls:
        pic_url = pic_urls[0]

    #译名
    vdo_name_yiming = vdo_name
    # vdo_name_yiming = ''
    # matcher = re.search(yiming_pattern, p)
    # if matcher is not None:
    #     match_str = matcher.group(0)
    #     vdo_name_yiming = match_str.replace("译　　名　","").replace("<br/>", "").strip()
    # else:
    #     print 'No YiMing:' + detailUrl

    #年代
    vdo_year  =''
    matcher = re.search(year_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_year = match_str.replace('年　　代　', '').replace('<br/>', '').strip()
    else:
        print 'No 年代:' + vdo_core_name + '\t' + detailUrl

    #地区
    matcher = re.search(area2_pattern, p)
    vdo_area = ''
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_area = match_str.replace('地　　区　', '').replace('<br/>', '').strip()
    else:
        matcher = re.search(area_pattern, p)
        if matcher is not None:
            match_str = matcher.group(0)
            vdo_area = match_str.replace('国　　家　', '').replace('<br/>', '').strip()
        else:
            print 'No 国家:' + vdo_core_name + '\t'  + detailUrl

    #类别
    vdo_type = ''
    matcher = re.search(type_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_type = match_str.replace('类　　型　', '').replace('<br/>', '').strip()
    else:
        matcher = re.search(type2_pattern, p)
        if matcher is not None:
            match_str = matcher.group(0)
            vdo_type = match_str.replace('类　　别　', '').replace('<br/>', '').strip()
        else:
            print 'No 类型:' + vdo_core_name + '\t'  + detailUrl

    #语言
    vdo_language = ''
    matcher = re.search(language_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_language = match_str.replace('语　　言　', '').replace('<br/>', '').strip()
    else:
        print 'No 语言:' + vdo_core_name + '\t'  + detailUrl

    #字幕
    vdo_screan = ''
    matcher = re.search(screan_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_screan = match_str.replace('字　　幕　', '').replace('<br/>', '').strip()
    else:
        print 'No 字幕:' + vdo_core_name + '\t'  + detailUrl

    #imdb评分
    vdo_imdb = ''
    matcher = re.search(imdb_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_imdb = match_str.replace('IMDb评分  ', '').replace('<br/>', '').strip()
    else:
        print 'No IMDb:' + vdo_core_name + '\t'  + detailUrl

    #视频尺寸
    vdo_size = ''
    matcher = re.search(size_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_size = match_str.replace('视频尺寸　', '').replace('<br/>', '').strip()
    else:
        print 'No 视频尺寸:' + vdo_core_name + '\t'  + detailUrl

    #片长
    vdo_length = ''
    matcher = re.search(length_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_length = str(match_str.replace('片　　长　', '').replace('<br/>', '').strip())
    else:
        print 'No 片长:' + vdo_core_name + '\t' +detailUrl

    #导演
    vdo_director = ''
    matcher = re.search(director_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_director = match_str.replace('导　　演　', '').replace('<br/>', '').strip()
        #vdo_director = match_str.replace('导.*演　', '').replace('<br/>', '').strip()
    else:
        print 'No 导演:' + vdo_core_name + '\t'  + detailUrl

    #主演
    vdo_stars = ''
    matcher = re.search(staring_pattern, p)
    if matcher is not None:
        match_str = matcher.group(0)
        vdo_staring = match_str.replace('主　　演　', '').replace('◎简　　介', '').replace('\'', '').strip('<br/>')
        vdo_stars = ''
        for item in vdo_staring.split('<br/>'):
            if vdo_stars != '':
                vdo_stars += ';'
            vdo_stars += item.strip('　')

    # print 'name:' +vdo_name_yiming
    # print vdo_year
    # print vdo_area
    # print vdo_type
    # print vdo_language
    # print vdo_screan
    # print vdo_imdb
    # print vdo_size
    # print vdo_length
    # print vdo_director
    # print vdo_stars
    # print vdo_url
    #sql = """INSERT INTO `vedio` VALUES (1000, '极限特工3', '极限特工3', '美国', '动作/冒险', '英语', '中英双字幕', '5.4/10 from 31,888 users', '1280 x 720', '107分钟', 'D·J·卡卢索 D.J. Caruso', '范·迪塞尔 Vin Diesel;甄子丹 Donnie Yen;迪皮卡·帕度柯妮 Deepika Padukone;吴亦凡 Kris Wu;鲁比·罗丝 Ruby Rose;塞缪尔·杰克逊 Samuel L. Jackson;妮娜·杜波夫 Nina Dobrev;托尼·贾 Tony Jaa;托妮·科莱特 Toni Collette;赫敏·科菲尔德 Hermione Corfield;阿尔·萨皮恩扎 Al Sapienza;艾斯·库珀 Ice Cube;内马尔 Neymar;罗伊·麦克凯恩 Rory McCann;迈克尔·比斯平 Michael Bisping', null, 'ftp://ygdy8:ygdy8@yg32.dydytt.net:7013/[阳光电影www.ygdy8.com].极限特工3：终极回归.BD.720p.中英双字幕.mkv', null);"""
    #sql = "insert into vedio values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #cur.execute(sql, (1000, vdo_name_yiming, vdo_name_yiming, vdo_area, vdo_type, vdo_language, vdo_screan, vdo_imdb, vdo_size, vdo_length,vdo_director,vdo_stars,'',vdo_url,''))
    picName = insert_mysql(vdo_name_yiming, vdo_core_name, vdo_area, vdo_type, vdo_language, vdo_screan, vdo_imdb, vdo_size, vdo_length,vdo_director,vdo_stars,vdo_url, detailUrl)
    print 'before down'
    downloadImageFile(str(picName),pic_url)
    pic_url = ''

def insert_mysql(vdo_name_yiming, vdo_core_name, vdo_area, vdo_type, vdo_language, vdo_screan, vdo_imdb, vdo_size, vdo_length,vdo_director,vdo_stars,vdo_url, detailUrl):
    vdo_length = vdo_length.decode('utf-8')
    if cur is None:
        print 'MySQL connect exception!'
    try:
        sql = "insert into vedio (" \
              "v_name," \
              "v_name_ch," \
              "v_country," \
              "v_type," \
              "v_language," \
              "v_screan," \
              "v_imdb," \
              "v_size," \
              "v_time_length," \
              "v_director," \
              "v_star," \
              "v_desc," \
              "v_url," \
              "v_pic" \
              ")" \
            " values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"% \
              (vdo_name_yiming, vdo_core_name, vdo_area, vdo_type, vdo_language, vdo_screan, vdo_imdb, vdo_size,
               vdo_length, vdo_director, vdo_stars, 'desc', vdo_url, 'pic')

        #cur.execute("SET NAMES utf8")
        rs = cur.execute(sql)
        conn.commit()
        id = cur.lastrowid
        return id
    except Exception, e:
        print str(e) + detailUrl
        conn.rollback()
        return -1
    # finally:
    #     conn.close()


if __name__ == '__main__':
    #parse_vdo_html('http://www.ygdy8.net/html/gndy/dyzz/20161208/52675.html', 'test','test')
    for i in range(1,162): #页码
        list_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_' + str(i) + '.html'
        list_res = get_url_result(list_url, 'gbk')
        vdo_name = []
        vdo_core_name = []
        vdo_page_link = []
        get_movies_link(list_res)
        for j in range(0, len(vdo_name)):
            parse_vdo_html(vdo_page_link[j], vdo_name[j], vdo_core_name[j])
            time.sleep(1)
        print 'Finished Page:' + str(i)

#http://www.cnblogs.com/kaituorensheng/archive/2013/01/05/2846627.html