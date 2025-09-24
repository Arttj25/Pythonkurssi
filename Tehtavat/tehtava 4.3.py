luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break

    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötäthän kelvollisen luvun.")

if len(luvut) > 0:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et antanut yhtään lukua.")
