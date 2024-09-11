print("MASUKKAN NILAI UNTUK MENGHITUNG RATA-RATA")
print("Ketik '-1' untuk keluar program")
#Menyiapkan list untuk data input
list_nilai = []
while(True):
    nilai = int(input("Masukkan nilai: "))
    #stop program
    if(nilai == -1 ):
        break
    #memasukkan input ke list
    list_nilai.append(nilai)
    #rumus rata-rata
    total = (sum(list_nilai)/len(list_nilai))
    print(total)
    