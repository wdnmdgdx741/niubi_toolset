#!/usr/bin/env python
# -*- coding: utf-8 -*-
#线程池一次性开辟多个贤臣，不要要自己手动一个个开启
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
#分别是线程池和进程池

def fn(name):
    for i in range(100):
        print(name)


if __name__ == '__main__':
    #创建线程池，线程次开辟50个线程
    with ThreadPoolExecutor(50) as t:
        for i in range(2):
            t.submit(fn, name=f'线程{i}')

    print("123")



