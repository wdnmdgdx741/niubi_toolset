# coding: utf-8
import re

lst = []
with open("3.txt","r", encoding='UTF-8') as f:
    text = f.read()
    lst.append(text)
    for i in lst:
        print(i)