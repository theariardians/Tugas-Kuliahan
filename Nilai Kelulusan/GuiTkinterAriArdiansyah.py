from tkinter import *
from tkinter import messagebox
import re
from typing import ContextManager, Pattern

window = Tk()
window.resizable(FALSE,FALSE)
window.title("Nilai Kelulusan Mahasiswa")
window.geometry("290x380")
window.config(background="white")


lbl1 = Label(window, text="Nama", bg="white",  fg="black", anchor="e", width=20) 
lbl1.grid(row=1, column=1)
lbl2 = Label(window, text="NIM", bg="white", fg="black",anchor="e", width=20) 
lbl2.grid(row=2, column=1)
lbl3 = Label(window, text="Kehadiran", bg="white", fg="black",anchor="e", width=20) .grid(row=3, column=1)
lbl4 = Label(window, text="Nilai Tugas", bg="white", fg="black",anchor="e", width=20) .grid(row=4, column=1)
lbl5 = Label(window, text="Nilai UTS", bg="white", fg="black",anchor="e", width=20) .grid(row=5, column=1)
lbl6 = Label(window, text="Nilai UAS", bg="white", fg="black",anchor="e", width=20) .grid(row=6, column=1)
lbl7 = Label(window, text="HASIL", bg="white", fg="black", anchor="e", width=20 )
lbl7.grid(row=11, column=1, columnspan=2)
lbl8 = Label(window, text="NAMA :", bg="white", fg="black", anchor="e", width=20)
lbl8.grid(row=12, column=1)
lbl9 = Label(window, text="NIM :", bg="white", fg="black", anchor="e", width=20)
lbl9.grid(row=13, column=1)
lbl10 = Label(window, text="JUMLAH NILAI :", bg="white", fg="black", anchor="e", width=20)
lbl10.grid(row=14, column=1)
lbl11 = Label(window, text="RATA-RATA :", bg="white", fg="black", anchor="e", width=20)
lbl11.grid(row=15, column=1)
lbl12 = Label(window, text="GRADE :", bg="white", fg="black", anchor="e", width=20)
lbl12.grid(row=16, column=1)
lbl13 = Label(window, text="KETERANGAN :", bg="white", fg="black", anchor="e", width=20)
lbl13.grid(row=17, column=1)

nama = Label(window, text=" ", width=20, bg="white", fg="black")
nama.grid(row=12, column=2)
nim = Label(window, text=" ", width=20, bg="white", fg="black")
nim.grid(row=13, column=2)
jumlah = Label(window, text="0", width=20,  bg="white", fg="black")
jumlah.grid(row=14, column=2)
rata = Label(window, text="0", width=20, bg="white", fg="black")
rata.grid(row=15, column=2)
grade = Label(window, text="0", width=20, bg="white", fg="black")
grade.grid(row=16, column=2)
keterangan = Label(window, text="0", width=20, bg="white", fg="black")
keterangan.grid(row=17, column=2)

nilai1 = Entry(window, width=20) 
nilai1.grid(row=1, column=2)
nilai2 = Entry(window, width=20) 
nilai2.grid(row=2, column=2)
nilai3= Entry(window, width=20)
nilai3.grid(row=3, column=2)
nilai4 = Entry(window, width=20) 
nilai4.grid(row=4, column=2)
nilai5 = Entry(window, width=20) 
nilai5.grid(row=5, column=2)
nilai6 = Entry(window, width=20) 
nilai6.grid(row=6, column=2)


def Lihat_hasil():
    a = int(nilai3.get())
    b = int(nilai4.get())
    c = int(nilai5.get())
    d = int(nilai6.get())
    absen = (a / 16 * 100)
    jumlah.configure(text=(absen + b + c + d))
    jmlh = (0.1*absen + 0.2*b + 0.3*c + 0.4*d)
    rata.configure(text=(jmlh))
    if (jmlh >= 0) and (jmlh <30):
       grade.configure(text=("E"))
       keterangan.configure(text=("TIDAK LULUS"))
    elif (jmlh >= 30) and (jmlh <50):
       grade.configure(text=("D"))
       keterangan.configure(text=("TIDAK LULUS"))
    elif(jmlh >= 50) and (jmlh <70):
       grade.configure(text=("C"))
       keterangan.configure(text=("TIDAK LULUS"))
    elif(jmlh >= 70) and (jmlh <90):
       grade.configure(text=("B"))
       keterangan.configure(text=("LULUS"))
    elif (jmlh >= 90):
       grade.configure(text=("A"))
       keterangan.configure(text=("LULUS"))
   
    Pattern = "\D[^0123456789]""\D$"
    if (re.search(Pattern, nilai1.get())):
       nama.configure(text=(nilai1.get()))
    else:
       nama.configure(text=("Format Nama Salah"))

    Pattern = re.compile(r'\d\d\d\d\d\d\d\d\d')
    if (re.search(Pattern, nilai2.get())):
       nim.configure(text=(nilai2.get()))
    else:
       nim.configure(text=("Format Nim Salah"))


def hapus():
    nilai1.delete(0, END)
    nilai2.delete(0, END)
    nilai3.delete(0, END)
    nilai4.delete(0, END)
    nilai5.delete(0, END)
    nilai6.delete(0, END)
    
hasil1 = Button(window, text="LIHAT HASIL", height=2, width=38, bd=5, fg="black",  command=Lihat_hasil)
hasil1.grid(row=18, column=1, columnspan=2)
hasil2 = Button(window, text="HAPUS", height=2, width=38, bd=5, fg="black", command=hapus)
hasil2.grid(row=19, column=1, columnspan=2)
window.mainloop()