# Buatlah file JSON baru dengan nama dataku.json
# Pastikan format data JSON yang kamu tulis sudah benar. Lakukan validasi dengan JSONLint (https://jsonlint.com/)
# Tujuannya, agar nanti bisa dibaca di dalam program. Kalau format JSON-nya tidak valid, bisa jadi ia tidak akan bisa dibaca.

# Setelah itu, buat file baru dengan nama misalnya baca_data_json.py tapi saya menggunakan nama saya sendiri
# gunakan modul json
import json

# buka file JSON
file_json = open("E:\python\Json\dataku.json")

# Oh iya, kedua file ini harus di simpan dalam satu folder yang sama.
# Karena agar kita melakukan open("dataku.json"), yang artinya file JSON yang akan dibuka adalah file yang masih satu folder dengan file script python tersebut.
# Setelah itu, coba buka terminal dan jalankan program baca_data_json.py.

# prsing data JSON
data = json.loads(file_json.read())

# cetak isi data JSON
print(data)

