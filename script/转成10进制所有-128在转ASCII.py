# -*- coding:utf-8 -*-zhua
# author: mochu7
def hex_str(str):#对字符串进行切片操作，每两位截取
    hex_str_list=[]
    for i in range(0,len(str)-1,2):
        hex_str=str[i:i+2]
        hex_str_list.append(hex_str)
    print("hex列表：%s\n"%hex_str_list)
    hex_to_str(hex_str_list)


def hex_to_str(hex_str_list):
    int_list=[]
    dec_list=[]
    flag=''
    for i in range(0,len(hex_str_list)):#把16进制转化为10进制
        int_str=int('0x%s'%hex_str_list[i],16)
        int_list.append(int_str)
        dec_list.append(int_str-128)#-128得到正确的ascii码
    for i in range(0,len(dec_list)):#ascii码转化为字符串
        flag += chr(dec_list[i])
    print("转化为十进制int列表：%s\n"%int_list)
    print("-128得到ASCII十进制dec列表：%s\n"%dec_list)
    print('最终答案：%s'%flag)


if __name__=='__main__':
    str='d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9b2b2e1e2b9b9b7b4e1b4b7e3e4b3b2b2e3e6b4b3e2b5b0b6b1b0e6e1e5e1b5fd'
    print("字符串长度：%s"%len(str))
    hex_str(str)