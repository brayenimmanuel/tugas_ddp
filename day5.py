#Soal Nomor 1
my_list = ['Vario', 'Matic', '150cc', 'Hitam Metalic','Roda 2' ]
print(my_list)

my_list.append('Rp 25.000.000')
my_list.append('Scooter')
print(my_list)

my_list.insert(2, 'Honda')
print(my_list)

#soal Nomor 2
i = int (input('Ketik 1, Maka Menghitung Luas Persergi. Ketik 2, Maka Menghitung Luas Lingkaran. Ketik 3, Maka Menghitung Luas Segitiga\n'))
match i:
     case 1:
         sisi = int(input("Masukan Sisi Persegi : "))
         luas_persegi = sisi * sisi
         print(luas_persegi)
     case 2:
         jari = int(input("Masukan Jari-Jari Lingkaran : "))
         phi = 3.14
         luas_lingkaran = phi*jari**2
         print(luas_lingkaran)
     case 3:
         alas = int(input("Masukan Alas Segitiga : "))
         tinggi = int(input("Masukan Tinggi Segitiga : "))
         luas_segitiga = 1/2*alas*tinggi
         print(luas_segitiga)
     case _:
         print('Cuma Ada 1 Sampe 3 Doang Bejir!!!')

