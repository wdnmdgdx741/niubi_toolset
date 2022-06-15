with open('cipher.txt') as f:
    f = f.read()
    for sub in range(200):
        flag = ''
        for i in range(0,len(f),2):
            data = int(f[i:i+2],16)
            data = data - sub
            try:
                flag += chr(data)
            except:
                pass
        if 'flag{' in flag:
            print(flag)
        else:
            pass