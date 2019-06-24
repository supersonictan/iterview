# -*- coding: utf-8 -*-

import json


if __name__ == '__main__':
    text = """
    [{"index": 0, "word": "刘德华", "label": "PERSON", "start": 0, "finger": 0, "end": 0}, {"index": 0, "word": "无间道", "label": "SHOW", "start": 0, "finger": 0, "end": 0}, {"index": 0, "word": "梁朝伟", "label": "PERSON", "start": 0, "finger": 0, "end": 0}]
    """

    json_obj = json.loads(text)

    result = ''
    for item in json_obj:
        if 'label' not in item:
            continue

        if item['label'] == "PERSON":
            if result != '':
                result += "_"
            result += item['word']

    print(result)