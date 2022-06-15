from PIL import Image

mother_path = r"C:\\Users\\kt211\\Downloads\\IDM\\target\\target\\"
byte_strings = ""
for j in range(0, 336):
    real_path = mother_path + str(j) + ".png"
    im = Image.open(real_path, 'r')
    pix = im.load()
    Color = pix[0, 0][0]
    if Color == 255:
        byte_strings += "0"
    else:
        byte_strings += "1"
    print(real_path)
print(byte_strings)

