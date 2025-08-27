pituus = int(input("Anna pituutesi: "))
paino = float(input("Anna painosi: "))

#muuttuja jossa lasku suoritetaan
bmi = paino / (pituus / 100)**2

print("pituus-paino-indeksisi on", bmi)
print(f"pituus-paino-indeksisi on, {bmi:.2f}")

