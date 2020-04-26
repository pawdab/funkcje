import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile_kalkulator.log")

def mnoz_liste(lista) : 
    wynik = 1
    for liczba in lista:
        wynik = wynik * liczba
    return wynik


def kalkulator(dzialanie, liczba1, liczba2):
    wynik = [None, None, None]
    liczby = [liczba1, liczba2]
    #dzialanie = int(dzialanie)
    #liczba1 = float(liczba1)
    #liczba2 = float(liczba2)
    if dzialanie == 1:
        wynik[1] = "Dodaje"
        odpowiedz = input("czy checsz dodać kolejną liczbe? [T/N]: ")
        while odpowiedz != "N":
            liczby.append(float(input("podaj kolejna")))
            odpowiedz = input("czy checsz dodać kolejną liczbe? [T/N]: ")
        wynik[0] = sum(liczby)          
    elif dzialanie == 2:
        wynik[0] = liczba1 - liczba2
        wynik[1] = "Odejmuje"
    elif dzialanie == 3:
        wynik[1] = "Mnoże"
        odpowiedz = input("czy checsz domnożyc kolejną liczbe? [T/N]: ")
        while odpowiedz != "N":
            liczby.append(float(input("podaj kolejna")))
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
        dzialanie = (input("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie"))
        liczba1 = (input("podaj liczbe1: "))
        liczba2 = (input("podaj liczbe2: "))
    else:
        dzialanie = (sys.argv[1])
        liczba1 = (sys.argv[2])
        liczba2 = (sys.argv[3])
else:
    dzialanie = (input("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie"))
    liczba1 = (input("podaj liczbe1: "))
    liczba2 = (input("podaj liczbe2: "))


check = False
while check == False:
    if dzialanie.isnumeric() == True:
        dzialanie = int(dzialanie)
        check = True
    else:
        dzialanie = (input("Podano zły kod działania. Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie"))

check = False
while check == False:
    if liczba1.isnumeric() == True:
        liczba1 = float(liczba1)
        check = True
    else:
        liczba1 = (input("Podano text zamiast Liczba1. Podaj Liczba1: "))

check = False
while check == False:
    if liczba2.isnumeric() == True:
        liczba2 = float(liczba2)
        check = True
    else:
        liczba2 = (input("Podano text zamiast Liczba2. Podaj Liczba2: "))



wynik = kalkulator(dzialanie, liczba1, liczba2)
logging.debug("Program został uruchomiony z następującymi parametrami: %s" % sys.argv[1:])
logging.debug("%s liczby %s oraz %s" % (wynik[1], liczba1, liczba2))

print(f"{wynik[1]} liczby {wynik[2]} co daje {wynik[0]}")

