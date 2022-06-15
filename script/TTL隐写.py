import binascii
with open('attachment.txt','r') as fp:
    a=fp.readlines()
    p=[]
    for x in range(len(a)):
       p.append(int(a[x])) 
    s=''
    for i in p:
        if(i==63):
            b='00'
        elif(i==127):
            b='01'
        elif(i==191):
            b='10'
        else:
            b='11'
        s +=b
# print(s)
flag = ''
for i in range(0,len(s),8):
    flag += chr(int(s[i:i+8],2))
flag = binascii.unhexlify(flag)
wp = open('ans.zip','wb')
wp.write(flag)
wp.close()
