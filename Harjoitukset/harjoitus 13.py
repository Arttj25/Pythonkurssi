import math

while True:
    try:
        luku = int(input("Syötä kokonaisluku: "))

        if luku < 0:
            print("Virheellinen numero")
        elif luku > 0:
                juuri = math.sqrt(luku)
                print(f"Luvun neliöjuuri on: {juuri}")
        else:
             break # jos luku on 0 poistutaan silmukasta
    except ValueError:
        print("Syötäthän kokonaisluvun")