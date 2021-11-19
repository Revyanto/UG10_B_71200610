x = float(input("Masukkan bilangan pertama: "))
y = float(input("Masukkan bilangan kedua: "))
operasi = input ("Masukkan kalimat: ")
if "tambah" in operasi :
    hasil = x + y
    print ("Hasil penjumlahan", x, "dengan", y, "adalah", hasil)
elif "kurang" in operasi :
    hasil = x - y
    print ("Hasil penguarangan", x, "dengan", y, "adalah", hasil)
elif "kali" in operasi :
    hasil = x * y
    print ("Hasil perkalian", x, "dengan", y, "adalah", hasil)
elif "bagi" in operasi :
    hasil = x / y
    print ("Hasil pembagian", x, "dengan", y, "adalah", hasil)