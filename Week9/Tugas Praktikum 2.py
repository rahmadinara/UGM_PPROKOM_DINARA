nilai_mahasiswa = []

for i in range(1,6):
    nilai = float(input("Masukkan nilai mahasiswa ke-"+str(i)+": "))
    nilai_mahasiswa.append(nilai)

while True:
    print("Menu:")
    print("""
    - Ketik "jumlah" untuk lihat jumlah
    - Ketik "rata-rata" untuk lihat rata-rata
    - ketik "keluar" untuk keluar
    """)
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "jumlah":
        print("Data total nilai mahasiswa: ", sum(nilai_mahasiswa))
    
    elif pilihan == "rata-rata":
         print("Data nilai rata-rata mahasiswa: ", (sum(nilai_mahasiswa)/len(nilai_mahasiswa)))

    elif pilihan == "keluar":
        break

    else:
        print("""
        - Perintah tidak valid
        - hanya tersedia untuk :
          "jumlah"
          "rata-rata"
          "keluar"
        """)