#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
北京新发地菜价
'''
import requests

url = "http://www.xinfadi.com.cn/getPriceData.html"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
data={
 "limit": "",
 "current": "",
 "pubDateStartTime": "",
 "pubDateEndTime": "",
 "prodPcatid": "",
 "prodCatid": "",
 "prodName": ""
}

resp = requests.post(url,headers=headers,data=data)
dic = resp.json()
lst = []
f = open('cai.txt','w',encoding="utf-8")

for i in dic:
    for k in range(20):
        resp_name = dic["list"][k]["prodName"]
        resp_low = dic["list"][k]["lowPrice"]
        resp_avg = dic["list"][k]["avgPrice"]
        resp_high = dic["list"][k]["highPrice"]
        f.write(resp_name+",")
        f.write(resp_low+",")
        f.write(resp_avg+",")
        f.write(resp_high+"\n")
f.close()
print("over")

