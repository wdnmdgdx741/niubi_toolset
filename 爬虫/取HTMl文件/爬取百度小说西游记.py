# coding: utf-8

# url="http://dushu.baidu.com/api/pc/getCatalog?data={"book_id" : "4306063500"}"   #所有章节的名称，cid
# url2="http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}"#小说内容

'''
同步操作：访问getCatalog拿到所有的章节cid名称
异步操作：访问getChapterContent下载章节中的内容
'''
import requests
import asyncio
import aiohttp
import aiofiles
import json


async def getChapterContent(cid, book_id, title):
    # data是一个json,转化为字符串
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f'http://dushu.baidu.com/api/pc/getChapterContent?data={data}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url)as resp:
            dic = await resp.json()

            async with aiofiles.open("D:\\桌面\\python\\爬虫\\text"+title+'.txt', mode='w', encoding='utf-8')as f:
                await f.write(dic["data"]["novel"]["content"])

async def getCatalog(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "http://dushu.baidu.com/pc/reader?gid=4306063500&cid=11348571"
    }
    resp = requests.get(url,headers=headers)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        print(title,cid)
        tasks.append(getChapterContent(cid, book_id, title))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    book_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id" : "' + book_id + '"}'
    # print(url)
    asyncio.run(getCatalog(url))
