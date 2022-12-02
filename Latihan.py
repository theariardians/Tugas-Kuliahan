from tkinter import *
window = Tk()
window.title("Perhitungan Kelulusan Mahasiswa") 
window.geometry('350x200')

lbl = Label(window, text="NIM : ",anchor="e",width=20)
lbl.grid(column=0, row=0)

nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=0)

lbl2 = Label(window, text="NAMA : ",anchor="e",width=20)
lbl2.grid(column=0, row=1)

nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=1)

lbl3 = Label(window, text="KEHADIRAN : ",anchor="e",width=20)
lbl3.grid(column=0, row=2)

nilai3 = Entry(window,width=10)
nilai3.grid(column=1, row=2)

lbl4 = Label(window, text="TUGAS : ",anchor="e",width=20)
lbl4.grid(column=0, row=3)

nilai4 = Entry(window,width=10)
nilai4.grid(column=1, row=3)

lbl5 = Label(window, text="UTS : ",anchor="e",width=20)
lbl5.grid(column=0, row=4)

nilai5 = Entry(window,width=10)
nilai5.grid(column=1, row=4)

lbl6 = Label(window, text="UAS : ",anchor="e",width=20)
lbl6.grid(column=0, row=5)

nilai6 = Entry(window,width=10)
nilai6.grid(column=1, row=5)

lbl7 = Label(window, text="JUMLAH: ",anchor="e",width=20)
lbl7.grid(column=0, row=6)

nilai7 = Label(window, text=" ", anchor="w", width=10)
nilai7.grid(column=1, row=6)

lbl8 = Label(window, text="RATA-RATA: ",anchor="e",width=20)
lbl8.grid(column=0, row=7)

nilai8 = Label(window, text=" ", anchor="w", width=10)
nilai8.grid(column=1, row=7)

lbl9 = Label(window, text="GRADE: ",anchor="e",width=20)
lbl9.grid(column=0, row=8)

nilai9 = Label(window, text=" ", anchor="w", width=10)
nilai9.grid(column=1, row=8)

lbl10 = Label(window, text="KETERANGAN: ",anchor="e",width=20)
lbl10.grid(column=0, row=9)

nilai9 = Label(window, text=" ", anchor="w", width=10)
nilai9.grid(column=1, row=9)



def tambah():
    nilai7.configure(text=(int(nilai3.get())+int(nilai4.get())+int(nilai5.get())+int(nilai6.get())))


btn = Button(window, text="Proses", command=tambah)
btn.grid(column=0, row=10)
window.mainloop()