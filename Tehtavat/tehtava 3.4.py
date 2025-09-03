vuosiluku = int(input("Kerro vuosiluku?"))

if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
    print(f"{vuosiluku} on Karkausvuosi. ")
else:
    print(f"{vuosiluku} ei ole Karkausvuosi. ")





