#menginput Nama,NIM dan Nilai
Nama=input("Masukan Nama            : Ari Ardiansysah")
NIM=input("Masukan NIM              : 210741031")
KEHADIRAN=input("Masukan Kehadiran  : 16")
UTS=input("Masukan Nilai UTS        : 90")
UAS=input("Masukan Nilai UAS        : 85")
TUGAS=input("Masukan Nilai Tugas    : 95")

KEHADIRAN=KEHADIRAN*10/100;
UTS=UTS*30/100;
UAS=UAS*40/100;
TUGAS=TUGAS*20/100;

#Formula mencari nilai akhir
Nilai_Akhir=KEHADIRAN+UTS+UAS+TUGAS

#Menampilkan Output Nama, NIM dan Nilai yang telah diinput
print("Nama         : %s") %Nama                #%s   : Tipe datang String
print("NIM          : %s") %NIM
print("KEHADIRAN    : %d") %KEHADIRAN           #%d   : Tipe data Interger
print("Nilai UTS    : %d") %UTS
print("Nilai UAS    : %d") %UAS
print("Nilai TUGAS  : %d") %TUGAS
print("Nilai Akhir  : %f") ,float(Nilai_Akhir)    #%f   : Tipe data Float(Desimal)

#Kondisi if untuk menentukan nilai huruf
if Nilai_Akhir >=91 :
    print ("Grade   : A")
elif Nilai_Akhir >=80 :
    print("Grade    : B")
elif Nilai_Akhir >=51 :
    print("Grade    : C")
elif Nilai_Akhir >=31 :
    print("Grade    : D")
elif Nilai_Akhir >=00 :
    print("Grade    : E")

#Kondisi if untuk menentukan keterangan Lulus atau Tidak Lulus
if Nilai_Akhir >=60 :
    print("Keterangan : L")
else :
    print("Keterangan : TL")

