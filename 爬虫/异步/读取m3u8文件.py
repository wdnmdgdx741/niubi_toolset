# coding: utf-8

import os
import requests
import time


n = 1
with open('哲仁王后.m3u8','r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()  # 处理字符串，去掉指定序列
        if line.startswith("#"):  # 寻找开头是#的字符串
            continue

        resp = requests.get(line)
        if not os.path.exists("video"):
            os.mkdir("video")
        f = open(f'video/{n}.ts', 'wb')
        f.write(resp.content)
        resp.close()
        time.sleep(1)
        print("完成{0}".format(n))
        n += 1
        with open("video/file.txt",'a+',encoding="utf-8") as t:
            t.write(f"file  \"home/linux/video/{str(n)}.txt"+"\""+'\n')
            print("ok")
    print("over!!!")
