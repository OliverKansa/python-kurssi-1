sukupuoli = input("Kerro sukupuolesi")
hemooglobiini = int(input("anna hemoglobiiniarvo"))

if sukupuoli == "mies":
    if hemooglobiini < 134:
        print("arvosi on alhainen")
    elif hemooglobiini <= 195:
        print("arvosi on normaali")
    else:
        print("arvosi on koholla")
if sukupuoli == "nainen":
    if hemooglobiini < 117:
        print("arvosi on alhainen")
    elif hemooglobiini <= 175:
         print("arvosi on normaali")
    else:
        print("arvosi on koholla")


