#Nama   : Ari Ardiansyah
#NIM    : 210741031

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKGREEN + "Ari "+ bcolors.HEADER + "Ardiansyah")


Nama_aku='Ari '
Balik=Nama_aku[::-1]
My_name='Ardiansyah'
Flip=My_name[::-1]

print( bcolors.HEADER+ Flip+ bcolors.OKGREEN+ Balik )