import numpy as np
import training_vector

print("Rozpoczynanie czytanie wektora...")
inputs = training_vector.wyznaczWektorTrenujacy("src/img/training_vector.png", 86)

iLayer = inputs[0] #input layer
#weightIH = np.zeros([41, 49]) #pierwsza czesc wag 41 nodes with 49 values each
hLayer = np.zeros(41) #hidden layer
#weightHO = np.zeros([26, 41]) #druga czesc wag 26 nodes with 41 values each
oLayer = np.zeros(26) #wartosci wyjsciowe - tyle mamy liter

"""Randomizacja wag"""
weightIH = np.random.uniform(low=0.0, high=1.0, size=(41, 49))
weightHO = np.random.uniform(low=0.0, high=1.0, size=(26, 41))
zh =1
ah_h = np.zeros(41) #przetrzymuje wartosci hidden noda
ah_o = np.zeros(26) #przechowuje wartosci final output node

def aktywacja(x):
    return 1 / (1 + np.exp(-x))


def pochodna_aktywacji(x):
    return aktywacja(x) * (1 - aktywacja(x))


for x in range(1):
    """Feed Forward PART ONE"""
    for i in range(0, 41):
        """przeliczanie kazdego hidden noda"""
        for j in range(0, 48):
            """dodawanie mnozen wag i ich wartosci"""
            zh = zh + (iLayer[j] * weightIH[i][j])
        ah_h[i] = aktywacja(zh)
        zh=0

    """Feed Forward PART TWO"""
    print(ah_h.size)
    hLayer = ah_h
    for i in range(0, 25):
        """przeliczanie kazdego output node"""
        for j in range(0, 41):
            zh = zh + (hLayer[j] * weightHO[i][j])
        ah_o[i] = aktywacja(zh)
        zh=0
    print(ah_o.size)
    print(ah_o)

    """Back Propagation PART ONE """
    #updating weightHO


