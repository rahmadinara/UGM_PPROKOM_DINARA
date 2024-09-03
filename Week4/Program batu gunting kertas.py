sign1 = input("Pilih mana, Batu/Gunting/Kertas: ")
sign2 = input("Lawan mana, Batu/Gunting/Kertas: ")
sign1 = sign1.lower()
sign2 = sign2.lower()

print()
if sign1 == "batu":
    if sign2=="batu":
        print("DRAW")
    elif sign2 == "gunting":
        print("Batu WIN")
    elif sign2 == "kertas":
        print("Kertas WIN")
elif sign1 == "gunting":
    if sign2=="batu":
        print("Batu WIN")
    elif sign2 == "gunting":
        print("DRAW")
    elif sign2 == "kertas":
        print("Gunting WIN")
elif sign1 == "kertas":
    if sign2=="batu":
        print("Kertas WIN")
    elif sign2 == "gunting":
        print("Gunting WIN")
    elif sign2 == "kertas":
        print("DRAW")
else:
    print("Coba lagi, yuk!")