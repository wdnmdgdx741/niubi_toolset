#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
找到请求的网页，得到加密前的数据
伪造加密
获取数据

window.asrsea生成params =》params   encSecKey =》encSecKey
'''

from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests


#url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
#params、encSecKey
#post请求，分析出未加密之前的数据
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1846489646",
    "threadId": "R_SO_4_1846489646"
}
e="010001"
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
i="wGWTj7Di1K1eDu7n"




def get_encSecKey():
    return "b411c44c55d747fe2d3765928643ea6ec1b598d504b73f41e3878df4c4f0829567ccb3e356a54f7e163b4f8d9eb7a641c65813dba84dcb0a3aec442c5045ff58397eeeeb002a137e0970b04f6ca04c192822840e7245f9c16aa0681975f72350ee4b5bdccf4005bd905be72e371a809d6aba5b9e9e21eb11ad49f4b0861428d7"

def get_params(data):           #现在我的data是字典，先默认我收到的是string
    first = enc_params(data,g)
    two = enc_params(first, i)
    return two                      #返回的就是params

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_params(data, key):          #AES加密过程
    iv = '0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"),mode=AES.MODE_CBC)     #加密器
    bs = aes.encrypt(data.encode("utf-8"))               #加密,加密的内容必须是16的倍数
    return str(b64encode(bs),"utf-8")    #转化成字符串返回


#处理加密过程
'''
function a(a=16) {              随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)              循环16次
            e = Math.random() * b.length,       随机数1.23213
            e = Math.floor(e),                  取整1
            c += b.charAt(e);                   字符串第1个 b
        return c                                返回随机的16位字符串
    }
    function b(a, b) {                          a是要加密的内容，就是数据data
        var c = CryptoJS.enc.Utf8.parse(b)      b就是密钥，往回看g就是密钥，i也是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)      e就是数据
          , f = CryptoJS.AES.encrypt(e, c, {    AES加密算法
            iv: d,                              偏移量=0102030405060708
            mode: CryptoJS.mode.CBC             加密模式
        });
        return f.toString()                     最后返回f字符串的形式
    }
    function c(a, b, c) {           c里面是不产生随机数的
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {   
        var h = {}                  #空对象
          , i = a(16);              i就是一个随机的16位字符串
        return h.encText = b(d, g),         b是密钥对应g就是密钥，对应下面i也是密钥
        h.encText = b(h.encText, i),        返回的就是params
        h.encSecKey = c(i, e, f),           返回的就是encSecKey，传入的数据e和f是固定的，i是一个随机的，如果我们固定i那么说明结果就是固定的
        return h
    }
这里进行了两次加加密，第一次把data数据+g => b ==> h.encText,第二次加密是h.encText+i ==> b,形成最终的h.encText -> params
return h.encText = b(d, g),
h.encText = b(h.encText, i),

'''

resp = requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})

r = open("嘉宾网易云音乐评价.csv","w",encoding='utf-8')
misc = "网易云嘉宾，热评！！"
r.write(misc+'\n\n')

dic = resp.json()
print(dic)


for i in range(0,20):
    reping = dic["data"]["comments"][i]["content"]+'\n'
    r.write(reping)
r.close()
print("over!!!")

