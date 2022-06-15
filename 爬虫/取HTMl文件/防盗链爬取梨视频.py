#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
抓取网页数据得到systemTime: "1629538502179"，替换到连接中
视频连接：https://video.pearvideo.com/mp4/adshort/20210819/cont-1739428-15750401_adpkg-ad_hd.mp4
请求连接：https://video.pearvideo.com/mp4/adshort/20210819/1629538502179-15750401_adpkg-ad_hd.mp4

首先请求网页拿到源码
得到源码中的视频连接和time
替换url链接得到真实url
下载视频
'''

import requests


true_url = "https://video.pearvideo.com/mp4/adshort/20210819/cont-1739428"
contId = true_url.split("-")[-1]

url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.09186200927899968"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    #防盗链，告诉服务器是从哪里跳转来的
    "Referer": "https://www.pearvideo.com/video_1739428"
}
resp = requests.get(url,headers=headers)
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
print(srcUrl)
# https://video.pearvideo.com/mp4/adshort/20210819/1629538502179-15750401_adpkg-ad_hd.mp4
systemtime = dic["systemTime"]
#1629538502179
srcUrl = srcUrl.replace(systemtime,"cont-{0}".format(contId))
#srcUrl中的systemtime值替换掉
with open('1.mp4','wb')as f:
    f.write(requests.get(srcUrl,headers=headers).content)




