from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image
import os

training_vector_path = "src/img/training_vector.png"
training_vector_path_filename = "training_vector.png"
input_vector_path = "src/img/example_2.png"
input_vector_path_filename = "example_2.png"


frame = Tk()
frame.title("ZSI - Arkadiusz Wieruchowski")
frame.geometry('600x600')


def find_path_training(event):
    global training_vector_path
    global training_vector_path_filename

    training_vector_path = filedialog.askopenfilename(filetypes=[("Pliki Graficzne", "*.png")])
    img = ImageTk.PhotoImage(Image.open(training_vector_path))
    wTrenujacy_img.configure(image=img)
    wTrenujacy_img.image = img

    training_vector_path_filename = os.path.basename(training_vector_path)
    lbl_wTrenujacy_filename.configure(text=training_vector_path_filename)
    return training_vector_path

def find_path_wejscie(event):
    global input_vector_path
    global input_vector_path_filename

    input_vector_path = filedialog.askopenfilename(filetypes=[("Pliki Graficzne", "*.png")])
    img = ImageTk.PhotoImage(Image.open(input_vector_path))
    wWejscie_img.configure(image=img)
    wWejscie_img.image = img

    input_vector_path_filename = os.path.basename(input_vector_path)
    lbl_wWejscie_filename.configure(text=input_vector_path_filename)
    return input_vector_path

# TOP---------------------------------------------------------------------------------------
top_frame = Frame(frame, width=400, height=300, pady=3)
top_frame.grid(row=0, sticky="w")

lbl_wTrenujacy = Label(top_frame, text="Wektor Trenujacy")
lbl_wTrenujacy.grid(row=0, columnspan=2)

lbl_wTrenujacy_filename = Label(top_frame, text=training_vector_path_filename)
lbl_wTrenujacy_filename.grid(row=1, columnspan=2)

wTrenujacy_path = ImageTk.PhotoImage(Image.open(training_vector_path))
wTrenujacy_img = Label(top_frame, image=wTrenujacy_path, width=200, height=100, text="sunken & borderwidth=3",
                       relief="groove")
wTrenujacy_img.grid(row=2, column=1, padx=(10, 10))

zmien_wektor = Button(top_frame, text="Zmień Wektor")
zmien_wektor.bind('<Button-1>', find_path_training)
zmien_wektor.grid(column=1, row=3, pady=5)

#==============================

lbl_wWejscie = Label(top_frame, text="Wejście sieci")
lbl_wWejscie.grid(column=2, row=0)

lbl_wWejscie_filename = Label(top_frame, text=input_vector_path_filename)
lbl_wWejscie_filename.grid(row=1, column=2)

wWejscie_path = ImageTk.PhotoImage(Image.open(input_vector_path))
wWejscie_img = Label(top_frame, image=wWejscie_path, width=200, height=100, text="sunken & borderwidth=3",
                       relief="groove")
wWejscie_img.grid(row=2, column=2, padx=(10, 10))

zmien_wejscie = Button(top_frame, text="Zmień Wejście")
zmien_wejscie.bind('<Button-1>', find_path_wejscie)
zmien_wejscie.grid(column=2, row=3, pady=5)

frame.mainloop()
