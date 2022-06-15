import pickle

# 打开序列化文件
fp = open("2.txt", "rb+")

# 打开保存文件
fw = open('pickle.txt', 'w')

# 反序列化文件编译
a = pickle.load(fp)

# 转换成字符串要不然不能保存
pickle = str(a)

# 写入文件
fw.write(pickle)

# 关闭文件
fw.close()

# 关闭文件
fp.close()