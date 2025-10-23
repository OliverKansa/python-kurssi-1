def yhteensa (lista):
    yhteensa = 0
    for luku in lista:
        yhteensa += luku
    return yhteensa

luvut = [1, 9, 4, 2, 6, 2, 4]
tulos = yhteensa(luvut)
print ("lukujen summa on:", tulos)