# coding: utf-8
'''
流程
首先访问网站，在源码中拿到m3u8连接，
访问m3u8
下载视频，整合视频
https://91kanju.com/vod-detail/54812.html
'''
import requests
import re


url = "https://91kanju.com/vod-play/54812-1-1.html"

obj = re.compile(r"url: '(?P<url>.*?)',",re.S)

resp = requests.get(url)
m3u8_url = obj.search(resp.text).group("url")
print(m3u8_url)
resp.close()

resp1 = requests.get(m3u8_url)

with open('哲仁王后.u3u8','wb')as f:
    f.write(resp1.content)
print('over!!!')










