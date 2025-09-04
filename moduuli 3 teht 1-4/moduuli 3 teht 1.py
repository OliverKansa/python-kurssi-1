pituus = float(input("kerro kuhan pituus senttimetreinä"))
if pituus < 37:
    print (f"Laske kuha takaisin järveen koska kuha on {37 - pituus:.2f} cm liian lyhyt" )
else:
    print("kuha on hyvän kokoinen")