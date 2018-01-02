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



if __name__ == '__main__':
    #read_query_file()
    print len('你好2018'.decode('utf-8'))