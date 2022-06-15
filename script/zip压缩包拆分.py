#zip压缩包拆分
file = open("zip.zip", 'rb')
data = file.read(29830)
file.close()
firstMagic =b'\x50\x4b\x03\x04'
secondMagic = b'\x50\x4b\x01\x02'
thirdMagic = b'\x50\x4b\x05\x06'

filerecord = data.split(firstMagic)
del filerecord[0]
direntry =filerecord[24].split(secondMagic)
del filerecord[24]
filerecord.append(direntry[0])
del direntry[0]
endlocator = direntry[24].split(thirdMagic)
del direntry[24]
direntry.append(endlocator[0])
del endlocator[0]

assert len(filerecord) == 25 and len(direntry) == 25 and len(endlocator) == 1

for i in range(25):
	file = open(f"{i}.zip", 'wb')
	file.write(
	firstMagic + filerecord[i] + secondMagic + direntry[i] +thirdMagic + endlocator[0])
	file.close()