oikea_tunnus = "phyton"
oikea_salasana = "rules"

yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Virheellinen tunnus tai salasana.")
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")

