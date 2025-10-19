from operator import truediv

luvut = []

while True:


    luku = input( "Anna luku (tyhjä lopettaa):")
    if luku == "":
        break
    luvut.append(float(luku))

luvut.sort(reverse=True)

print("Viisi suurinta lukua suuruusjärjestyksessä:")
for luku in luvut[:5]:
    print(luku)



