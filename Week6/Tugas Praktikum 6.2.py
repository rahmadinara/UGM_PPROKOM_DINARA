A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = set()

# Hasil menggunakan fungsi .difference()
print("Hasil menggunakan fungsi .difference()")
print(A.difference(B))
print(B.difference(A))
print(A.difference(C))
print(B.difference(C))

# Hasil menggunakan simbol "-"
print("Hasil menggunakan simbol '-'")
print(A-B)
print(B-A)
print(A-C)
print(B-C)