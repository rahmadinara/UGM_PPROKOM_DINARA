nilai = {3,6,9,2,5,7}
tambah = {1,4,8,10}
hapus = {1,3,4,5,7,8,10}

# tambah elemen baru
nilai.update(tambah)
print(nilai)

# hapus elemen
nilai.difference_update(hapus)
print(nilai)