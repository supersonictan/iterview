#!/usr/bin/python
#encoding=utf-8
# -*- coding=utf-8-*-



def read_query_file():
    with open("person_name", 'r') as p, open("rel", 'rb') as r, open("result", 'w') as r:
        for person in p:
            for relation in r:
                newLine = person.strip() + relation.strip()
                r.write(newLine)
                r.write('\n')

def evaluate(data, colName):
    if data == "" or data is None:
        return ''

    arr = data.split(' ')
    if colName == "label":
        return arr[0]

    if colName == "qid":
        qid_str = arr[1]
        qid_arr = qid_str.split(':')
        return qid_arr[1]

    if colName == "feature":
        featureArr = arr[2:48]
        feature_newarr = []
        i = 0
        fea_str = ""
        for f in featureArr:
            kv = f.split(':')
            fea_str += str(i)
            fea_str += ":"
            fea_str += kv[1]
            i+=1
            fea_str += " "
        return fea_str


if __name__ == '__main__':
    #read_query_file()
    #print len('你好aa2018'.decode('utf-8'))
    strtmp = "169 qid:13803 1:0.012651 2:0.222222 3:0.250000 4:0.500000 5:0.014843 6:0.000000 7:0.000000 8:0.000000 9:0.000000 10:0.000000 11:0.104874 12:0.236668 13:0.273306 14:0.533099 15:0.111858 16:0.005139 17:0.229167 18:0.446809 19:0.130435 20:0.005578 21:0.183844 22:0.474563 23:0.538482 24:0.383962 25:0.215313 26:0.327105 27:0.242432 28:0.201398 29:0.109582 30:0.181110 31:0.215026 32:0.176352 33:0.557517 34:0.604034 35:0.426925 36:0.556976 37:0.197775 38:0.473637 39:0.550041 40:0.390851 41:0.090909 42:0.117647 43:0.000000 44:0.001657 45:0.008639 46:0.011200 #docid = GX004-61-15522747 inc = -1 prob = 0.0755857"
    print(evaluate(strtmp, "feature"))