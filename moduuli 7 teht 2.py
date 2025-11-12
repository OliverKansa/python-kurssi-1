nimet = set()

while True:
    nimi = input("nimi:")

    if nimi == "":
        break


    if nimi in nimet:
        print("syötetty nimi:", nimet)
    else:
        print("uusi nimi")
        nimet.add(nimi)

print("syötetyt nimet:")
for n in nimet:
    print(n)