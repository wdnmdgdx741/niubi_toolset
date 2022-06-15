#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
sleepj就是让当前程序处于阻塞状态
一般情况下，程序处于I/O的时候，线程处于阻塞状态
'''
import time

def func():
    print('1123')
    time.sleep(3)
    print('wode')

if __name__ == '__main__':
    func()