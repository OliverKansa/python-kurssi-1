pituus = int(input("anna pituutesi:"))
paino = float(input("anna painosi:"))

#muuttuja jossa lasku suoritetaan
bmi = paino / (pituus / 100) ** 2

print("pituus-paimo-indeksi on", bmi)
print(f"pituus-paino-indeksi on {bmi:.2f}")
