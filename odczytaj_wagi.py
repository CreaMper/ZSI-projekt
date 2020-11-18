import numpy as np


def odczytaj_wagi():
    wHidden = []
    file = open("src/wagi/hidden.txt", "r")
    a = 1
    liczba = ""
    while a:
        a = file.read(1)
        liczba = liczba + a
        if a == " ":
            wHidden = np.append(wHidden, float(liczba))
            liczba = ""
    file.close()
    wHidden = np.resize(wHidden, (49, 41))

    wOut = []
    file = open("src/wagi/out.txt", "r")
    a = 1
    liczba = ""
    while a:
        a = file.read(1)
        liczba = liczba + a
        if a == " ":
            wOut = np.append(wOut, float(liczba))
            liczba = ""
    file.close()
    wOut = np.resize(wOut, (41, 26))

    return wHidden, wOut


odczytaj_wagi()
