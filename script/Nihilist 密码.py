# 原26个英文字母为ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 把关键字提前后为LOVEKFCABDGHIJMNPQRSTUWXYZ
# 在置换后的序列里可以发现对应关系P=Q，V=C，S=T，F=F

import string

enc = 'PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}'#密码
grid = 'LOVEKFC' + 'ABDGHIJMNPQRSTUWXY'#解密密钥
flag = ''

for i in enc:
    if i in string.ascii_lowercase:
        index = grid.lower().index(i)
        flag += string.ascii_lowercase[index]
        continue
    if i in string.ascii_uppercase:
        index = grid.upper().index(i)
        flag += string.ascii_uppercase[index]
        continue
    flag += i
print(flag)