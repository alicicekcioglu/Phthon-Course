import random,time

class Kumanda():

    def __init__(self,tv_durumu = "Kapalı", kanal_listesi = ["Trt"], kanal = "Trt", tv_ses = 0 ):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses,
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durumu == "Açık"):
            print("Televizyon zaten açık.")
        else:
            print("Televizyon açıldı. ")
            self.tv_durumu = "Açık"
    def tv_kapat(self):
        if (self.tv_durumu != "Açık"):
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapatıldı. ")
            self.tv_durumu = "Kapalı"
    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi azaltmak için (-) tuşuna basın.\n"
                          "Sesi arrttırmak için (+) tuşuna basın.\n"
                          "Çıkış için (Çıkış) tuşuna basın")
            if cevap == "<":
                if self.tv_ses == 0:
                    print("Minumum ses seviyesindesiniz.")
                else:
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif cevap == ">":
                if self.tv_ses == 32:
                    print("Maksimum ses seviyesine ulaştınız.")
                else:
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses güncellendi.",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        self.kanal_listesi.append(kanal_ismi)
        time.sleep(0.5)
        print(f"{kanal_ismi} eklendi.")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şua anki kanal.",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return f"Tv durumu: {self.tv_durumu}\nTV Ses: {self.tv_ses}\nKanal listesi: {self.kanal_listesi}\nKanal: {self.kanal}"


kumanda = Kumanda()

print("""
Televizyon Uygulaması:
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısı
6. Rasgele Kanala Geçme
7. Televizyon Bilgileri
Çıkmak için "q" ya basın
""")

while True:
    islem = input("\nİslemi Seçiniz: ")
    if islem == "q":
        print("Program sonlandırılıyor.")
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        kumanda.ses_ayarlari()
    elif islem == "4":
        kanal_isimleri = input("Kanal isimlerini virgül ile ayırarak giriniz.")
        kanal_listesi = kanal_isimleri.split(",")
        for i in kanal_listesi:
            kumanda.kanal_ekle(i)
    elif islem == "5":
        print(f"Kanal sayısı: {len(kumanda)}")
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "7":
        print(kumanda)
    else:
        print("Geçersiz işlem.")























































