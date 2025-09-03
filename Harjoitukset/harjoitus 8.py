nimi = input("Kerro nimesi?").lower

if nimi != "matti":
    annokset = int(input("montako keittoannosta?"))
    print("kokonaishinta on" , annokset * 5.9)
    print("seuraava kiitos!")

else:
   print("seuraava kiitos!")

