fruits = ["Apel", "Alpukat", "Blueberry"] #Looping Melalui String
for x in "Apel": 
  print(x) #perintah untuk variabel x


fruits = ["Durian", "Alpukat", "Nanas"] #The break Statement
for y in fruits:
  if y == "Alpukat":
    break #dapat menghentikan loop sebelum loop melewati semua item
  print(y) #perintah untuk variabel y


  fruits = ["Apel", "Durian", "Nanas"] #The continue Statement
for a in fruits:
  if a == "Durian":
    continue #dapat menghentikan iterasi loop saat ini, dan melanjutkan dengan yang berikutnya
  print(a) #perintah untuk variabel a