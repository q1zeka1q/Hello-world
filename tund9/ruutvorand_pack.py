from tkinter import *
from PIL import Image, ImageTk
def aken():
    aken=Tk()
    f1 = Frame(aken, width=650, height=260)
    f1.pack()

    lbl = Label(f1, text="Ruutvõrrandite lahendamine", font="Calibri 26", fg="green", bg="lightblue")
    lbl.pack(side=TOP)

    lbl_vastus = Label(f1, text="Lahendamine", height=4, width=60, bg="yellow")
    lbl_vastus.pack(side=BOTTOM)

    lbl_a = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
    lbl_a.pack(side=LEFT)

    x2 = Label(f1, text="x^2+", font="Calibri 26", fg="green", padx=10)
    x2.pack(side=LEFT)

    lbl_b = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
    lbl_b.pack(side=LEFT)

    x = Label(f1, text="x+", font="Calibri 26", fg="green", padx=10)
    x.pack(side=LEFT)

    lbl_c = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
    lbl_c.pack(side=LEFT)

    y = Label(f1, text="=0", font="Calibri 26", fg="green", padx=10)
    y.pack(side=LEFT)

    btn_lahenda = Button(f1, text="Lahenda", font="Calibri 26", fg="green")
    btn_lahenda.pack(side=LEFT)

    btn_graafik = Button(f1, text="Graafik", font="Calibri 26", fg="green")
    btn_graafik.pack(side=LEFT)

    aken.mainloop()

aken()
