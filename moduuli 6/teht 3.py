def bensa (gallona):
  return gallona * 3.785

while True:
    gallona = float(input("anna gallonat, negatiivinen lopettaa: "))
    if gallona < 0:
        break

    litra = bensa (gallona)
    print("bensa:", litra)
