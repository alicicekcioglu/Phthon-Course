sayi = int(input("Sayı: "))
toplam = 0
for i in range(1,sayi):
    if(sayi % i == 0):
        toplam += i
if(toplam == sayi):
    print("{} bir mükemmel sayıdır.".format(sayi))
else:
    print("{} bir mükkemmel sayı değildir.". format(sayi))
