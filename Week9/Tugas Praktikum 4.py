array_elemen = []
jumlah_elemen = int(input("Masukkan jumlah elemen dalam array: "))

for jumlah in range(1,jumlah_elemen+1):
    array_elemen.append(jumlah)
print(array_elemen)

elemen_kelipatan = []
jumlah_kelipatan = int(input("Masukkan kelipatan yang ingin ditampilkan: "))

for elemen in array_elemen:
    if elemen%jumlah_kelipatan==0:
        elemen_kelipatan.append(elemen)
    else:
        continue
        print("tidak ada data")
print(elemen_kelipatan)
