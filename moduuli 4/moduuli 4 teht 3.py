luvut = []

while True:
    luku = input("Anna luku (tyhjä lopettaa): ")
    if luku == "":
        break
    luvut.append(float(luku))

if luvut:
    print("Pienin luku:", min(luvut))
    print("Suurin luku:", max(luvut))
else:
    print("Et syöttänyt yhtään lukua.")