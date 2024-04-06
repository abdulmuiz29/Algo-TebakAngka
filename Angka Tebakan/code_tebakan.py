# QUIZ 1

import random
angka = random.randint(0,100)

kesempatan = 10
while kesempatan > 0:   # Di sini saya memakai perulangan while, karena menunjukkan banyak perulangan yang tidak tentu
    tebakan = int(input("Masukkan angka tebakan :"))
    if tebakan < angka:
        kesempatan -= 1
        print("Angka terlalu kecil\n")
    elif tebakan > angka:
        kesempatan -= 1
        print("Angka terlalu besar\n")
    elif tebakan == angka:
        print(f'Angka anda benar setelah menebak {kesempatan} kali')
        break   # break untuk menghentikan perulangan
if kesempatan == 0:
    print("Anda kurang beruntung")