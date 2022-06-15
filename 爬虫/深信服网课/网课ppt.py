#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
for i in range(1,32):
    url='https://cnstatic01.e.vhall.com/document/84a088d056b41a94be469bd96065e961/'+str(i)+'.jpg'
    resp = requests.get(url,headers=headers)
    with open("video/"+str(i)+".jpg","wb") as f:
        f.write(resp.content)
    print(f"{i}完成")
