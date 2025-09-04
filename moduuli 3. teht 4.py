vuosiluku = int(input("kerro vuosiluku: "))

if vuosiluku % 400 == 0:
      print("Vuosi on karkausvuosi")

elif vuosiluku % 100 == 0:
    print("Vuosi ei ole karkausvuosi")

elif vuosiluku % 4 == 0:
    print("Vuosi on karkausvuosi")

else:
    print("vuosi ei ole karkaus vuosi")

