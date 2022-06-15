import requests
from bs4 import BeautifulSoup
import re
import base64
from fontTools.ttLib import TTFont

# 登陆界面
url='http://www.glidedsky.com/login'
# _token=T2yjUNJz3k7zjZEuGs4QAmZnQyKAx89fmN00QNJl&email=xxxxxx&password=xxxxxx

# 拿到网页中的token
session = requests.session()
resp = session.get(url)
token = BeautifulSoup(resp.text,"html.parser")
token_text = token.find("input",type="hidden").get("value")

# 登陆网页
data={
    "_token":token_text,
    "email":"xxxxxx",
    "password": "xxxxxx"
}

# session保持登陆会话
resp1 = session.post(url,data=data)
# 访问第一题的url得到网页源码
first_url="http://www.glidedsky.com/level/web/crawler-font-puzzle-1?page=1"
resp2 = session.get(first_url)
obj = re.compile(r'src: url\(data:font;charset=utf-8;base64,(?P<base64>.*?)\) format',re.S)
base64_text = obj.search(resp2.text).group("base64")
zt = base64.b64decode(base64_text)
with open("glide_font.ttf","wb")as f:
    f.write(zt)
from fontTools.ttLib import TTFont
font = TTFont('glide_font.ttf')
font.saveXML('glide_font.xml')