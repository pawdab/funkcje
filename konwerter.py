def konwertuj(text, typ):
    liczba = input(text)
    check = False
    while check == False:
        try:
            liczba = typ(liczba)
            check = True
        except:
            liczba = (input("Błąd wprowadzenia." + text))
    return liczba

liczba = konwertuj("Podaj liczbe", float)
print(type(liczba))

