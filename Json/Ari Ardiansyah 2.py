# gunakan modul json
import json

# buka file JSON
file_json = open("E:\python\Json\dataku.json")

# prsing data JSON
data = json.loads(file_json.read())

#print(data)

# sekarang.. kita modifikasi lagi programnya, ubahlah print(data) menjadi seperti ini:
# cetak isi data JSON
print(f"Nama: {data['name']}")
print(f"Website: {data['web']}")
print("Sosial Media:")
print(f"- Facebook: {data['social_media']['facebook']}")
print(f"- Twitter: {data['social_media']['twitter']}")
print(f"- Instagram: {data['social_media']['instagram']}")