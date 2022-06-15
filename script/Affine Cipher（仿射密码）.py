#题目：hwwfutfjstgbzxxq ,y=3x+7,flag 格式是 SeBaFi{}
flag = "hwwfutfjstgbzxxq"
flaglist = []
for i in flag:
    flaglist.append(ord(i)-97)
flags = ""
for i in flaglist:
    for j in range(0,26):
        #对应这里的乘积
        c = (3 * j + 7) % 26
        if(c == i):
            flags += chr(j+97)
print(flags)
