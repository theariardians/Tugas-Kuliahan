# Untuk mengimport tkinter
from tkinter import *

window = Tk()
Label1 = Label()
root = Tk()

root.title("Kalkulator sederhana")
z = Entry(root, width=15)
z.grid(row=0, column=0, columnspan=4)


def klik(angka):
    # membalik insert
    balik = z.get()
    # menghapus layar sebelumnya
    z.delete(0, END)
    z.insert(0, str(balik) + str(angka))


def tambah():
    first_number = z.get()
    global f_num
    global math
    math = 'tambah'
    f_num = int(first_number)
    z.delete(0, END)


def sama_dengan():
    second_number = z.get()
    z.delete(0, END)

    if math == 'tambah':
        z.insert(0, f_num + int(second_number))

    if math == 'kali':
        z.insert(0, f_num * int(second_number))

    if math == 'bagi':
        z.insert(0, f_num / int(second_number))

    if math == 'kurang':
        z.insert(0, f_num - int(second_number))


def kali():
    first_number = z.get()
    global f_num
    global math
    math = 'kali'
    f_num = int(first_number)
    z.delete(0, END)


def bagi():
    first_number = z.get()
    global f_num
    global math
    math = 'bagi'
    f_num = int(first_number)
    z.delete(0, END)


def kurang():
    first_number = z.get()
    global f_num
    global math
    math = 'kurang'
    f_num = int(first_number)
    z.delete(0, END)


def hapus():
    # menghapus layar
    z.delete(0, END)


a_1 = Button(root, text="1", width=5, command=lambda: klik(1)).grid(row=3, column=1)
a_2 = Button(root, text="2", width=5, command=lambda: klik(2)).grid(row=3, column=2)
a_3 = Button(root, text="3", width=5, command=lambda: klik(3)).grid(row=3, column=3)

a_4 = Button(root, text="4", width=5, command=lambda: klik(4)).grid(row=2, column=1)
a_5 = Button(root, text="5", width=5, command=lambda: klik(5)).grid(row=2, column=2)
a_6 = Button(root, text="6", width=5, command=lambda: klik(6)).grid(row=2, column=3)

a_7 = Button(root, text="7", width=5, command=lambda: klik(7)).grid(row=1, column=1)
a_8 = Button(root, text="8", width=5, command=lambda: klik(8)).grid(row=1, column=2)
a_9 = Button(root, text="9", width=5, command=lambda: klik(9)).grid(row=1, column=3)

a_0 = Button(root, text="0", width=5, command=lambda: klik(0)).grid(row=4, column=1)
a_p = Button(root, text="+", width=5, command=tambah).grid(row=4, column=2)
a_s = Button(root, text="=", width=15, command=sama_dengan).grid(row=6, column=1, columnspan=4)

clear = Button(root, text="AC", command=hapus, width=5).grid(row=5, column=1)
kurang = Button(root, text="-", width=5, command=kurang).grid(row=4, column=3)
bagi = Button(root, text="/", width=5, command=bagi).grid(row=5, column=3)
kali = Button(root, text="x", width=5, command=kali).grid(row=5, column=2)

root.mainloop()
