import string
s = "$Bn$Ai$An$Ac$Al$Au$Ad$Ae$Bk$Cc$As$At$Ad$Ai$Ao$By$Ah$Ce$Ai$An$At$Bk$Am$Aa$Ai$An$Bs$Bt$Cn$Ap$Ar$Ai$An$At$Bs$Bm$Aw$Dd$Al$Ac$Da$Am$Ae$Cl$De$Ao$Cl$Dj$Ak$Ac$At$Df$Bm$Bt$Cb$Ar$Ae$At$Au$Ar$An$Bk$Da$Cb$Cp"
ll = s.split('$')
list1 = ['Bk','Bm','Bn','Bs','Bt','By','Cb','Cc','Ce','Cl','Cn','Cp',
'Da','Db','Dc','Dd','De','Df','Dg','Dh','Di','Dj']
list2 = [' ','"','#','(',')','.','','<','>','_','{','}','0','1','2','3','4','5','6','7','8','9']
list3 = []
list4 = []
s = string.ascii_lowercase
for i in s:
	list3.append('A%s'%i)
	list4.append(i)
#print(list3,'\n',list4)

t = ''
for i in range(0,len(ll)):
	for j in range(0,len(list1)):
		if ll[i]==list1[j]:
			t += list2[j]
	for k in range(0,len(list3)):
		if ll[i]==list3[k]:
			t +=list4[k]
print(t)
