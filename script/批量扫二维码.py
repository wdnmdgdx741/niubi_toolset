from PIL import Image
import pyzbar.pyzbar as pyzbar
from base64 import b64decode


def CQR_qr(save_path):
    flagbase = ""
    for i in range(1, 313):
        # im = Image.open()
        s = save_path + '%03d.png' % i
        # print(pyzbar.decode(Image.open(s))[0].data.decode())
        flagbase += pyzbar.decode(Image.open(s))[0].data.decode()

    flag = b64decode(flagbase).decode('UTf-8')
    while True:
        flag = b64decode(flag).decode('UTf-8')
        if "flag" in flag:
            print(flag)
            break
        else:
            continue


if __name__ == '__main__':
    save_path = "C:\\Users\\kt211\\Downloads\\qrimg的附件_2\\2\\"
    CQR_qr(save_path)
