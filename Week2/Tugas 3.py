# masukkan input dalam detik
n=int(input("Masukkan waktu dalam detik: "))

# variabel pembagi detik ke hari
a=60*60*24

# cari nilai hari - bagi detik dengan pembagi
hari=n//a

# cari jumlah detik yang telah diubah ke hari
b=a*hari

# jumlah detik sisa
c=n-b

# gunakan detik sisa untuk mencari jam
jam=(c//(60*60))

# cari jumlah detik yang diubah ke jam
d=jam*(60*60)

# jumlah detik sisa
e=c-d

# gunakan detik sisa untuk mencari menit
menit=e//60

# hasil detik
detik=n%60

print("%d hari %d jam %d menit %d detik"%(hari,jam,menit,detik))
