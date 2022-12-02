# Buatlah file JSON baru dengan nama dataku.json

# Setelah itu, buat file baru dengan nama misalnya baca_data_json.py tapi saya menggunakan nama saya sendiri
# gunakan modul json
import json

# buka file JSON
file_json = open("E:\python\Json\dataku.json")

# prsing data JSON
data = json.loads(file_json.read())

# Setelah itu, coba buka terminal dan jalankan program baca_data_json.py.
# cetak isi data JSON
print(data)

