class Yazilimci():
    def __init__(self,isim, soyisim, numara, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgilerigoster(self):
        print(f"""
        Yazılımcının özellikleri:
        İsim: {self.isim}
        Soy isim: {self.soyisim}
        Numara: {self.numara}
        Maas: {self.maas}
        Diller: {self.diller}
        """)
    def zamyap(self,zam):
        self.maas += zam
        print("Zam Yapıldı.")
    def dil_ekle(self,yenidil):
        self.diller.append(yenidil)
        print("Dil eklendi.")

yazilimci1 = Yazilimci("Ali","Çiçekçioğlu",12345,6000,["Python","Sql"])
print(yazilimci1.bilgilerigoster())
yazilimci1.dil_ekle("java")
print(yazilimci1.bilgilerigoster())

class computer():
    def __init__(self, brand, model, ram, hdd):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.hdd = hdd
    def info(self):
        print(f"""
        Brand: {self.brand}
        Model: {self.model}
        Ram: {self.ram}
        Hdd: {self.hdd}
        """)
    def update_brand(self,update):
        self.brand = update
        print("Brand changed.")

comp = computer("Asus", "A542", 8, 100)
comp.info()
comp.update_brand("lenovo")
comp.info()



