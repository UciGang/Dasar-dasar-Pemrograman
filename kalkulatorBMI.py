#program hitung berat badan ideal
#input
jenisKelamin = str(input("Masukkan jenis kelamin anda (pria/wanita) = "))
tinggiBadan = int(input("Masukkan tinggi badan anda (dalam centimeter) = "))

#rumus
if jenisKelamin == "pria":
    beratIdeal = (tinggiBadan - 100) - ((tinggiBadan - 100) * 10/100)
    print("Berat badan ideal kamu adalah = ", beratIdeal , "Kg")
else:
    beratIdeal = (tinggiBadan - 100) - ((tinggiBadan - 100) * 15/100)
    print("Berat badan ideal kamu adalah = ", beratIdeal , "Kg")