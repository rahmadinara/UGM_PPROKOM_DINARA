m = 2
n = 3
x = [[0] * n for x in range(m)]
for i in range(m):
    for j in range(n):
        x[i][j] = int(input(f"Masukkan nilai ke-[{i}][{j}]: "))

print(x)