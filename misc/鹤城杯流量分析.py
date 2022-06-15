# coding: utf-8
with open('data1.txt', 'r', encoding='UTF-8') as f:
    data = f.read().strip().replace("%20"," ").split('\n')
flag = [0 for i in range(50)]   # 创建了一个index为50个，value为0的数组
for i in data:
    flag[int(i[34:i.find(',', 34)])] = int(i[i.find('=') + 1:i.find('--+')])
    # 把 int(i[73:i.find(',', 73)])作用limit 0,1),2,1))中2,1的2提出来作为flag数组中索值
    # 把 int(i[i.find('=') + 1:i.find(',sleep')])作用0,1),2,1))=80,sleep(5),1)中=80的值赋给flag数组中索引为1的value
    # 每次for都会把最后一个索引的值赋给flag索引位置的value
print(bytes(flag))
# bytes就是以字节的形式储存数据，通常在数据前面会带上b'\
print(bytes(flag).decode())
