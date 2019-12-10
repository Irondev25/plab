from operator import itemgetter
l=[['H',20],['B',20],['V',19],['K',19],['Z',19]]
m=min(l,key=itemgetter(1))[1]
f=[x for x in l if x[1]!=m]
mf=min(f,key=itemgetter(1))[1]
out=[x for x in f if x[1]==mf]
out.sort()
for i in range (0,len(out)):
    print(out[i][0])
