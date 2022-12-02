from tkinter import *
from tkinter import messagebox


window = Tk()
window.config(background="white")
window.title("KASIR ARI ARDIANS")
window.resizable(FALSE,FALSE)
window.geometry("450x450")


#MENU
lbl1 = Label(window, text="ARI ARDIANS CAFE", fg="black", bg="white")
lbl1.grid(column=1, columnspan=5)
lbl20 = Label(window, text="Jl. KH. Ahmad Dahlan N.77 Rangkui, Pangkal Pinang City", fg="black", bg="white")
lbl20.grid(column=1, columnspan=5)
lbl2 = Label(window, text="Kode Menu :", anchor="w", width=20, bg="white")
lbl2.grid(row=3, column=2)
lbl3 = Label(window, text="01. Milo 10K", anchor="w", width=20, bg="white",)
lbl3.grid(row=4, column=2)
lbl4 = Label(window, text="02. Chocolate coffee 15K", anchor="w", width=20, bg="white")
lbl4.grid(row=5, column=2)
lbl5 =Label(window, text="03. Caramel Latte 12K", anchor="w", width=20, bg="white")
lbl5.grid(row=6, column=2) 
lbl6 = Label(window, text="04. Espresso 15K", anchor="w", width=20, bg="white")
lbl6.grid(row=4, column=3)
lbl7 = Label(window, text="05. Red Velvet 10K", anchor="w", width=20, bg="white")
lbl7.grid(row=5, column=3)
lbl8 = Label(window, text="06. Vanilla Latte 13K", anchor="w", width=20, bg="white")
lbl8.grid(row=6, column=3)
lbl9 = Label(window, text="07. Brownies Keju 15K", anchor="w", width=20, bg="white")
lbl9.grid(row=4, column=4)
lbl10 = Label(window, text="08. Brownies Coklat 12K", anchor="w", width=20, bg="white")
lbl10.grid(row=5, column=4)
lbl11 = Label(window, text="09. Dessert Box Coklat 18K", anchor="w", width=20, bg="white")
lbl11.grid(row=6, column=4)


#PESANAN
lbl12 = Label(window, text="Pesanan :", anchor="w", width=20, bg="white")
lbl12.grid(row=7, column=2)
lbl13 = Label(window, text="Kode Menu", anchor="w", width=20, bg="white")
lbl13.grid(row=8, column=2)
lbl14 = Label(window, text="Jumlah Pesan", anchor="w", width=20, bg="white")
lbl14.grid(row=9, column=2)
ent1 = Entry(window, width=20, bg="white")
ent1.grid(row=8, column=3)
ent2 = Entry(window, width=20, bg="white")
ent2.grid(row=9, column=3)
ent3 = Entry(window, width=20, bg="white")
ent3.grid(row=11, column=3)
ent4 = Entry(window, width=20, bg="white")
ent4.grid(row=13, column=3)
lbl15 = Label(window, text="Total", anchor="w", width=20, bg="white")
lbl15.grid(row=10, column=2)
total = Entry(window, width=20, bg="white")
total.grid(row=10, column=3)
lbl16 = Label(window, text="Masukan Uang", anchor="w", width=20, bg="white")
lbl16.grid(row=11, column=2)
lbl19 = Label(window, text="Masukan Kembalian", width=20, bg="white")
lbl19.grid(row=13, column=2)


#FUCTION
def total_harga():
    a = int(ent1.get())
    b = int(ent2.get())
    
    if a == 1:
        hrga = int(10000)
    elif a == 2:
        hrga = int(15000)
    elif a == 3:
        hrga = int(12000)
    elif a == 4:
        hrga = int(15000)
    elif a == 5:
        hrga = int(10000)
    elif a == 6:
        hrga = int(13000)
    elif a == 7:
        hrga = int(15000)
    elif a == 8:
        hrga = int(12000)
    elif a == 9:
        hrga = int(18000)
    c = hrga * b
    total.insert(0, c)
    second_number = c
    if math == 'tambah':
        total.delete(0, END)
        total.insert(0, f_num + second_number)

def kmbl():
    a = int(ent3.get())
    b = int(total.get())
    global tip
    tip = str(a-b)
    if a == b:
        messagebox.showinfo("ARI ARDIANS CAFE","TERIMA KASIH TELAH BERBELANJA \nUANG ANDA PAS \nTRANSAKSI SELESAI")
    elif a <b:
        messagebox.showinfo("ARI ARDIANS CAFE","MOHON MAAF UANG ANDA KURANG")
    else:
        messagebox.showinfo("ARI ARDIANS CAFE", "KEMBALIAN :"+tip)

def nambah():
    a = int(ent1.get())
    b = int(ent2.get())
    if a == 1:
        hrga = int(10000)
    elif a == 2:
        hrga = int(15000)
    elif a == 3:
        hrga = int(12000)
    elif a == 4:
        hrga = int(15000)
    elif a == 5:
        hrga = int(10000)
    elif a == 6:
        hrga = int(13000)
    elif a == 7:
        hrga = int(15000)
    elif a == 8:
        hrga = int(12000)
    elif a == 9:
        hrga = int(18000)
    c = hrga*b
    first_number = c
    global f_num
    global math
    math = 'tambah'
    f_num = int(first_number)
    ent1.delete(0, END)
    ent2.delete(0, END)

def tambah():
    first_number = ent4.get()
    global f_num
    global math
    math = 'tambah'
    f_num = int(first_number)
    ent4.delete(0, END)

def samdeng():
    second_number = ent4.get()
    ent4.delete(0, END)

    if math == 'tambah':
            ent4.insert(0, f_num + int(second_number))


def selesai():  
    a = str(ent4.get())
    if a == tip:
        messagebox.showinfo("ARI ARDIANS CAFE","TRANSAKSI TELAH SELESAI \nTERIMA KASIH TELAH BERBELANJA")
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        total.delete(0, END)
    elif a >tip:
        messagebox.showinfo("ARI ARDIANS CAFE","KEMBALIAN LEBIH \nSAYA IKHLASKAN")
    else:
        messagebox.showinfo("ARI ARDIANS CAFE","KEMBALIAN SALAH \nHARAP MASUKAN ULANG")
        ent4.delete(0, END)

def list():
    ent4.insert(0, list1.get(ANCHOR))

#LIST
list1 = Listbox(window, height=8, bg="white")
list1.grid(row=14, column=3)
list1_isi = ["500", "1000", "2000", "5000", "10000", "20000", "50000", "100000"]
for isi in list1_isi:
    list1.insert(END, isi)

#tombol
btn1 = Button(window, text="TAMBAH", width=20, command=nambah ,bg="white")
btn1.grid(row=12, column=2)
btn2 = Button(window, text="CEK TOTAL", width=20, command=total_harga, bg="white")
btn2.grid(row=12, column=3)
btn3 = Button(window, text="CEK KEMBALIAN", width=20, command=kmbl, bg="white")
btn3.grid(row=12, column=4)
btn4 = Button(window, text="SELESAI", width=20, command=selesai, bg="white")
btn4.grid(row=13, column=4)
btn5 = Button(window, text="PILIH", width=20, command=list, bg="white")
btn5.grid(row=15, column=3)
btn12 = Button(window, text="=", width=20, command=samdeng,bg="white")
btn12.grid(row=15, column=4)
btn13 = Button(window, text="+", width=20, command=tambah,bg="white")
btn13.grid(row=15, column=2)


window.mainloop()