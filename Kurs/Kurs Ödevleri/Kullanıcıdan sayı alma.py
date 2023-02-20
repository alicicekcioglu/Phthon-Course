
toplam = 0
while True:
    sayi = input("Sayı: ")
    if (sayi == "q" or "Q"):
        break
    sayi = int(sayi)
    toplam += sayi
print("Toplam: {}".format(toplam))
