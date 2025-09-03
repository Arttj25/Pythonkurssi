money = float(input("Kuinka rahaa sinulla on: "))
if money >= 5:
    print("voit ostaa kahvin.")
else:
    print("raha ei riitä kahviin")
print("Kiitos ja hei.")



pituus = int(input("Kuinka pitkä olet?"))

if 170 <= pituus <= 180:
    print("oletpa pitkä!")


koira = input("mikä koiran nimi on?").lower()
kissa = input("mikä kissan nimi on").lower()

if koira == kissa:
    print("oho niillä on sama nimi!")

