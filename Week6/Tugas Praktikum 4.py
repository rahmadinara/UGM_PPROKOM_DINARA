A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

# Hasil menggunakan fungsi .union()
print("Hasil menggunakan fungsi .union()")
print(A.union(B))
print(B.union(C))
print(B.union(C).union(D))
print(A.union(B).union(C).union(D))

# Hasil menggunakan simbol "|"
print("Hasil menggunakan simbol '|'")
print(A | B)
print(B | C) 
print(B | C | D)
print(A | B | C | D)


