"""
Decorator fonksiyonlar, Pythonda fonksiyonlarımızı dinamik olark ekstra özellik eklediğimiz fonksiyonlarır ve dacorator
fonksiyonların kulolanımı kod tekrar yapmamızı engeller.

Pythonda decorator fonksiyonlar Flask gibi frameworklerde oldukça çok kullanılır.
"""

import time

"""
def kareleri_hesapla(sayilar):
    sonuc = list()
    baslama = time.time() #şuanki zamanı saniye cinsinden verir
    for i in sayilar:
        sonuc.append(i ** 2)
    bitis = time.time()
    print("Bu fonksiyon"+ str(bitis-baslama)+"saniye sürdü.")
    return sonuc

def küpleri_hesapla(sayilar):
    sonuc = list()
    baslama = time.time()
    for i in sayilar:
        sonuc.append(i ** 3)
    bitis = time.time()
    print("Bu fonksiyon" + str(bitis - baslama) + "saniye sürdü.")
    return sonuc


kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))
"""

"""
Yukarıdaki gibi her fonksiyon için tek tek zaman hesaplama fonksiyonu girmek yerine bunu tek bir fonksiyonda
halldedebiliriz.
"""

def zaman_hesapla(func):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = func(sayilar)
        bitis = time.time()
        print(func.__name__+" "+str(bitis-baslama)+"saniye sürdü.")
    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i ** 2)
    return sonuc

@zaman_hesapla
def küpleri_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i**3)
    return sonuc

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))



























