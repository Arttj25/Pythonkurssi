import random

# Kysy käyttäjältä pisteiden määrä
try:
    N = int(input("Kuinka monta pistettä arvotaan? "))
    if N <= 0:
        print("Pisteiden määrän on oltava positiivinen kokonaisluku.")
    else:
        ympyrassa = 0

        for _ in range(N):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 < 1:
                ympyrassa += 1

        pii_likiarvo = 4 * ympyrassa / N
        print(f"Piin likiarvo {N} pisteellä on noin {pii_likiarvo}")
except ValueError:
    print("Syötä kelvollinen kokonaisluku.")
