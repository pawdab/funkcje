import sys
import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile_kalkulator.log")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

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


def mnoz_liste(lista) : 
    wynik = 1
    for liczba in lista:
        wynik = wynik * liczba
    return wynik


def kalkulator(dzialanie, liczba1, liczba2):
    wynik = [None, None, None]
    liczby = [liczba1, liczba2]
    if dzialanie == 1:
#alternatywą (pewnie trochę lepszą) było by przeniesienie inputu tutaj i zapytanie użyttkownika ile licz chce dodawać [mnożyć] i zapętlić pytanie tyle razy żeby podał te liczby
        wynik[1] = "Dodaje"
        odpowiedz = input("czy checsz dodać kolejną liczbe? [T/N]: ")
        while odpowiedz != "N":
            liczby.append(konwertuj("podaj kolejna ", float))
            odpowiedz = input("czy checsz dodać kolejną liczbe? [T/N]: ")
        wynik[0] = sum(liczby)          
    elif dzialanie == 2:
        wynik[0] = liczba1 - liczba2
        wynik[1] = "Odejmuje"
    elif dzialanie == 3:
        wynik[1] = "Mnoże"
        odpowiedz = input("czy checsz domnożyc kolejną liczbe? [T/N]: ")
        while odpowiedz != "N":
            liczby.append(konwertuj("podaj kolejna ", float))
            odpowiedz = input("czy checsz domnożyc kolejną liczbe? [T/N]: ")
        wynik[0] = mnoz_liste(liczby)          
    elif dzialanie == 4:
        if liczba2 == 0:
            wynik[0] = "Nie dzieli się przez zero"
            wynik[1] = "Chciałem dzielic ale użytkownik podał 0"
        else:
            wynik[0] = liczba1 / liczba2
            wynik[1] = "Dziele"
    else:
        wynik[0] = "Nie ma takiego dzialania"
        wynik[1] = "Inne dzialanie wiec nie wyszło"
    wynik[2] = liczby
    return wynik

if __name__ == "__main__":
    if len(sys.argv) < 4:
        dzialanie = konwertuj("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie", int)
        liczba1 = konwertuj("podaj liczbe1: ", float)
        liczba2 = konwertuj("podaj liczbe2: ", float)
    else:
        try:
            dzialanie = int(sys.argv[1])
        except:
            dzialanie = konwertuj("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie", int)
        try:
            liczba1 = float(sys.argv[2])
        except:
            liczba1 = konwertuj("podaj liczbe1: ", float)
        try:
            liczba2 = float(sys.argv[3])
        except:
            liczba2 = konwertuj("podaj liczbe2: ", float)
else:
    dzialanie = konwertuj("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie", int)
    liczba1 = konwertuj("podaj liczbe1: ", float)
    liczba2 = konwertuj("podaj liczbe2: ", float)



wynik = kalkulator(dzialanie, liczba1, liczba2)
logging.debug("Program został uruchomiony z następującymi parametrami: %s" % sys.argv[1:])
logging.debug("%s liczby %s" % (wynik[1], wynik[2]))

print(f"{wynik[1]} liczby {wynik[2]} co daje {wynik[0]}")

