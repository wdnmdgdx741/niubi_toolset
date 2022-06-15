import base64

with open('out.txt','r') as file:
    for i in file.readlines():
        line = str(base64.b64decode(i),'utf8')
        # print(line.replace('1',' '))
        print(line)
