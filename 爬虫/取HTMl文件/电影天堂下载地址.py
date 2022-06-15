#!/usr/bin/env python
# -*- coding: utf-8 -*-
#定位子链接块源代码提取出来
#提起子链接
#访问子链接拿到里面需要的下载连接

import requests
import re
import csv


filename = '电影download.csv'
doman='https://www.dy2018.com/'

heads={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
obj = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj1 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj2 = re.compile(r'◎译　　名　(?P<name>.*?)<br />.*?<a href="(?P<download>.*?)">',re.S)

resp = requests.get(doman,heads)
resp.encoding='gb2312'
resp_text = resp.text
result1 = obj.finditer(resp_text)

f = open(filename,'w+',encoding='utf-8')
csv_text = csv.writer(f)

lst = []

for i in result1:
    ul = i.group('ul')

    result2 = obj1.finditer(ul)
    for z in result2:
        child_href = doman + z.group("href").strip("/")
        lst.append(child_href)
    for href in lst:
        resp1 = requests.get(href,heads)
        resp1.encoding='gb2312'
        resp1_text = resp1.text
        result3 = obj2.finditer(resp1_text)
        for dwn in result3:
            dic=dwn.groupdict()
            print(dic)
            csv_text.writerow(dic.values())
f.close()
print('ok')

