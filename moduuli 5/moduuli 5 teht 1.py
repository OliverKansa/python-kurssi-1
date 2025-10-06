import random
lukumaara = int(input("kerro arpakuutioden lukumäärä?"))

summa = 0

for i in range(lukumaara):
    silmaluku = random.randint(1,6)
    summa += silmaluku

print (f"silmalukujen summa on {summa} ")