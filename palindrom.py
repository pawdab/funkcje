def palindrom(word):
    """
    Checks if word is palindorme
    """

    lenght = len(word)
    if lenght == 0:
        print("Brak słowa")
        return
    for i in range(0,round(lenght / 2)):
        if word[i] != word[lenght - i - 1]:
            return False
        i = i + 1
    return True



print(palindrom("potop"))


help(palindrom)