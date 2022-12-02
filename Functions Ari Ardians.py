def my_function(country = "Indonesia"): #Nilai Parameter Default
      print("Saya Berasal dari " + country) #Jika kita memanggil fungsi tanpa argumen, ia menggunakan nilai default

my_function("Singapore")
my_function("Thailand")
my_function()
my_function("Malaysia")


def Nama(food): #Melewati Daftar sebagai Argumen
      for x in food:
          print(x) #printah untuk variabel x

Fruits = ["Anggur", "Belimbing", "Nangka"]

Nama(Fruits)


def sapa_lisa(): #Kode Program Functions
      print("Hai Lisa");
 
def sapa_sari():
  print("Morning, Sari");
 
def sapa_rudi():
  print("Halo bro,..");
 
sapa_lisa()
sapa_sari()
sapa_rudi()