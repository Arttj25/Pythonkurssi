sukupuoli = input("Kerro biologinen sukupuolesi (mies/nainen): ").lower()
hemoglobiini = int(input("Anna hemoglobiini arvosi (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini arvosi on alhainen")
    elif hemoglobiini <= 175:
        print("Hemoglobiini arvosi on normaali")
    else:
        print("Hemoglobiini arvosi on korkea")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini arvosi on alhainen")
    elif hemoglobiini <= 195:
        print("Hemoglobiini arvosi on normaali")
    else:
        print("Hemoglobiini arvosi on korkea")
