#文件重命名.jpg
import os
#文件地址
path = 'D:\\桌面\\脚本\\脚本\\beisi'
for i in os.listdir('./beisi'):
	if i == 'flag.zip':
		continue
	else:
		oldname = os.path.join(path,i)
		newname = os.path.join(path,i+'.jpg')
		os.rename(oldname,newname)