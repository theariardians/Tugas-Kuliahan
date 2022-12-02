nama = input ("Masukan Nama : ")
nim = input ("Masukan NIM : ")
absen = float(input("Masukan Nilai kehadiran : "))
tugas = float(input("Masukan Nilai Tugas : "))
uts = float(input("Masukan Nilai UTS : "))
uas = float(input("Masukan Nilai UAS : "))

na = (0.1 * absen) + (0.2 * tugas) + (0.3 * uts) + (0.4 * uas)
if (na >= 0) and (na <30):
    Grade = "E"
    ket = "TIDAK LULUS"
if (na >= 31) and (na <50):
    Grade = "D"
    ket = "TIDAK LULUS"
if (na >= 51) and (na <70):
    Grade = "c"
    ket = "LULUS"
if (na >= 71) and (na <90):
    Grade = "B"
    ket = "LULUS"
if (na >= 91) and (na <100):
    Grade = "A"
    ket = "LULUS"

print("Jumlah Nilai :", absen + tugas + uts + uas)
print("nilai Rata-rata :", na)
print("Nilai Grade :", Grade)
print("Keterangan: ", ket)