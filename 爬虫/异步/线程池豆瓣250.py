#!/usr/bin/env python
# coding: utf-8
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time

f = open('电影名.csv','w', encoding='utf-8',newline='')
csvw = csv.writer(f)


def download_douban(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)
    div = html.xpath('//*[@id="content"]/div/div[1]/ol')[0]
    _li = div.xpath('./li')
    for i in _li:
        name = i.xpath('./div/div[2]/div/a/span[1]/text()')
        son = i.xpath('./div/div[2]/div[2]/div/span[4]/text()')
        pingfen = i.xpath('./div/div[2]/div[2]/div/span[2]/text()')
        text = name + pingfen + son
        csvw.writerow(text)
    print(url,'提取完成！')
    time.sleep(5)

if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(0,251,25):
            t.submit(download_douban, f'https://movie.douban.com/top250?start={i}&filter=')