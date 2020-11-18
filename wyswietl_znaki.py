import numpy as np
import przygotuj_wejscie


def wyswietl_znaki():

    error = 0
    Ek = przygotuj_wejscie.przygotuj_wejscie("src/img/training_vector.png", 86)


    def aktywacja(x):
        """Funkcje pomocniczne , pomagaja w czytelnosci kodu"""
        return 1 / (1 + np.exp(-x))

    def pochodna(x):
        """Funkcje pomocniczne , pomagaja w czytelnosci kodu"""
        return aktywacja(x) * (1 - aktywacja(x))



    """Losowanie wag zarowno po stronie hidden jak i output"""
    hWeight = np.random.rand(49, 41)
    oWeight = np.random.rand(41, 26)
        #
        # """Przeliczanie wartosci kazdego noda wedlug wzoru:
        #     xInput = (Ek[0] * xWeight[0]) + (Ek[1] * xWeight[1])....
        #     xOutput = 1 / (1 + e^[-xInput])
        #     """
        # hInput = np.dot(Ek, hWeight)
        # hOutput = aktywacja(hInput)
        #
        # oInput = np.dot(hOutput, oWeight)
        # oOutput = aktywacja(oInput)
        #
        # """Algorytm Wstecznej Propagacji Błędu"""""
        # """Przeliczanie MSE (Mean Squared Error) wedlug wzoru:
        #     MSE = sum([1/n] * [wartosc_otrzymana - wektor_trenujacy]^2)
        #     n=49 (wejscia)
        # """
        # error = ((1 / 49) * (np.power((oOutput - Ck), 2)))
        # print(error.sum())
        #
        # """Ograniczenie precyzji do 0.001"""
        # if error.sum() < 0.001:
        #     print("Algorytm wyuczony!")
        #     zapis_do_pliku(hWeight, oWeight, error.sum())
        #     a = 1 + 3
        #     print(a)
        #     return 0

    return 0


wyswietl_znaki()
