#!/usr/bin/python
# -*- encoding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


data = """
{"/people/person/highest_education": [], "/people/person/industry_involved": [], "/people/person/sibling_s": [], "/type/object/name": "小泽·玛利亚", "/common/entity/_hot": 1584, "/people/person/place_of_birth": [{"guid": "fecc3c6c-44ce-11e5-8e72-f80f41fb03aa", "name": "日本", "id": "/authority/sm_baike/e1ff79006639f990c9b62b3a863b136a"}], "/people/person/imdb": ["nm3076831"], "/people/person/nationality": [{"guid": "fecc3c6c-44ce-11e5-8e72-f80f41fb03aa", "name": "日本", "id": "/authority/sm_baike/e1ff79006639f990c9b62b3a863b136a"}], "/type/object/description": "小泽玛利亚（日语：小泽マリア、おざわ まりあ，英语：Ozawa Maria），1986年1月8日出生于日本北海道 ，混血儿 （父亲是>法裔加拿大人，母亲是日本人 ），日本AV女优 。 她一开始为网站shirouto-teien做模特 ，并在此期间拍摄了", "/people/person/date_of_birth": ["1986-01-08"], "/people/person/profession": [{"guid": "aa1e91a8-b5f1-11e5-b2b7-d43d7e6fab60", "name": "演员"}, {"guid": "19d2c294-b386-11e5-888a-d43d7e6fab60", "name": "AV女优"}, {"guid": "1a847bba-47e8-11e5-9bc2-f80f41fb03aa", "name": "模特"}, {"guid": "14447cbe-47e8-11e5-9bc2-f80f41fb03aa", "name": "编剧"}], "/people/person/gender": [{"guid": "3ef85580-f4c2-11e4-8183-f80f41f8d6e5", "name": "女", "id": "/authority/gender/female"}], "/people/person/spouse_s": [], "/people/person/parents": [], "/people/person/talent_agency": [], "/people/person/zodiac_sign": [{"guid": "83a80276-4660-11e5-bbc0-f80f41fb03aa", "name": "摩羯座", "id": "/authority/sm_baike/e1e8c5ec8ee22508368a627e83c895e5"}], "guid": "ba8e2834-4d30-11e5-af4b-f80f41fb03aa", "/people/person/ethnicity": [], "/people/person/languages": [], "/people/person/weight_kg": [], "/people/person/native_place": []}
"""
if __name__ == '__main__':
    i = 0

    with open('/Users/tanzhen/Desktop/parse.txt', 'w') as w, open('/Users/tanzhen/Desktop/part-00000', 'r') as f:
        for line in f:
            obj = json.loads(line)
            res = ""
            # 姓名
            name = str(obj['/type/object/name'])
            name.replace("·", "")
            res += name

            # guid
            guid = obj['guid']
            res += ";"
            res += guid

            # 国籍
            countryList = []
            country = obj['/people/person/nationality']
            for c in country:
                countryList.append(c['name'])
            res += ";"
            res += ','.join(countryList)

            # 生日
            birthdayObj = obj['/people/person/date_of_birth']
            if len(birthdayObj) > 0:
                birthday = birthdayObj[0]
            res += ";"
            res += birthday

            # 性别
            gender = ''
            genderList = obj['/people/person/gender']
            if len(genderList) > 0:
                gender = genderList[0]['name']
            if gender.encode("utf-8") == '女':
                gender = 'F'
            else:
                gender = 'M'

            res += ";"
            res += gender

            res += "\n"

            w.write(str(res))
