def armstrongCheck(a):

    sayi = int(input("Sayı: "))
    sayi_str = str(sayi)
    toplam = 0

    for i in sayi_str:
        x = int(i) ** len(sayi_str)
        toplam += x

    if(toplam == sayi):
        print("{} bir Armstrong sayısıdır.".format(sayi))
    else:
        print("{} bir Armstrong sayısı değildir.".format(sayi))

    armstrongCheck(0)
armstrongCheck(0)
