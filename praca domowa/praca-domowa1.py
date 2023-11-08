liczba = int(input('Podaj liczbe: ')) #LICZBA

if liczba < 17: #JEZELI LICZBA MNIEJSZA NIZ 17
    wartosc = 1
else: wartosc = 4

if wartosc < 2: #JEZELI PONIZEJ 17
    print("Liczba nie jest parzysta lub nie jest powyzej 17")
else: #TO
    if liczba % 2 == 0: #JEZELI PARZYSTA TO
        print("liczba jest parzysta i jest powyzej 17")
    else: #ALE JESLI NIEPARZYSTA TO
        print("Liczba nie jest parzysta lub nie jest powyzej 17")
        #skonczone 08.11.2023 23;47

