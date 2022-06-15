from PIL import Image
import os

path = "C:\\Users\\kt211\\Downloads\\1.png"

img = Image.open(path)
img = img.convert("RGB")
w, h = img.size
print(img.mode)
img.save("2.png")
# result = ""
# for x in range(w):
#     for y in range(h):
#         pixel = img.getpixel((x, y))
#         result += bin(pixel[2])[-1]
# print(result)
# a = 0
# pic = Image.new("RGB", (250, 250))
# for x in range(0, 250):
#     for y in range(0, 250):
#         if (result[a] == "0"):
#             pic.putpixel([x,y],255)
#         else:
#             pic.putpixel([x,y],0)
#         a += 1
# pic.save("12.png")
# pic.show()