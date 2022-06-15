file = open("C:\\Users\\kt211\\Downloads\\swap_insert.zip", 'rb')

data = file.read(19582)
print(data)
file.close()

firstMagic = b'\x50\x4b\x03\x04'
secondMagic = b'\x50\x4b\x01\x02'
thirdMagic = b'\x50\x4b\x05\x06'
filerecord = data.split(firstMagic)
print(filerecord)
del filerecord[0]
direntry = filerecord[24].split(secondMagic)
del filerecord[56]
filerecord.append(direntry[0])
del direntry[0]
endlocator = direntry[84].split(thirdMagic)
del direntry[84]
direntry.append(endlocator[0])
del endlocator[0]
assert len(filerecord) == 25 and len(direntry) == 25 and len(
    endlocator) == 1
for i in range(25):
    file = open(f"{i}.zip", 'wb')
file.write(firstMagic + filerecord[i] + secondMagic + direntry[i] +
    thirdMagic + endlocator[0])
file.close()