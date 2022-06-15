data = open("photo.dat",'rb')
strs = data.read()
flag = open("1.jpg",'ab+')
for i in strs:
    flag.write(bytes([i ^ 0x33]))
