import os
from PIL import Image
import pyzbar.pyzbar as pyzbar
from base64 import b64decode


def Blue_corl(path, save_path):
    dirlist = os.listdir(path)
    a, b = 111, 54
    pic_1 = Image.new("L", (a, b), 255)
    for i in dirlist[0:]:
        pic = Image.open(path + i)
        for y in range(b):
            for x in range(a):
                pixel = pic.getpixel((x, y))[3] % 2  #RGBA
                if pixel == 0:
                    pic_1.putpixel((x, y), 0)
                else:
                    pic_1.putpixel((x, y), 255)
        pic_1.save(save_path + i)
    print("over!!!")


# def CQR_qr(save_path):
#     flagbase = ""
#     for i in range(1, 1236):
#         # im = Image.open()
#         s = save_path + '%04d.png' % i
#         # print(pyzbar.decode(Image.open(s))[0].data.decode())
#         flagbase += pyzbar.decode(Image.open(s))[0].data.decode()
#
#     flag = b64decode(flagbase).decode('UTf-8')
#     while True:
#         flag = b64decode(flag).decode('UTf-8')
#         if "flag" in flag:
#             print(flag)
#             break
#         else:
#             continue


if __name__ == '__main__':
    path = "C:\\Users\\kt211\\Downloads\\IDM\\jj\\kali\\"
    save_path = "C:\\Users\\kt211\\Downloads\\IDM\\jj\\A\\"
    Blue_corl(path, save_path)
    # CQR_qr(save_path)

# pic = Image.open("C:\\Users\\kt211\\Downloads\\IDM\\kali\\0001.png")
# print(pic.mode)
