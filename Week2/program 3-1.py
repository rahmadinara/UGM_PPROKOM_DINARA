n=int(input("Masukkan waktu dalam detik: "))
a=60*60*24
hari=n//a
b=a*hari
c=n-b
jam=(c//(60*60))
d=jam*(60*60)
e=c-d
menit=e//60
detik=n%60

print("%d hari %d jam %d menit %d detik"%(hari,jam,menit,detik))
