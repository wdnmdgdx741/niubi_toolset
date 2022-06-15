# coding: utf-8
import aiohttp
import asyncio

urls=[
    "http://kr.shanghai-jiuxin.com/file/2020/1031/a2c58d6d726fb7ef29390becac5d8643.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/d7de3f9faf1e0ecdea27b73139fc8d3a.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/3ed27e5aedc2673755bf3327e9dcc13b.jpg"
]

async def download(url):
    #aiohttp.ClientSession() <===>requests
    filename = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url)as resp:
            with open(filename,'wb')as f:
                f.write(await resp.content.read())

    print(url,'over!!!')


async def main():
    tasks=[]
    for url in urls:
        d = download(url)
        tasks.append(d)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())