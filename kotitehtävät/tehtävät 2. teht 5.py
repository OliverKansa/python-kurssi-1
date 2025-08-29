leiviskat = float(input("anna leiviskat: "))
naulat = float(input("anna naulat: "))
luodit = float(input("anna luodit: "))

#määritys
naulaa_per_leiviska = 20
luotia_per_naula = 32
grammaa_per_luoti = 13.3

#muunnetaan
luodit_yhteensa = (leiviskat * naulaa_per_leiviska *luotia_per_naula + naulat * luotia_per_naula + luodit)


#grammoiksi
grammat_yhteensa = (grammaa_per_luoti * luodit_yhteensa)

#kg ja g
kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000

#print
print (f"massa nykymittojen mukaan:" )
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa")
