from tkinter import *


window = Tk()


def Kg_to_Other_units():
    grams = float(e1_val.get()) * 1000
    pounds = float(e1_val.get()) * 2.20462
    ounces = float(e1_val.get()) * 35.274
    t1_grams.delete("1.0", END)
    t1_grams.insert(END, str(grams) +" grams")
    t1_pounds.delete("1.0", END)
    t1_pounds.insert(END, str(pounds) + " pounds")
    t1_ounces.delete("1.0", END)
    t1_ounces.insert(END, str(ounces) + " ounces")

e1 = Label(window, text = "Kg")
e1.grid ( row =0, column =0)

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.grid(row =0, column =1)

b1 = Button(window, text = "convert", command = Kg_to_Other_units)
b1.grid(row = 0, column = 2)

t1_grams = Text(window, height = 1, width = 20)
t1_grams.grid(row = 1, column= 0)

t1_pounds = Text(window, height = 1, width = 20)
t1_pounds.grid(row = 1, column= 1)

t1_ounces = Text(window, height = 1, width = 20)
t1_ounces.grid(row = 1, column= 2)


window.mainloop()
