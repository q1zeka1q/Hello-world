from tkinter import *
from tund9Graafilineliides import *
def värvi_valik():
    global tekst
    värv = "white"
    tekst.configure(bg="white")
    if tekst.get() != "":
        tekst.configure(bg="yellow")
        värv = tekst.get()
    else:
        tekst.configure(bg="red")
    return värv

def figuur():
    värv = värvi_valik()
    valik = var.get()
    if valik == 1:
        Liblikas(värv)
    elif valik == 2:
        vaal(värv)
    else:
        Vihmavari()
        print("Joonistan hiljem")

aken = Tk()
aken.geometry("500x500")
aken.title("Graafikud")

pealkiri = Label(aken, text="Erinevad pildid Matplotlib abil", font=("Calibri", 24), fg="green", bg="red", pady=20, width=40)
pealkiri.pack()

tekst = Entry(aken, font=("Calibri", 24), fg="green", bg="red", width=30)
tekst.pack()

nupp = Button(aken, text="Värvi valik", font=("Calibri", 24), command=värvi_valik)
nupp.pack()

var = IntVar()
r1 = Radiobutton(aken, text="Liblikas", font=("Calibri", 18), variable=var, value=1, command=figuur)
r2 = Radiobutton(aken, text="Vaal", font=("Calibri", 18), variable=var, value=2, command=figuur)
r3 = Radiobutton(aken, text="Vihmavari", font=("Calibri", 18), variable=var, value=3, command=figuur)

r1.pack()
r2.pack()
r3.pack()

aken.mainloop()
