import zipfile

first = '1595'
sed = first + '.zip'
Dir = 'D:/CTF/20210202/'
file = 'D:/CTF/20210202/' + first + '.zip'
for y in range(1, 1000):
    print(y)
f = zipfile.ZipFile(file, 'r')
zip_list = f.namelist()
for x in zip_list:
    m = x.split(".")
m = m[0]
f.extract(x, path = Dir, pwd = m)
Dir = 'D:/CTF/20210202/'
file = Dir + m + '.zip'
sed = m[0] + '.zip'
f.close()