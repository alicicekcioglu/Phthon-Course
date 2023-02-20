def sayi_kontrol(a):
    sayi = input("Bir sayı giriniz. ")
    while not sayi.isdigit():
        print("Bu bir sayı değil.")
        sayi = input("Bir sayı giriniz. ")
    else:
        print("Bu bir sayı.")

sayi_kontrol(10)





















































