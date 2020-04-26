import sys
import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile_kalkulator.log")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def convert(text, required_type):
    figure = input(text)
    check = False
    while check == False:
        try:
            figure = required_type(figure)
            check = True
        except:
            figure = (input("Błąd wprowadzenia." + text))
    return figure


def product_list(lista) : 
    result = 1
    for figure in lista:
        result = result * figure
    return result


def calculator(math_operation, figure1, figure2):
    result = {
        "result": None,
        "operation": None,
        "figures": None
    }
    figures = [figure1, figure2]
 # Dodawanie   
    if math_operation == 1:
#alternatywą (pewnie trochę lepszą) było by przeniesienie inputu tutaj i zapytanie użyttkownika ile licz chce dodawać [mnożyć] i zapętlić pytanie tyle razy żeby podał te figures
# wtedy nie trzeba by pytać czy chce kolejną
        result["operation"] = "Dodaje"
        odpowiedz = input("czy checsz dodać kolejną liczbe? [T/N]: ")
        while odpowiedz != "N":
            figures.append(convert("podaj kolejna ", float))
            odpowiedz = input("czy checsz dodać kolejną liczbe? [T/N]: ")
        result["result"] = sum(figures)          
# Odejmowanie
    elif math_operation == 2:
        result["result"] = figure1 - figure2
        result["operation"] = "Odejmuje"
# Mnożenie
    elif math_operation == 3:
        result["operation"] = "Mnoże"
        odpowiedz = input("czy checsz domnożyc kolejną liczbe? [T/N]: ")
        while odpowiedz != "N":
            figures.append(convert("podaj kolejna ", float))
            odpowiedz = input("czy checsz domnożyc kolejną liczbe? [T/N]: ")
        result["result"] = product_list(figures)          
# Dzielenie
    elif math_operation == 4:
        if figure2 == 0:
            result["result"] = "Nie dzieli się przez zero"
            result["operation"] = "Chciałem dzielic ale użytkownik podał 0"
        else:
            result["result"] = figure1 / figure2
            result["operation"] = "Dziele"
# Inne
    else:
        result["result"] = "Nie ma takiego dzialania"
        result["operation"] = "Inne math_operation wiec nie wyszło"
    result["figures"] = figures
    return result

if __name__ == "__main__":
    if len(sys.argv) < 4:
        math_operation = convert("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie", int)
        figure1 = convert("podaj liczbe1: ", float)
        figure2 = convert("podaj liczbe2: ", float)
    else:
        try:
            math_operation = int(sys.argv[1])
        except:
            math_operation = convert("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie", int)
        try:
            figure1 = float(sys.argv[2])
        except:
            figure1 = convert("podaj liczbe1: ", float)
        try:
            figure2 = float(sys.argv[3])
        except:
            figure2 = convert("podaj liczbe2: ", float)
else:
    math_operation = convert("Podaj działanie. 1 - Dodawanie, 2- Odejmowanie, 3 - mnozenie, 4 - dzielenie", int)
    figure1 = convert("podaj liczbe1: ", float)
    figure2 = convert("podaj liczbe2: ", float)



result = calculator(math_operation, figure1, figure2)
logging.debug("Program został uruchomiony z następującymi parametrami: %s" % sys.argv[1:])
logging.debug("%s liczby %s" % (result["operation"], result["figures"]))

print("%s liczby %s co daje %s" % (result["operation"], result["figures"], result["result"]))
#print(f"{result["operation"]} figures {result["figures"]} co daje {result["result"]}")
