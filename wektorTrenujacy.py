"""Importy"""
import cv2 as cv
import numpy as np
import pytesseract

"""Ladowanie tesseract'a"""
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def wyznaczWektorTrenujacy(image_path, sensitivity):
    """Funkcja która bedzie znajdywac w podaym obrazku 26 liter angielskiego alfabetu a nastepnie na ich
    podstawie tworzyc wektor trenujacy """
    """Image Pre-Processing , zamiana na GRAY bedzie pomocna przy klasyfikacji pixeli"""
    try:
        img = cv.imread(image_path)
        img = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    except:
        print("Błąd poczas pre-procesingu, sprawdz ściezke/rozszezenie pliku lub jego rozmairy")
        return

    # wyznaczenie rozmiarów image i polozenia poszczegolnych znakow
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    # sprawdzanie czy napewno znaleziono dokladnie 26 znaków
    number_of_signs = int(len(boxes.split()) / 6)
    if number_of_signs != 26:
        print("Error, found more or less than 26 alphabet signs!")
        return

    # zmienne pomocnicze
    vector = np.zeros((26, 49))
    sign_number = 0

    for b in boxes.splitlines():
        """Petla sprawdzajacy array boxes pod kontem znalezionych obiektow"""

        # przypisywanie wartosci arraya nowym zmiennym
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

        # przyciecie obrazka do odpowiednich rozmiarów
        crooped = img[hImg - h:hImg - y, x:w]

        """Sprawdzanie jak zostaly przyciete obrazki, w razie potrzeby dodają białe pola w taki sposób
        aby zawsze było do dyspozycji dokładnie 49 sektorów"""
        if crooped.shape[0] < 35:
            crooped = cv.copyMakeBorder(crooped.copy(), 0, 35 - crooped.shape[0], 0, 0, cv.BORDER_CONSTANT,
                                        value=[255, 255, 255])
        if crooped.shape[1] < 35:
            crooped = cv.copyMakeBorder(crooped.copy(), 0, 0, 0, 35 - crooped.shape[1], cv.BORDER_CONSTANT,
                                        value=[255, 255, 255])

        """Cześć kodu odpowiadajaca za przygotowywanie odpowiednich wektorów
        vector - przechowuje kod binarny naszego segmentu w stringu
        color - przechowuje kod RGB danego pixela
        is_sign - zczytuje ile pixeli w segmencie spełnia nasze wymagania
        """
        is_sign = 0
        for kolumna_sektora in range(0, 7):
            """zmiana sektora po kolumnie po przekroczeniu X=34"""
            for i in range(0, 35):
                """zmiana wierszy """
                for j in range(0, 5):
                    """Pętla zczytująca kolejne piksele z Y"""

                    # Zabezpieczenie przed otrzymaniem kolejny raz tego samego sektora
                    if kolumna_sektora == 1:
                        color = crooped[i, j + 5]
                    elif kolumna_sektora > 1:
                        color = crooped[i, j + (5 * kolumna_sektora)]
                    else:
                        color = crooped[i, j]

                    """ sprawdzenie nie czy nasz pixel odpowiada naszym wymagania (pamietaj ze poruszamy 
                    sie w GRAY RGB) sensitivity ustawiamy na wejsciu 0-255 , im mniejsza tym bardziej dokladna"""
                    if color[0] < sensitivity:
                        is_sign = is_sign + 1
                """sprawdz czy to koniec sektora , oblicz wskaznik
                    sector_number - numer sektoru
                    value - przeliczanie współczynnika ilosci znaku do przestrzeni
                    vector - tablica ktora przechowuje nasze wyniki"""
                if i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 29 or i == 34:
                    sector_number = int((i + 1) / 5) + kolumna_sektora * 7
                    value = round((is_sign / 35), 4)
                    vector[sign_number, sector_number - 1] = value
                    is_sign = 0

        # przechodzenie do nastepnego znaku
        sign_number = sign_number + 1
    print("Frame został przetworzony poprawnie")
    return vector
