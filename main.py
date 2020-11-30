from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar

from PIL import ImageTk, Image
import os

training_vector_path = "src/img/training_vector.png"
training_vector_path_filename = "training_vector.png"
input_vector_path = "src/img/example_2.png"
input_vector_path_filename = "example_2.png"


frame = Tk()
frame.title("ZSI - Arkadiusz Wieruchowski")
frame.geometry('450x380')


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

def trenuj_siec(event):
    return 0

# TOP---------------------------------------------------------------------------------------
top_frame = Frame(frame, width=200, height=200,)
top_frame.grid(row=0, sticky="w")

lbl_wTrenujacy = Label(top_frame,  text="Wektor Trenujacy")
lbl_wTrenujacy.grid(row=0, columnspan=2)

lbl_wTrenujacy_filename = Label(top_frame, text=training_vector_path_filename)
lbl_wTrenujacy_filename.grid(row=1, columnspan=2)

wTrenujacy_path = ImageTk.PhotoImage(Image.open(training_vector_path))
wTrenujacy_img = Label(top_frame, image=wTrenujacy_path, width=200, height=100, text="sunken & borderwidth=3", background='white',
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
wWejscie_img = Label(top_frame, image=wWejscie_path, width=200, height=100, text="sunken & borderwidth=3",background='white',
                       relief="groove")
wWejscie_img.grid(row=2, column=2, padx=(10, 10))

zmien_wejscie = Button(top_frame, text="Zmień Wejście")
zmien_wejscie.bind('<Button-1>', find_path_wejscie)
zmien_wejscie.grid(column=2, row=3, pady=5)

#MID--------------------------------------------------------------------------------
mid_frame_left = Frame(frame, width=150, height=200, pady=3)
mid_frame_left.grid(row=1, column=0, sticky="w", padx=(20,10))

lbl_stanSieci = Label(mid_frame_left, text="STAN : WYTRENOWANA")
lbl_stanSieci.grid(column=0, row=0 , sticky="w")

lbl_wektor = Label(mid_frame_left, text="WEKTOR: training_vector.png")
lbl_wektor.grid(column=0, row=1, sticky="w")

lbl_skutecznosc = Label(mid_frame_left, text="SKUTECZNOŚĆ: 97%")
lbl_skutecznosc.grid(column=0, row=3, sticky="w")

lbl_iteracje = Label(mid_frame_left, text="Iteracje: ")
lbl_iteracje.grid(column=0, row=4, sticky="E", pady=10)

iteracje = Entry(mid_frame_left, bd =5)
iteracje.grid(row=4, column=1)

trenuj = Button(mid_frame_left, text="TRENUJ")
trenuj.bind('<Button-1>', trenuj_siec)
trenuj.grid(column=1, row=5,)

rzuc_na_siec = Button(mid_frame_left, text="Rzuć na sieć")
rzuc_na_siec.bind('<Button-1>', find_path_wejscie)
rzuc_na_siec.grid(column=2, row=1)

progresss = Frame(frame, width=200, height=200,)
progresss.grid(column=0, row=3, pady=20)

progress = Progressbar(progresss, orient = HORIZONTAL,
            length = 350, mode = 'indeterminate')
progress.grid(column=1, row=1)

progress_status = Label(progresss, text="Status: ")
progress_status.grid(row=1, column=0,)


frame.mainloop()

