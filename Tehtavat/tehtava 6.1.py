import random

def heitto():
    return random.randint(1,6)

def main():
    luku = 0
    while luku != 6:
        luku = heitto()
        print("heitit",luku)
if __name__ == "__main__":
    main()

