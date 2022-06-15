# coding: utf-8
'''
首先要连接上url登陆到网页，然后才可以进行数据的爬取
登陆网站保持会话，访问第一题url
拿到源码得到数据，计算求和
'''
import requests
from bs4 import BeautifulSoup
import re

# 登陆界面
url='http://www.glidedsky.com/login'
# _token=T2yjUNJz3k7zjZEuGs4QAmZnQyKAx89fmN00QNJl&email=xxxxxx&password=xxxxx

# 拿到网页中的token
session = requests.session()
resp = session.get(url)
token = BeautifulSoup(resp.text,"html.parser")
token_text = token.find("input",type="hidden").get("value")

# 登陆网页
data={
    "_token":token_text,
    "email":"xxxxxx",
    "password": "xxxxxxx"
}

# session保持登陆会话
resp1 = session.post(url,data=data)
# 访问第一题的url得到网页源码
first_url="http://www.glidedsky.com/level/web/crawler-basic-1"
resp2 = session.get(first_url)
obj = re.compile(r'<div class="col-md-1">(?P<number>.*?)</div>',re.S)
number = obj.finditer(resp2.text)
end_number = 0
for lien in number:
    lien = lien.group("number").strip()
    end_number += int(lien)
print(end_number)