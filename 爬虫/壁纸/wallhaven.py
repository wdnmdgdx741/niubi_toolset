# coding: utf-8
import requests
from bs4 import BeautifulSoup

# 排行榜图片
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

for y in range(12, 15):
    url = 'https://wallhaven.cc/toplist?page={}'.format(y)
    print(url)
    resp = requests.get(url, headers=headers)
    main_page = BeautifulSoup(resp.text, "html.parser")
    alist = main_page.find("section", class_="thumb-listing-page").find_all('a', class_="preview")
    for i in alist:
        son_url = i.get('href')
        resp1 = requests.get(son_url, headers=headers)
        son_page = BeautifulSoup(resp1.text, "html.parser")
        lst = son_page.find("section", id="showcase").find_all("img", id="wallpaper")
        for src in lst:
            src_donload = src.get("src")
            filename = src_donload.split("/")[-1]
            resp2 = requests.get(src_donload, headers=headers)
            with open('image/' + filename, 'wb') as f:
                f.write(resp2.content)
            print(filename, '完成！！！')
