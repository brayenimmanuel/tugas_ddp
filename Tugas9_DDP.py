#Nomor 1
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

#Nomor 2
def is_genap(bilangan):
    return bilangan % 2 == 0

print(is_genap(4))
print(is_genap(7)) 

#Nomor 3
def nilai(skor):
    if skor >= 75: 
        print("Lulus")
    else:
        print("Gagal") 

nilai(80)
nilai(60)

#Nomor 4
def bilangan(n):
    # hasil = []
    # for i in range(1, n): 
    #     if i % 2  != 0:
    #         hasil.append(i)
    # print(hasil)
    for i in range(1, n, 2):
        print(i, end=" ")

bilangan(20) 