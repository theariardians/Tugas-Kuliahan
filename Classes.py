#pertama
class MyClass: #perintah untuk membuat class 
  z = 3 #perintah untuk membuat properti bernama z

#kedua 
p2 = MyClass() #perintah untuk membuat object p2
print(p2.z) #perintah untuk mencetak nilai z

#ketiga
class book: # perintah untuk membuat class bernama book
  def _init_(self, name, years): #perintah untuk menetapkan nama dan tahun
    self.name = name
    self.years = years

p3 = book("Algoritma", 2021) #perintah untuk memberi tahu object yang di cetak adalah p3

print(p3.name)#perintah untuk mencetak p3 berupa name
print(p3.years)#perintah untuk mencetak p3 berupa years

#keempat
class motor: # perintah untuk membuat class bernama motor
  def _init_(self, nama, years): #perintah untuk menetapkan nama dan tahun
    self.nama = nama
    self.years = years

p1 = motor("Yamaha",2003) #perintah untuk memberi tahu object yang di cetak adalah p1

print(p1.nama) #perintah untuk mencetak p3 berupa nama
print(p1.years) #perintah untuk mencetak p3 berupa tahun

#kelima
class fruits: # perintah untuk membuat class bernama fruits
  def _init_(self, nama, years): #perintah untuk menetapkan nama dan tahun
    self.nama = nama
    self.years = years

p4 = fruits("durian",2021) #perintah untuk memberi tahu object yang di cetak adalah p4

print(p4.nama) #perintah untuk mencetak p4 berupa nama
print(p4.years) #perintah untuk mencetak p4 berupa tahun