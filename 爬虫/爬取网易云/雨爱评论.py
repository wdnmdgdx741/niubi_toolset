#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
网易云《雨爱》评论找到第二次请求url

'''
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json


#评论是通过这个url拿到的
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

#网页为POST提交，debug寻找到我们需要的未加密的源数据
'''
    {
    params: mJZiip2IkYpkIL+VZTvzj/135QupfrWNfWJutVtV61AIGiHWlkIBtnIJmLg36ab3w9CrMgmIJMEu2S3oWB5DL/DZbDp/pEHLxZIN+7Pzek/vYySaQkhItM7s8KnsrRienMpbgICgs41yGTp5DP5GIX4BSXKslrvx3rkbn6bXfY6n9BojR/+B/wShZzit1wfIoxzHh1bED3yNQ0vsy505yuMNR/L6jgZoX3drtLnK/ZuqgIyiLYqwYh8PtF8TO2LFK1SkwM5Z9wll6uZAnhsiyFgSEihAL12tlyq3ypdZOx0=
encSecKey: cdee3dbea23c783a4f30f3ad1be050a88f1438546e9594f97226922445e292ff6df634ad252af0cbf0f4f0c57effbcd788c84a9c02e0a2c7d52cba726460471ab831bbf5b43689a1a939a8a29f192a48535287c45f5918388faa7c25ec696bc834377a0dd194f95d5b5170cb37d98618d898face2563e315dcc9aa8d6a905134
}
通过这POST提价这两个参数，很明显这两个参数是加密过的，我们需要找到在网页中的加密过程
想看到网站的加密过程我们需要<栈跟踪(lnitiator)>，查看最后一次处理的过程(最上面的一条)，跳转到调试器(Soures)，({})查看源代码。
打上断点debug，刷新页面在右边Scope中找到我们要抓取的网页url，然后查看里面的params和encSecKey的数据看看有没有有被加密，
被加密就在Call Stack中一次寻找上一步，直到看到未加密的params和encSecKey，就是我们要找到源代码的地方，找到源代码，就会看到函数体，查看传参，找到数据从哪个变量传来的
就拿到了加密前的原data数据.
'''

#分析源代码中加密的过程，伪造加密过程
'''
首先我们通过debug可以看到原始数据是i9b，往回退返现经过这u9l.be9V个函数之后就被加密了，我们找到这个函数，看看这个函数做了什么。同样debug
一步步走找到加密的地方
            var bUG7z = window.asrsea(JSON.stringify(i9b), bsB3x(["流泪", "强"]), bsB3x(WU8M.md), bsB3x(["爱心", "女孩", "惊恐", "大笑"]));
            e9f.data = j9a.cs0x({
                params: bUG7z.encText,
                encSecKey: bUG7z.encSecKey
            })
这里可以看到i9b经过window.asrsea加密之后把值分别赋给了params和encSecKey
那么加密过程就是这个var bUG7z = window.asrsea(JSON.stringify(i9b), bsB3x(["流泪", "强"]), bsB3x(WU8M.md), bsB3x(["爱心", "女孩", "惊恐", "大笑"]));
搜索这个参数可以看到页面上只有两个地方拥有这两个参数，我们可以看到window.asrsea=d找到这个d
对应的d需要四个参数，那么看到window.asrsea就知道第一个参数就是i9b就是data,
本质上三个数据都可以通过控制台输出(Console),得到剩下的三个参数

得到这些参数就需要看abcd这几个函数做了什么事情
'''
#函数的分析过程
'''
function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)              
            e = Math.random() * b.length,       
            e = Math.floor(e),                  
            c += b.charAt(e);                   
        return c                                
    }
    function b(a, b) {                                           
        var c = CryptoJS.enc.Utf8.parse(b)                       
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")      
          , e = CryptoJS.enc.Utf8.parse(a)                       
          , f = CryptoJS.AES.encrypt(e, c, {                     
            iv: d,                                               
            mode: CryptoJS.mode.CBC                              
        });
        return f.toString()                                      
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)                                
    }

'''

data={              #d
    "cursor": -1,
    "offset": 0,
    "orderType": 1,
    "pageNo": 1,
    "pageSize": 20,
    "rid": "R_SO_4_1467444619",
    "threadId": "R_SO_4_1467444619"
}

e="010001"
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
i="v6JS9d0ApwXcmCPq"    #i=a(16)说明i就是a定义死了i，所以a也是不变的

# 通过固定随机数，获得浏览器加密之后的固定的seckey的值
def get_encSecKey():
    return "95538ced6cc5f92818807280fe4f3f42e2613d3c766486fa99824ae57eb60764cd021f40d9caae84222e0575d3010b6c6d919330fb345ed79a56bc79f5a578839a2606807b1d80f62986a413b00ccdf576f71da4eaf832fd8d00139b66fc56100e07c87d17ac631fef13f6865b8b1e29a0ca4f75366a400a1547d7cf61a445bc"

# 模拟浏览器对params加密的过程
def aes_encode(data):
    first = enc_Text(data,g)        # 调用enc_Text函数传参data=data,g=key
    two = enc_Text(first,i)         # 调用enc_Text函数传参first=data,i=key
    return two

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_Text(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"),mode=AES.MODE_CBC)  #创建加密过程
    bs = aes.encrypt(data.encode("utf-8"))  # 加密,因为加密出来的是字节流，不可以直接转化成string
    return str(b64encode(bs),'utf-8')       # 先把字节流转化成base64然后，转化为string

resp = requests.post(url,data={
    "params":aes_encode(json.dumps(data)),
    "encSecKey":get_encSecKey()
})
print(resp.text)



'''
首先要找到加密过程，理解加密函数中间做了些什么，然后会用python模拟加过程
从而拿到数据
'''

