# coding: utf-8
'''
拿到网页源代码，找到iframe
访问iframe连接，拿到第一层m3u8
访问第一层m3u8拿到第二层m3u8
访问key.key解密
下载视频
合并视频
'''

import requests
import re
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
import asyncio
from Crypto.Cipher import AES

#拿到首页中源代码，中的iframe_urlhttps://player.yunb.tv/dplayer.php?url=https://video.buycar5.cn/20200901/e4NhpyM5/index.m3u8
def get_iframe_src(url):
    # resp = requests.get(url)
    # print(resp.text)
    return "https://player.yunb.tv/dplayer.php?url=https://video.buycar5.cn/20200901/e4NhpyM5/index.m3u8"

#访问第一个m3u8连接，拿到第视频所在连接https://video.buycar5.cn/20200901/e4NhpyM5/index.m3u8
def get_first_m3u8_url(url):
    resp = requests.get(url)
    obj = re.compile(r"var playUrl = '(?P<first>.*?)';",re.S)
    first_url = obj.search(resp.text).group("first")
    return first_url

#访问第一个个m3u8连接，保存内容https://video.buycar5.cn/20200901/e4NhpyM5/1000kb/hls/index.m3u8
def download_m3u8(url,name):
    resp = requests.get(url)
    with open(name,'wb') as f:
        f.write(resp.content)


async def aio_download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(name,'wb') as f:
            await f.write(await resp.content.read())
    print(f"{name}下载完毕")

async def aio_download(up_url):#https://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/
    tasks=[]
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("two_m3u8.txt",'r',encoding="utf-8") as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line = line.strip()
                #https://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/ZlPMyMi0.ts
                #https://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/key.key
                #拼接真的tw_url
                name = line.rsplit("hls/")[1]
                task = asyncio.create_task(aio_download_ts(line, name, session))#创建任务
                tasks.append(task)

            await asyncio.wait(tasks)#等待任务结束

def get_key(url):
    resp = requests.get(url)
    resp.encoding="utf-8"
    return resp.text

async def aes_decode_ts(name, key):
    aes=AES.new(key=key.encode("utf-8"),IV=b"0000000000000000",mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/{name}",'rb') as f1,\
        aiofiles.open(f"video/temp_{name}",'wb')as f2:

        bs = await f1.read()#读取f1中的所有内容
        await f2.write(aes.decrypt(bs))#把解密好的内容写入文件
    print(f"{name}处理完毕！！")

async def aes_decode(key):
    tasks = []
    #解密
    async with aiofiles.open("video/two_m3u8.txt",'r',encoding='utf-8') as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            line = line.rsplit("hls/")[1]
            #开始创建异步任务
            task = asyncio.create_task(aes_decode_ts(line, key))
            tasks.append(task)
        await asyncio.wait(tasks)

def merge_ts():
    #首先在two中拿到文件名
    pass



def main(url):
    # 拿到网页源代码，找到iframe,里面的url
    iframe_src = get_iframe_src(url)
    # 拿到一层m3u8的下载地址
    first_m3u8_url = get_first_m3u8_url(iframe_src)
    #拿到下载的m3u8，下载第一层m3u8文件
    download_m3u8(first_m3u8_url,"video/first_m3u8.txt")
    print('第一层下载完成')
    #下载第二层m3u8文件
    with open('video/first_m3u8.txt','r',encoding="utf-8") as f:
        for i in f:
            if i.startswith('#'):   #判断是否是#开头
                continue
            else:
                i = i.strip()#去掉换行符空格等  /20200901/e4NhpyM5/1000kb/hls/index.m3u8
                #拼接2层下载路径

                #第三层https://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/ZlPMyMi0.ts
                #key.keyhttps://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/key.key
                two_m3u8_url = first_m3u8_url.rsplit("20200901")[0]+i
                download_m3u8(two_m3u8_url,'video/two_m3u8.txt')
                print('第二层下载完成')
    #下载视频
    download_url = 'https://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/'
    #异步协程
    asyncio.run(aio_download(download_url))
    #key的url
    key_url = download_url + 'key.key'
    key = get_key(key_url)
    #解密
    asyncio.run(aes_decode(key))
    #合并视频
    merge_ts()


if __name__ == '__main__':
    url = "https://www.yunbtv.com/vodplay/yueyudiyiji-1-1.html"
    main(url)
