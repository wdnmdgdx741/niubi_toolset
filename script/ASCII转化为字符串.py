f=open('1.txt','r').readlines()
for i in f:
	print(chr(int(i)),end="")