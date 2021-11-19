angka = int(input("Masukkan angka: "))
if angka % 2 == 0 and angka % 3 != 0:
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: YA")
    if angka % 5 != 0 and angka % 10 == 0:
        print("Apakah bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: IYA DONG")
    else :
        print("Apakah bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: TIDAK")
elif angka % 2 != 0 and angka % 3 != 0:
    print("Bilangan tersebut tidak habis dibagi 2 dan tidak habis dibagi 3. Program dihentikan")
elif angka % 2 != 0 and angka % 3 == 0:
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")
elif angka % 2 == 0 and angka % 3 == 0:
    print("Bilangan tersebut habis dibagi 2 dan habis dibagi 3. Program dihentikan")