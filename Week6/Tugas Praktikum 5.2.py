A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = set()

# Hasil menggunakan fungsi .symmetric_difference()
print("Hasil menggunakan fungsi .symmetric_difference()")
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
print(A.symmetric_difference(C))
print(B.symmetric_difference(C))

# Hasil menggunakan simbol "^"
print("Hasil menggunakan simbol '^'")
print(A^B)
print(B^A)
print(A^C)
print(B^C)
