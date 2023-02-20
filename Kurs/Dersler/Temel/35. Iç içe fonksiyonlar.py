import PyQt5
def selam(isim):
    print("selam ",isim)

merhaba = selam
merhaba("ali")

def fonksiyon():
    def fonksiyon2():
        print("selam")
    fonksiyon2()
    print("merhaba")

fonksiyon()

def fonksiyon(*args):
    def toplama(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(toplama(args))

fonksiyon(1,2,4,5,6,7,8,8)
