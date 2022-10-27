#program menghitung luas dan keliling lingkaran
#input
r = input("Masukkan jari-jari lingkaran = ")

#rumus
phi = float(3.14)
luas = phi * int(r) * int(r)
keliling = 2 * phi * int(r)

#output
print("Luas Lingkaran tersebut adalah = ", luas)
print("Keliling Lingkaran tersebut adalah = ", keliling)