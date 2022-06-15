import zlib
import struct

filename = "C:\\Users\\kt211\\Downloads\\IDM\\123.jpg"
with open(filename, 'rb') as f:
    all_b = f.read()
    # png的索引位置
    # w = all_b[16:20]
    # h = all_b[20:24]
    # jpg的索引位置
    # w = all_b[159:161]
    # h = all_b[157:159]
    # 生成901到1199的数
    for i in range(1, 2000):
        name = str(i) + ".jpg"
        f1 = open("E:\\脚本\\script\\images\\" + name, "wb")
        # im = all_b[:20]+struct.pack('>i',i)+all_b[24:]      # png图片
        # im = all_b[:16]+struct.pack('>i',i)+all_b[20:]      # png图片
        # im = all_b[:213] + struct.pack('>h', i) + all_b[215:]  # jpg图片
        # im = all_b[:215] + struct.pack('>h', i) + all_b[217:]  # jpg图片
        f1.write(im)
        f1.close()
