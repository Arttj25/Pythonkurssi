import random

def heitto():
    return random.randint(1, tahkot)

def main():
    tahkot = int(input("Anna tahkojen lukumäärä:"))

    luku = 0
    while luku != tahkot:
        luku = tahkot
        print("heitit",luku)

    print("sait maksimiluvun:" , tahkot)



if __name__ == "__main__":
    main()
