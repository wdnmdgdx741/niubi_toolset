#!/usr/bin/env python
# -*- coding: utf-8 -*-
#进程就像是运行的软件，线程就像是软件中的功能
#开一个软件，软件本身就是进程，使用很多的功能就是线程

from threading import Thread

'''
定义函数创建多线程

def func():
    for i in range(1000):
        print('func',i)

def fun1():
    for i in range(1000):
        print('fun1',i)

if __name__ == '__main__':
    t = Thread(target=func) # 创建线程并安排任务
    t.start()               # 开始执行该线程，多线程状态为可以执行，执行什么时候开始是由cpu决定
    t1 = Thread(target=fun1)
    t1.start()

    for i in range(1000):
        print('main',i)    

'''
# 创建线程类
class MyThread(Thread):
    def func(self):
        for i in range(1000):
            print('子线程',i)

if __name__ == '__main__':
    t = MyThread()
    t.start()

    for i in range(1000):
        print("主线程",i)