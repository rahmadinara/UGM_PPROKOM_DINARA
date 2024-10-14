angka = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]
genap = []
ganjil = []

for a in angka:
    if a % 2 == 0:
        genap.append(a)
    else:
        ganjil.append(a)

print("Angka genap\t:",genap)
print("Jumlah genap\t: "+str(len(genap))+" angka")
print("Angka ganjil\t:",ganjil)
print("Jumlah ganjil\t: "+str(len(ganjil))+" angka")
