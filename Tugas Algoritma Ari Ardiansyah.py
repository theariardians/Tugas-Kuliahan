
#menginput Nama, NIM dan Nilai
import re
from typing import Pattern
Pattern = "[a-zA-Z]" # perintah untuk menentukan input Nama hanya menggunakan huruf besar dan kecil 
nama = input ("Nama : ") 
if (re.search(Pattern, nama)):
   print("Nama Tersedia")
else:
    print("Nama Tidak Tersedia")
Pattern = "[0-9]{9}"  # perintah untuk menentukan input NIM dengan ketentuan validasi panjangnnya 9 dan hanya angka
nim = input ("NIM : ")
if (re.search(Pattern, nim)):
   print("NIM Tersedia")
else:
    print("NIM Tidak Tersedia")
kehadiran=float(input("Masukan Nilai KEHADIRAN : ")) #perintah untuk input nilai kehadiran
tugas=float(input("Masukan Nilai Tugas : ")) #perintah untuk input nilai tugas
uts=float(input("Masukan Nilai UTS : ")) #perintah untuk input nilai uts
uas=float(input("Masukan Nilai UAS : ")) #perintah untuk input nilai uas

#Rumus untuk mencari nilai akhir(rata-rata) dan jumlah nilai
na = (0.1 * kehadiran) + (0.2 * tugas) + (0.3 * uts) + (0.4 * uas) # menghitung NA dengan ketentuan

#Kondisi if untuk menentukan nilai huruf
if (na >=91) and (na <100):
    Grade = "A"
elif (na >=71) and (na <90 ):
    Grade = "B"
elif (na >=51) and (na < 70):
    Grade = "C"
elif (na >=31) and (na <50):
    Grade = "D"
elif (na >=00) and (na <30):
    Grade = "E"

#Kondisi if untuk menentukan keterangan Lulus atau Tidak Lulus
if na >=50 :
    Ket = "L"
else :
    Ket = "TL"

print("Jumlah Nilai :" , kehadiran + uts + uas + tugas) #Perintah untuk menjalankan Jumlah Nilai
print("Nilai Rata-rata :" , na) #Perintah untuk menjalankan Nilai Rata-rata
print("Nilai Grade :", Grade) #Perintah untuk menjalankan Nilai Grade
print("Keterangan :" , Ket) #Perintah untuk menjalankan Keterangan