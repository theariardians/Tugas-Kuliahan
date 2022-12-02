from tkinter import *

window = Tk()

Label1 = Label(window, text = "NIM")
Label2 = Label(window, text = "Nama")
Label3 = Label(window, text = "Kehadiran")
Label4 = Label(window, text = "Tugas")
Label5 = Label(window, text = "UTS")
Label6 = Label(window, text = "UAS")

tombol1 = Button(window, text = "Save")

nm = Entry(window)
nma = Entry(window)
kn = Entry(window)
tg = Entry(window)
ut = Entry(window)
ua = Entry(window)

Label1.grid()
nm.grid()
Label2.grid()
nma.grid()
Label3.grid()
kn.grid()
Label4.grid()
tg.grid()
Label5.grid()
ut.grid()
Label6.grid()
ua.grid()
tombol1.grid()

window.mainloop()