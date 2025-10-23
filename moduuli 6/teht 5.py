def parittomat(lista):
    uusi = []
    for luku in lista:
        if luku % 2 == 0:
            uusi.append (luku)
    return uusi

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = (parittomat(lista1))

print ("lista1:", lista1)
print ("lista2:", lista2)