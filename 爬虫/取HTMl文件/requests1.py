#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re

url='https://movie.douban.com/top250'
dic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}



rec = requests.get(url,headers=dic)
rec_text = rec.text

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>',re.S)

result = obj.finditer(rec_text)
for i in result:
    print(i.group('name'))
    print(i.group('year').strip())
    print(i.group('score'))