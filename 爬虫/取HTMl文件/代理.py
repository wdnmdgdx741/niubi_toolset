#!/usr/bin/env python
# -*- coding: utf-8 -*-

#通过第三方机器发送请求
import requests

url="https://www.baidu.com/"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

proxies={
    "https":"218.75.158.153:3128"
}

resp = requests.get(url,headers=headers,proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)