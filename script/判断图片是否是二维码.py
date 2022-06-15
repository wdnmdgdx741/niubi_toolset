import cv2
import pyzbar.pyzbar as pyzbar
from PIL import Image
import os



def decode(path):
    sk = ""
    for i in range(1, 1236):
        s = path + '%04d.png' % i
        frame = Image.open(s)
        barcodes = pyzbar.decode(frame)
        data = ''
        for barcode in barcodes:
            data += barcode.data.decode("utf-8")
            sk += data
        # if data:
            # print('已识别二维码')
            print(sk)
        # else:
        #     print('图片 {} 不是二维码'.format(s))
        #     os.remove(s)


if __name__ == '__main__':
    # while True:
    #     filePath = input('请输入文件夹绝对路径：')
    #     for i, j, k in os.walk(filePath):
    #         # print(k)
    #         for files in k:
    #             file_name = filePath + '\\' + files
    decode("C:\\Users\\kt211\\Downloads\\IDM\\jj\\All\\")