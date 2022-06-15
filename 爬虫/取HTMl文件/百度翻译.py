#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

i = input('你需要翻译的单词')

url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': i
}


rec = requests.post(url,data=data)
print(rec.json())