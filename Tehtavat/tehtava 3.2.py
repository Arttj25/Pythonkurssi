hytti = input("Mika sinun hyttiluokkasi on?").upper()

if hytti == "LUX":
    input(print("LUX on parvekkeellinen hytti."))
elif hytti == "A":
    input(print("A on ikkunallinen hytti autokannen yläpuolella."))
elif hytti == "B":
    input(print("B on ikkunaton hytti autokannen yläpuolella."))
elif hytti == "C":
    input(print("C on ikkunaton hytti autokannen alapuolella."))
else:
    print("Virheellinen hyttiluokka!")
