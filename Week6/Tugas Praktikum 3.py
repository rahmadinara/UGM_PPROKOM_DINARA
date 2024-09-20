A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

# hasil menggunakan fungsi .intersection()
print("Hasil menggunakan fungsi .intersection()")
print(A.intersection(D))
print(B.intersection(D))
print(C.intersection(D))
print(A.intersection(B).intersection(C).intersection(D))

# hasil menggunakan simbol "&"
print("Hasil menggunakan simbol '&'")
print(A & D)
print(B & D)
print(C & D)
print(A & B & C & D)