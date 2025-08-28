luoti_grammoina = 13.3
naulaa_leiviskassa = 20
luoteja_naulassa = 20

leiviska = float(input("Anna Leiviskat"))
naula = float(input("Anna naulat"))
luodit = float(input("Anna luodit"))

kokonaisgrammat = 909 * luoti_grammoina
kilot = int(kokonaisgrammat // 1000)
grammat = kokonaisgrammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {grammat :.2f} grammaa")