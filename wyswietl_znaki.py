import numpy as np

import odczytaj_wagi
import przygotuj_wejscie


def wyswietl_znaki():
    global oOutput
    error = 0
    Ek = przygotuj_wejscie.przygotuj_wejscie("src/img/example_2.png", 86)
    slownik = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def aktywacja(x):
        """Funkcje pomocniczne , pomagaja w czytelnosci kodu"""
        return 1 / (1 + np.exp(-x))

    def pochodna(x):
        """Funkcje pomocniczne , pomagaja w czytelnosci kodu"""
        return aktywacja(x) * (1 - aktywacja(x))

    """Losowanie wag zarowno po stronie hidden jak i output"""
    hWeight, oWeight = odczytaj_wagi.odczytaj_wagi()

    for i in range(len(Ek)):
        """Przeliczanie wartosci kazdego noda wedlug wzoru:
            xInput = (Ek[0] * xWeight[0]) + (Ek[1] * xWeight[1])....
            xOutput = 1 / (1 + e^[-xInput])
            """
        # hInput = np.dot(Ek[i], hWeight[i])
        hInput = np.dot(Ek, hWeight)
        hOutput = aktywacja(hInput)

        oInput = np.dot(hOutput, oWeight)
        oOutput = aktywacja(oInput)
    max_iter = 0
    max_value = 0
    acc_sum = 0

    """Wyświetlanie znaków """
    for i in range(len(oOutput)):
        for j in range(len(oOutput[i])):
            oOutput[i, j] = np.round(oOutput[i, j], 5)
            if max_value < oOutput[i, j]:
                max_value = oOutput[i, j]
                max_iter = j
                acc_sum = acc_sum + max_value
        print(slownik[max_iter], end=" ")
        max_value = 0
        max_iter = 0
    print(round(acc_sum / len(Ek), 5))

    return 0


wyswietl_znaki()
