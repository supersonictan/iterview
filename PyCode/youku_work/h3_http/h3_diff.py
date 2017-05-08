#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getUrlResult(url):
    session = requests.session()
    res = session.get(url)
    print res
    return res


if __name__ == '__main__':
    url = "http://10.103.143.118:20428/config%3dcluster%3aecb_main_1%2cno_summary%3ayes%2cstart%3a0%2chit%3a30%2crank_size%3a50000%2crerank_size%3a2000%2cresult_compress%3az_speed_compress%2crank_trace%3aTRACE3%2ctrace%3aTRACE3%2ctimeout%3a20000%2cformat%3aprotobuf%2cproto_format_option%3apb_matchdoc_format%26%26query%3d((show_name%3a%27%e6%80%9d%e7%be%8e%e4%ba%ba%27+AND+type%3a%271%27)+OR+(show_alias%3a%27%e6%80%9d%e7%be%8e%e4%ba%ba%27+AND+type%3a%271%27)+OR+(show_keyword%3a%27%e6%80%9d%e7%be%8e%e4%ba%ba%27+AND+type%3a%271%27)+OR+(show_sub_title%3a%27%e6%80%9d%e7%be%8e%e4%ba%ba%27+AND+type%3a%271%27)+OR+(show_name%3a%27%e6%80%9d%e7%be%8e%e4%ba%ba%27+AND+type%3a%271%27))%26%26filter%3dcontain(show_site%2c%220%7c2%7c1%7c3%7c4%22)%26%26attribute%3did%26%26kvpairs%3d_ps%3avideo_quality111%2cadvsort%3aadvtaobao%2cextention%3a2007024052%2313%23%e6%80%9d%e7%be%8e%e4%ba%ba%3b2007024052%232%23%e6%80%9d%e7%be%8e%e4%ba%ba%2cextention_rel%3a%3b1%23316709%2311.103737%2cextention_tag%3a%3b%2cextention_term%3a%e6%80%9d%e7%be%8e%e4%ba%ba%232007024052%233%230%230%3b%e6%80%9d%e7%be%8e%e4%ba%ba%232007024052%233%230%230%2cindex_term%3a%e6%80%9d%e7%be%8e%e4%ba%ba%232007024052%233%230%230%2ckey%3a2007024052%230%23%e6%80%9d%e7%be%8e%e4%ba%ba%2coriginal_query%3a1%2cq%3ashow_info%5c%5c%3a%5c%5c%3a%e6%80%9d%e7%be%8e%e4%ba%ba+OR+show_name%5c%5c%3a%5c%5c%3a%e6%80%9d%e7%be%8e%e4%ba%ba%2cquery_category%3a97%236177%4086%232524%4095%23603%2crank_size%3a50000%2crerank_size%3a2000%2crewq%3a(show_name%5c%5c%3a%5c%5c%3a%e6%80%9d%e7%be%8e%e4%ba%ba+type%5c%5c%3a%5c%5c%3a1)+OR+(show_alias%5c%5c%3a%5c%5c%3a%e6%80%9d%e7%be%8e%e4%ba%ba+type%5c%5c%3a%5c%5c%3a1)+OR+(show_keyword%5c%5c%3a%5c%5c%3a%e6%80%9d%e7%be%8e%e4%ba%ba+type%5c%5c%3a%5c%5c%3a1)+OR+(show_sub_title%5c%5c%3a%5c%5c%3a%e6%80%9d%e7%be%8e%e4%ba%ba+type%5c%5c%3a%5c%5c%3a1)++OR++(show_name%5c%5c%3a%5c%5c%3a%e6%80%9d%e7%be%8e%e4%ba%ba+type%5c%5c%3a%5c%5c%3a1)+%2csort_flag%3a40%2cstats%3aecb_relevance111%2cusesearchercache%3ayes%2cwide_query%3a0%40%40%40%40%40%26%26sort%3d-RANK%26%26rank%3drank_profile%3aDefaultProfile%26%26virtual_attribute%3dPS%3avideo_quality%26%26final_sort%3dsort_name%3aAdapterSorter"
    getUrlResult(url)