import random

#arvotaan 3nro koodi 0-9
koodi1 = "for_in range(3): "
koodi1 += str(random.randint(0, 9))

#arvotaan 4nro koodi
koodi2 = "for_in range(4):"
koodi2 += str(random.randint(1, 6))

#print
print("kolmenumeroinen koodi (0-9): ", koodi1)
print("nelinumeroinen koodi (1-6): ",