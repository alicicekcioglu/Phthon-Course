# Fonksiyon tanımlama
# def foksiyon_adı (parametre1 , parametre2.....(opsiyonel))
    #foksiyon bloğu
    #yapılacak işlemler
    #dönüş değeri - opsiyonel.

#Selamlama fonksiyonu örneği.
def selamla():
    print("Merhaba...")
    print("Nasılsınız?")
selamla()

# Parametreler ve Argumanlar.
def selamla(isim): #isim literatürde argüman olarak geçiyor.
    print("Merhaba:", isim)

selamla("Ali")

def toplama(a,b,c):
    print("Toplamları", a+b+c)
toplama(1,1,1)

def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi == 0 or sayi == 1):
        print("Faktoriyel", faktoriyel)
    else:
        while (sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print("Faktoriyel", faktoriyel)

faktoriyel(10)




