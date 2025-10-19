import random

maara = int(input("Montako noppaa heitetään? "))

summa = 0

for i in range(maara):
    summa += maara
    luku = random.randint(1, 10)
    print(f"{i+1}.noppa: {luku}")

summa+= luku

print(f"Noppien summa on {summa}.")