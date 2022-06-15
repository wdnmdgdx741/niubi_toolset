from PIL import Image
pic = Image.open('1.png')
width,height = pic.size
flag = ''
num = -1
i = [1,0,1,3,2,4,3,0]
for x in range(width):
    for y in range(height):
        if num <= 500:
            num += 1
            if pow(2,i[num % 8]) == pic.getpixel((x,y))[3]:
                flag += '1'
            else:
                flag += '0'
        else:
            print(flag)
            break
