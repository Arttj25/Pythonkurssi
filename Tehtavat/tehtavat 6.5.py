def poista_parittomat(luku):
    parilliset = (luku for luku in luku if luku % 2 == 0 )
    return (parilliset)

def main():
    luvut = (1,3,5,7,8,9)

    poistetut_luvut = poista_parittomat(luvut)

    print("Alkuperäinen lista:",luvut)
    print("Parillisten lukujen lista:", poistetut_luvut)

if __name__ == "__main__":
    main()
