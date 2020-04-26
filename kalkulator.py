import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile_kalkulator.log")

def kalkulator(dzialanie, liczba1, liczba2):
    wynik = [None, None]
    #dzialanie = int(dzialanie)
    #liczba1 = float(liczba1)
    #liczba2 = float(liczba2)
    if dzialanie == 1:
        wynik[0] = liczba1 + liczba2
        wynik[1] = "Dodaje"
    elif dzialanie == 2:
        wynik[0] = liczba1 - liczba2
        wynik[1] = "Odejmuje"
    elif dzialanie == 3:
        wynik[1] = "Mnoże"
        wynik[0] = liczba1 * liczba2
        odpowiedz = input("czy checsz domnożyc kolejną liczbe? [T/N]")
        while odpowiedz != "N":
            liczba2 = float(input("podaj kolejna"))
            wynik[0] =wynik[0] * liczba2
            odpowiedz = input("czy checsz domnożyc kolejną liczbe? [T/N]")

            
            
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

while: 
if dzialanie.isnumeric == True:
    dzialanie = int(dzialanie)
else:
    dzialanie = (input("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie"))



wynik = kalkulator(dzialanie, liczba1, liczba2)
logging.debug("Program został uruchomiony z następującymi parametrami: %s" % sys.argv[1:])
logging.debug("%s liczby %s oraz %s" % (wynik[1], liczba1, liczba2))

print(f"{wynik[1]} liczbę {liczba1} oraz {liczba2} co daje {wynik[0]}")

