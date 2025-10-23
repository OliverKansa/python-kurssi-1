import random

def noppa(tahkot):
    return random.randint (1, tahkot)


maara = int(input("anna tahkojen maara"))

luku = 0


while luku != maara:
    luku = noppa(maara)
    print ("luku:", luku)

