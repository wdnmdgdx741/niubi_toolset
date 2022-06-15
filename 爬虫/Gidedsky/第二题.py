# coding: utf-8
import re
import requests
from bs4 import BeautifulSoup
from lxml import etree




# 登陆网页,token
def _token(url):
    resp_login = session.get(url_login)
    html = BeautifulSoup(resp_login.text,"html.parser")
    return html.find("input",type="hidden").get("value")

# 登陆网站
def login(url,token):
    data={
        "_token": token,
        "email": "xxxxxx",
        "password": "xxxxx"
    }
    resp = session.post(url,data=data)
    print(resp.url)
    print(resp.request,'登陆成功')

def cocned_url(url):
    numbers = 0
    for k in range(1,1001):
        parser = {
            "page" : k
        }
        resp1 = session.get(url,params=parser)
        print(resp1.url)
        obj = re.compile(r'<div class="col-md-1">(?P<number>.*?)</div>', re.S)
        lst = obj.finditer(resp1.text)
        for number in lst:
            number = number.group('number').strip()
            numbers += int(number)
    print(numbers)



def main(url):
    token = _token(url)

    login(url,token)
    second_url = "http://www.glidedsky.com/level/web/crawler-basic-2"
    cocned_url(second_url)


if __name__ == '__main__':
    session = requests.session()
    url_login = 'http://www.glidedsky.com/login'
    main(url_login)