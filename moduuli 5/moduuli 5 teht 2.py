luvut = []

while True:
    luku = input("anna luku. tyhjä lopettaa")
    if luku == "":
        break
    luvut.append(float(luku))

luvut.sort(reverse=True)
print ("viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)
