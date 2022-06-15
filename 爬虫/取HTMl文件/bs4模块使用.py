#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
访问唯美图片主站点，源代码
找到子连接
获得子连接的源代码
保存图片
'''

from bs4 import BeautifulSoup
import requests
import time
import os

os.mkdir('image')
for y in range(3,30):
    url = "https://www.umei.cc/bizhitupian/weimeibizhi/index_" + str(y) + ".htm"

    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    resp = requests.get(url,headers=headers)
    resp.encoding='utf-8'
    man_page = BeautifulSoup(resp.text,"html.parser")
    lst = man_page.find("div",class_="TypeList").find_all('a')


    for i in lst:
        href = "https://www.umei.cc" + i.get('href')
        resp1 = requests.get(href,headers=headers)
        resp1.encoding="utf-8"
        bp = BeautifulSoup(resp1.text,'html.parser')
        lst = bp.find('div',class_="ImageBody").find_all('img')
        for k in lst:
            image = k.get('src')
            image_name = image.split("/")[-1] + ".jpg"
            resp2 = requests.get(image,heads)
            with open("D:/桌面/python/爬虫/image/" + image_name,'wb')as f:
                f.write(resp2.content)
            print('over!!')
            time.sleep(5)
    print('第{0}页完成'.format(y))
print('all_over!!!!')

