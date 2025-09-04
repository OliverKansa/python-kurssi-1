hyttiluokka = input("kerro hyttiluokkasi ( LUX, A, B, C ): ")
if hyttiluokka == "LUX":
    print("on parvekkeellinen hytti yläkannella")
elif hyttiluokka == "A":
    print ("ikkunallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print("ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print("on ikkunaton hytti autokannen alapuolella")
else:
    print("virheellinen hyttiluokka")