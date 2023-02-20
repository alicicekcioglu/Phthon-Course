def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi == 1 or sayi == 0):
        print("Faktoriyel", faktoriyel)
    else:
        while(sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print(faktoriyel)

faktoriyel(10)

