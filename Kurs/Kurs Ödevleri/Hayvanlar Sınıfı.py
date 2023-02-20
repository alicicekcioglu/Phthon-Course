class Hayvanlar():
    def __init__(self,isim, cinsiyet,yas,kilo):
        self.cinsiyet = cinsiyet
        self.yas = yas
        self.kilo = kilo
        self.isim = isim
    def hayvan_bilgisi(self):
        print(f"""
        Name: {self.isim}
        Cinsiyet: {self.cinsiyet}
        Yaş: {self.yas}
        Kilo: {self.kilo}
        """)
    def kilo_degistirme(self,yeni_kilo):
        self.kilo = yeni_kilo

class Kopek(Hayvanlar):
    def isim_degistirme(self,yeni_isim):
        self.isim = yeni_isim

class Kus(Hayvanlar):
    def tuydokmedonemi(self):
        mevsim = input("Hangi mevsimdesiniz?: ")
        if mevsim == "kış" or mevsim == "sonbahar":
            print("Kuşunuz tüy dökme döneminde")
        else:
            print("Kuşunuz tüy dökme döneminde değil.")
    def kuskilo(self):
        print(self.kilo)

class At(Hayvanlar):
    def yasekleme(self,yeniyas):
        self.yas += yeniyas
    def atkilo(self):
        print(at.kilo)

at1 = At("jo","Erkek",1,35)
at1.yasekleme(4)
at1.atkilo()


