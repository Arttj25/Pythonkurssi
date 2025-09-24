from sys import excepthook

print("Valitse mitä toimintoa haluat käyttää: \n A: Yhteenlasku \n B: Vähennyslasku"
      "\n C: Kertolasku \n D: Jakolasku ")

valinta = input("Valintasi (A - D:) ").upper()
a = float(input("Anna ensimmäinen luku"))
b = float(input("Anna toinen luku"))

if valinta == "A":
    print("yhteenlasku", a + b)
elif valinta == "B":
    print("Vähennyslasku", a - b)
elif valinta == "C":
    print("Kertolasku", a * b)
elif valinta == "D":
    print("Desimaalijakolasku", a / b)
else:
    print("Valintasi oli virheellinen!")

while True:
    print("\nValitse toiminto (+,-,*,/) tai lopeta kirjoittamalla 'lopeta'")
    toiminto = input("Toiminto: ")

    if toiminto == "lopeta":
        print("Lopetetaan laskin.")
        break

    if toiminto not in ["+", "-", "*", "/"]:
        print("Virheellinen toiminto!")
        continue

    try:
        a = float(input("Anna ensimmäinen luku"))
        b = float(input("Anna toinen luku"))

        if toiminto == "+":
            print("yhteenlasku", a + b)

        elif toiminto == "-":
            print("Vähennyslasku", a - b)

        elif toiminto == "*":
            print("Kertolasku", a * b)

        elif toiminto == "/":
            if b == 0:
                print("Nollalla ei voi jakaa")
                continue
            tulos = a / b
            print(f"tulos: {tulos}")

    except ValueError:
        print("Syötäthän kelvolliset numerot.")
