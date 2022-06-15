#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio          #多异步携程模块
import time

# async def func():
#     print('helloworld!')
#     #time.sleep(3)#sleep是同步操作，当程序中出现同步操作，异步就失效了
#     await asyncio.sleep(3)    #异步操作,await挂起的操作
#     print('helloworld!')
#
# async def fun1():
#     print('123')
#     await asyncio.sleep(2)
#     print('123')
#
# async def fun2():
#     print('你好!')
#     await asyncio.sleep(4)
#     print('没见!')

# if __name__ == '__main__':
#     f1 = func()
#     f2 = fun1()
#     f3 = fun2()
#
#     tasks=[
#         f1,f2,f3
#     ]
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2-t1)

async def download(url):
    print('正在下载')
    await asyncio.sleep(3)
    print('下载完成')


async def main():
    lst=[
        'baidui.com',
        'google.com',
        'sougou.com'
    ]
    tasks=[]
    for url in lst:
        d = download(url)
        tasks.append(d)

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())