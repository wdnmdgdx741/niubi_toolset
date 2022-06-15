#压缩文件以文件名作为密码无线套完，使用这个脚本
import zipfile
name = '0114'
while True:
    fz = zipfile.ZipFile(name + '.zip', 'r')
    #这里可以改文件压缩后缀如".rar",".zip",".tar.gz"
    fz.extractall(pwd=bytes(name, 'utf-8'))
    name = fz.filelist[0].filename[0:4]
    fz.close()
