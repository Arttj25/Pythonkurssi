while True:
    try:
        tuumat = float(input("Anna tuumat (negatiivinen lopettaa):"))

        if tuumat < 0:
            print("Ohjelma lopetetaan.")
            break

        senttimetrit = tuumat * 2.54
        print(f"{tuumat} tuumaa on {senttimetrit:.2f} cm")

    except ValueError:
        print("Syötä kelvollinen luku.")