import numpy as np
import training_vector


def przepuscPrzezSiec(iteracje):
    def zapis_do_pliku(hidden, output, error):
        """Odpowiada za zapis wynikow o pliku"""
        file = open("src/wagi/hidden.txt", "w")
        for i in range(len(hidden)):
            for j in range(len(hidden[0,])):
                file.write(str(hidden[i, j]) + " ")
            if i != (len(hidden) - 1):
                file.write("\n")
        file.close()

        file = open("src/wagi/out.txt", "w")
        for i in range(len(output)):
            for j in range(len(output[0,])):
                file.write(str(output[i, j]) + " ")
            if i != (len(output) - 1):
                file.write("\n")
        file.close()

        file = open("src/wagi/error.txt", "w")
        file.write(str(error.sum()))
        file.close()
        return 0

    """Tworzenie DATA_SET"""
    global error
    error = 0
    Ek = training_vector.wyznaczWektorTrenujacy("src/img/training_vector.png", 86)
    Ck = np.zeros([26, 26])

    """Tworzenie przekatnej z 1. Kazdy kolejny bit danych to oddzielna litera"""
    for i in range(26):
        Ck[i][i] = 1

    def aktywacja(x):
        """Funkcje pomocniczne , pomagaja w czytelnosci kodu"""
        return 1 / (1 + np.exp(-x))

    def pochodna(x):
        """Funkcje pomocniczne , pomagaja w czytelnosci kodu"""
        return aktywacja(x) * (1 - aktywacja(x))



    """Losowanie wag zarowno po stronie hidden jak i output"""
    hWeight = np.random.rand(49, 41)
    oWeight = np.random.rand(41, 26)

    """O ile mają 'skakac' wagi"""
    learning_rate = 0.05

    for iteracja in range(iteracje):
        """Przeliczanie wartosci kazdego noda wedlug wzoru:
            xInput = (Ek[0] * xWeight[0]) + (Ek[1] * xWeight[1])....
            xOutput = 1 / (1 + e^[-xInput])
            """
        hInput = np.dot(Ek, hWeight)
        hOutput = aktywacja(hInput)

        oInput = np.dot(hOutput, oWeight)
        oOutput = aktywacja(oInput)

        """Algorytm Wstecznej Propagacji Błędu"""""
        """Przeliczanie MSE (Mean Squared Error) wedlug wzoru:
            MSE = sum([1/n] * [wartosc_otrzymana - wektor_trenujacy]^2)
            n=49 (wejscia)
        """
        error = ((1 / 49) * (np.power((oOutput - Ck), 2)))
        print(error.sum())

        """Ograniczenie precyzji do 0.001"""
        if error.sum() < 0.001:
            print("Algorytm wyuczony!")
            #zapisz_wagi(hWeight, oWeight, 0.001)
            zapis_do_pliku(hWeight, oWeight, error.sum())
            a = 1 + 3
            print(a)
            return 0

        """Metoda gradientu prostego (Gradient Descent)
            Znalezienie 3 pochodnych w warstwie output i ich podstawienie
        """
        do1 = oOutput - Ck
        do2 = pochodna(oInput)
        do3 = hOutput

        oWynik = np.dot(do3.T, do1 * do2)

        """Znalezienie pomocnicznych pochodnych"""
        dh0 = do1 * do2
        dh4 = oWeight
        dh2 = np.dot(dh0, dh4.T)

        """Znalezienie 3 pochodnych w warstwie hidden i ich podstawienie"""
        dh1 = pochodna(hInput)
        dh3 = Ek
        hWynik = np.dot(dh3.T, dh1 * dh2)

        """Aktualizacja wag"""

        hWeight -= learning_rate * hWynik
        oWeight -= learning_rate * oWynik

    zapis_do_pliku(hWeight, oWeight, error.sum())
    return 0


przepuscPrzezSiec(300000)
