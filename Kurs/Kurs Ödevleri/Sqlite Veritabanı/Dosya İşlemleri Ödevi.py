"""
                     Örnek Metodlar;

                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil

"""
import sqlite3
import PyQt5

class Sarkı():
    def __init__(self,sarki_ismi,sanatci, album, sirket,sarki_suresi):
        self.sarki_ismi = sarki_ismi
        self.sanatci = sanatci
        self.album = album
        self.sirket = sirket
        self.sarki_suresi = sarki_suresi

    def __str__(self):
        return f"Şarkı adı: {self.sarki_ismi}\n" \
               f"Sanatçı: {self.sanatci}\n" \
               f"Albüm: {self.album}\n" \
               f"Şirket: {self.sirkets}\n" \
               f"Şarkı Süresi: {self.sarki_suresi}"
class Sarki_listesi():
    def __init__(self):
        self.connection

    def connection(self):
        self.connect = sqlite3.connect()