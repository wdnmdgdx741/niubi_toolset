# coding: utf-8
'''
1、首先访问网页面代码，拿到iframe,中的m3u8_url连接
2、访问m3u8连接拿到源码中的第一层m3u8连接，保存文件
3、访问第一层m3u8文件中的连接，得到第二层m3u8文件
4、访问最后一层m3u8文件，拿到最终的m3u8.ts连接
5、下载视频
6、解密视频
7、合并视频
'''
import requests
from bs4 import BeautifulSoup
import re
import aiohttp
import asyncio
import aiofiles
import time
from Crypto.Cipher import AES
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 访问视频目录链接拿到，第single(单)视频连接
def get_iframe(url):
    # resp = requests.get(url,headers=headers)
    # bs = BeautifulSoup(resp_text)
    # bs("iframe")
    return "https://player.yunb.tv/dplayer.php?url=https://video.buycar5.cn/20200901/e4NhpyM5/index.m3u8"


def get_video_m3u8(url):
    resp = requests.get(url,headers=headers)
    obj = re.compile(r"var playUrl = '(?P<first_m3u8_url>.*?)';", re.S)
    first_m3u8_url = obj.search(resp.text).group("first_m3u8_url")
    # return first_m3u8_url # https://video.buycar5.cn/20200901/e4NhpyM5/index.m3u8
    return "https://video.buycar5.cn/20200901/e4NhpyM5/index.m3u8"  # 测试


def donwload_save(url, filename):
    resp = requests.get(url,headers=headers)
    with open(filename, 'wb') as f:
        f.write(resp.content)

async def download_ts(url,filename,session):
    async with session.get(url,headers=headers) as resp:
        async with aiofiles.open(f"video/{filename}",'wb') as f:
            await f.write(await resp.content.read())
        time.sleep(0.5)
    print(f"{filename}下载完成")


async def downlaod_open():
    tasks=[]
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("video/two_m3u8_url.txt", 'r', encoding="utf-8") as f:
            async for itme in f:
                if itme.startswith("#"):
                    continue
                itme = itme.strip()
                filename = itme.rsplit("hls/")[1]
                # 创建任务，给task,然后run列表await asyncio.wait(tasks)
                task = asyncio.create_task(download_ts(itme,filename,session))
                tasks.append(task)

        await asyncio.wait(tasks)

def get_key_url(url):
    resp = requests.get(url,headers=headers)
    resp.encoding = "utf-8"
    return resp.text


async def aes_decode(key):
    tasks=[]
    async with aiofiles.open("video/two_m3u8_url.txt","r",encoding='utf-8') as f:
        async for i in f:
            if i.startswith("#"):
                continue
            i = i.strip()
            i = i.rsplit("hls/")[1]
            task = asyncio.create_task(aes_decode_ts(i,key))
            tasks.append(task)

    await asyncio.run(tasks)

async def aes_decode_ts(i,key):
    aes = AES.new(key=key.encode("utf-8"),IV=b"0000000000000000",mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/{i}","rb") as f1,\
        aiofiles.open(f"video/temp_{i}", "wb")as f2:

        bs = await f1.read()
        await f2.write(aes.decrypt(bs))# 把解密好的内容写入文件
    print(f"{i}处理完毕！！")

def hebinvideo():
    # lst=[]
    # with open("video/two_m3u8_url.txt",'r',encoding="utf-8") as f:
    #     for i in f:
    #         if i.startswith("#"):
    #             continue
    #         i = i.strip()
    #         i = i.split("hls/")[1]
    #         lst.append(f"video/temp_{i}")
    #
    # s = "+".join(lst)
    # print(s)

    os.system("copy /b video/temp_*.ts 1.mp4")
    print("ok")


def main(url):
    # 1、请求源码拿到iframe中的单独视频连接
    # single_get = https://www.yunbtv.com/vodplay/yueyudiyiji-1-1.html
    single_get = get_iframe(url)
    # 2、请求放回的url,拿到第一层m3u8连接
    # first_m3u8_url = https://video.buycar5.cn/20200901/e4NhpyM5/index.m3u8
    # first_m3u8_url = get_video_m3u8(single_get)
    # 3、请求第一个m3u8连接，保存文件
    # donwload_save(first_m3u8_url, "video/first_m3u8_url.txt")
    print("第一层m3u8下载完成")
    # 3.1、打开第一个文件，拿到里面的url
    with open("video/first_m3u8_url.txt", 'r', encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):  # 判断字符串以#开头
                continue
            line.strip()  # 去掉特殊字符（空格、换行……）
            # line = /20200901/e4NhpyM5/1000kb/hls/index.m3u8
            # 拼接url,first_m3u8_url+line
            # two_m3u8_url = first_m3u8_url.rsplit("/20200901")[0] + line
            # 重复调用download_save函数下载文件
            # donwload_save(two_m3u8_url, "video/two_m3u8_url.txt")
            print("第二层m3u8下载完成")

    # 5、下载视频
    # 多任务异步携程
    # asyncio.run(downlaod_open())
    # 6、解密视频文件
    # 首先我们要拿到key
    # key_url = "https://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/key.key"
    # key = get_key_url(key_url)
    # 写aes解密体
    # asyncio.run(aes_decode(key))
    # 合并视频
    hebinvideo()


if __name__ == '__main__':
    url = "https://www.yunbtv.com/vodplay/yueyudiyiji-1-1.html"
    main(url)
