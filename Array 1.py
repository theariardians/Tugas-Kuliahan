#Penerapan Array 3 Dimensi
from tabulate  import tabulate 

# Array 3 Dimensi bentuk kubus 4 x 5 x 3
a = [
    [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]],
    [[6,6,6],[7,7,7],[8,8,8][9,9,9],[10,10,10]],
    [[11,11,11],[12,12,12],[13,13,13],[14,14,14],[15,15,15]],
    [[16,16,16],[17,17,17],[18,18,18],[19,19,19],[20,20,20]]
    ]
print(a[2])
print("="*30)
print("Hasil Tabel blok pertama index ke 0")
for i in a:
    for b in i:
        print(b[0],end=" ")
    print()
tabel = tabulate(a[0], tablefmt="fancy_grid")
print(tabel)
