luku = int(input("anna kokonaisluku:"))

if luku < 2:
    print ("luku ei ole alkuluku")
else:
    alkuluku = True
    for i in range (2, luku):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print("luku on alkuluku")
    else:
        print("luku ei ole alkuluku")



