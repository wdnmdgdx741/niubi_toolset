#size偏移数，010右下角的大小
the_size = input("请输入bmp文件像素大小：")
#图片高度十进制
the_height = input("请输入bmp文件高度：")
#图片宽度十进制
the_width = input("请输入bmp文件宽度：")
#53文件头大小53
Length_and_width = (int(the_size) - 53) / 3

height = Length_and_width / int(the_width)

width = Length_and_width / int(the_height)

print("高度正确时,宽度为：",width)

print("宽度正确时,高度为：",height)