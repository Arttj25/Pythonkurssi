def gallonat_litroiksi(gallonat):
    return gallonat*3.785

def main():
    while True:
        gallonat = float(input("Anna bensan määrä gallonissa: "))

        if gallonat <0:
            print("ohjelma päättyy")
            break


        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat:.2f} gallonaa on {litrat:.2f} litraa.")

if __name__ == '__main__':
    main()