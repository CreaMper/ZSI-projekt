import time
from tkinter import Tk, Label, HORIZONTAL, messagebox
from tkinter.ttk import Progressbar

import numpy as np
import wektorTrenujacy


def przepuscPrzezSiec(iteracje, wektor):
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
    Ek = wektorTrenujacy.wyznaczWektorTrenujacy(wektor, 86)
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

    # ----------------------------WYŚWIETLANIE
    learning = Tk()
    learning.title("ZSI - Arkadiusz Wieruchowski - Trenowanie!")
    learning.geometry('530x70')


    lbl_iteracja = Label(learning, text="Iteracja:", width=10)
    lbl_iteracja.grid(row=1, column=0)
    lbl_iteracja_num = Label(learning, text="0", width=10)
    lbl_iteracja_num.grid(row=1, column=1, sticky="w")

    lbl_aktualnyBlad = Label(learning, text="Suma błędu:", width=10)
    lbl_aktualnyBlad.grid(row=0, column=0)
    lbl_aktualnyBlad_num = Label(learning, text="0", width=10)
    lbl_aktualnyBlad_num.grid(row=0, column=1, sticky="w")

    lbl_acc = Label(learning, text="Skuteczność:", width=10)
    lbl_acc.grid(row=2, column=0)
    lbl_acc_num = Label(learning, text="0", width=10)
    lbl_acc_num.grid(row=2, column=1, sticky="w")

    progress = Progressbar(learning, orient=HORIZONTAL,
                           length=350, mode='determinate', )
    progress.grid(column=3, row=1)

    avg = 0
    sign_error = 0
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

        """Ograniczenie precyzji do 0.0001"""
        if error.sum() < 0.0001:
            print("Algorytm wyuczony!")
            #zapisz_wagi(hWeight, oWeight, 0.001)
            zapis_do_pliku(hWeight, oWeight, error.sum())
            y = messagebox.showinfo(title="Trenowanie sieci zakończone!", message="Program już więcej się nie nauczy! skutecznosć - "+wyswietl)
            if y:
                learning.destroy()
            return wyswietl2*100

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
        if (iteracja % 1000 == 0):
            lbl_aktualnyBlad_num.configure(text=round(error.sum(), 4))
            lbl_iteracja_num.configure(text=iteracja)
            progress['value'] = round(((iteracja/iteracje)*100),1)
            for i in range(len(oOutput)):
                for j in range(len(oOutput)):
                    sign_error = sign_error + abs(Ck[i][j] - oOutput[i][j])
                    wyswietl = str(round(abs(sign_error / len(oOutput) - 1),4))
                    wyswietl2 = round(abs(sign_error / len(oOutput) - 1),4)
                lbl_acc_num.configure(text=wyswietl)
                learning.update()
                sign_error = 0


    progress['value'] = 100
    lbl_iteracja_num.configure(text=iteracje)
    learning.update()
    zapis_do_pliku(hWeight, oWeight, error.sum())
    y = messagebox.showinfo(title="Trenowanie sieci zakończone!",
                        message="Program przeszedł przez wszystkie "+str(iteracje)+ " iteracji.  Skutecznosć:  " + str(round(wyswietl2,3)*100) + "%")
    if y:
        learning.destroy()

    return wyswietl2*100
