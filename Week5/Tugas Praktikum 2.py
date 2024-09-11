awal = int(input("Masukan saldo awal: "))
sisa = awal
while (True):
    pengeluaran = int(input("Masukkan pengeluaran hari ini (0 untuk keluar): "))
    #tampilkan sisa, hentikan loop
    if pengeluaran == 0:
        print("Sisa saldo: ", sisa)
        break
    #hitung sisa saldo
    sisa -= pengeluaran
    #jika sisa kurang dari 0
    if sisa<0:
        print("Saldo tidak cukup")
        print("Sisa saldo: ", sisa+pengeluaran)
        break