def selamla(isim):
    print("Selam", isim)

selamla("Mehmet") #Selam Mehmet

# selamla() bu şekilde boş geçersem değer girmediğim için hata alırım. Ama;

def selamla(isim = "İsimsiz"):
    print("Selam", isim)

selamla() # Selam İsimsiz
selamla("Süt") # Selam Süt

def ogr_bilgileri(ad, soyad, numara):
    print("Adı: {}\nSoyadı: {}\nNumara: {}".format(ad,soyad,numara))

ogr_bilgileri("Ali","Çiçekçioğlu",201414004054)
"""
Çıktı: 
Adı: Ali
Soyadı: Çiçekçioğlu
Numara: 201414004054
"""

def ogr_bilgileri(ad = "Bilgi Yok", soyad = "Bilgi Yok", numara = "Bilgi Yok"):
    print("Adı: {}\nSoyadı: {}\nNumara: {}".format(ad,soyad,numara))
ogr_bilgileri()

"""
Çıktı: 
Adı: Bilgi Yok
Soyadı: Bilgi Yok
Numara: Bilgi Yok
"""

ogr_bilgileri("Ali","Çiçekçioğlu")
"""
Çıktı: 
Adı: Ali
Soyadı: Çiçekçioğlu
Numara: Bilgi Yok
"""

ogr_bilgileri(numara = "201414004054") # doğrudan 2. değer girilmek istenirse özel olarak belirtilmeli yoksa numarayı isim olarak algılar.

"""
Çıktı: 
Adı: Bilgi Yok
Soyadı: Bilgi Yok
Numara: 201414004054
"""

"""
Esnek Sayıda Değerler:
"""
def carpma(a,b,c):
    print(a*b*c)

carpma(3,4,5,6)
# Çıktı: TypeError: toplama() takes 3 positional arguments but 4 were given

#Esnek Değer
def carpma(*a):
    print(a)

carpma(3,4,5,6,7,8)
# Değerleri tuple olarak çıkardı. Çıktı:  (3, 4, 5, 6, 7, 8)

# Fonksiyonu yeniden işimize yarayacak şekilde yazıyoruz.
def carpma(*a):
    carpim = 1 #Çarpma işlemi olduğu için bir veriyoruz.
    for i in a:
        carpim *= i
    print(carpim)

carpma(2,2,2) # Çıktı: 8

