angka = [4,5,11,12,14,16,16,19]
prima = []

for a in angka:
    if a > 1 or a == 2:
        if (a%2) != 0:
            prima.append(a)
    else:
        break

print("Bilangan prima : ",prima)
print("Terdapat ", str(len(prima)), "bilangan prima dalam array")