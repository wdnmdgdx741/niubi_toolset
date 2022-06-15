#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen

url = 'http://www.baidu.com'
res = urlopen(url).read().decode('utf-8')

with open('mybaidu.html', 'w+',encoding='utf-8')as f:
    f.write(res)
print('over!')