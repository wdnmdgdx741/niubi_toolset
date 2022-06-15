#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re

url = 'https://movie.douban.com/chart'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

res = requests.get(url, headers=header)
res_text = res.text

re.compile(r'')

