import numpy as np
import string
# abcdefghijklmnopqrstuvwxyz
lower_case = string.ascii_lowercase

cipher = 'xihlsseaoy'

cipher = 'xhseoilsay'
# 找到下标后，缩放成2*5的数组
cipher_arr = np.resize(np.array([lower_case.index(c) for c in cipher]),(2,5))
# 转换成矩阵类型，方便接下来的运算
cipher_matrix = np.matrix(cipher_arr)

"""
x i h l s
s e a o y
"""
"""
x h s e o
i l s a y

23 7 18 4 14
8 11 18 0 24
A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
"""
# 2*2
A = np.matrix(np.array([[1,2],[0,1]])) 
# A的逆矩阵
A_inv = A.I
B = A_inv * cipher_matrix
print(B)
flag = np.resize(B,(1,10)).tolist()[0]
print(''.join([lower_case[int(x)%26] for x in np.resize(B,(1,10)).tolist()[0]]))


"""
hlies
ilsay
hilliseasy
"""
# flag提交格式SeBaFi{hilliseasy}