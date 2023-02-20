"""
Dosya açmak:
    Bir dosyayı açmak için open() fonksiyonunu kullanıyoruz.
                open(dosya_adı,dosya_erişme_kipi)
    Dosya erişme kişi bizim dosya üzerindeki işlemlerimizi belirler.

    w dosya kipi
    "w" kipi bulunduğumuz dizine bir dosya oluşturur. Aynı isimli farklı bir dosya varsa eskisini siler ve yeniden
    oluşturur.
"""

file1 = open("bigiler.txt","w") #encoding="uft-8" en genel karakter dizisi
file1.write("Ali Çiçekçioğlu")
file1.close()#dosya kapatma işi işlem bitince özellikle yapılmalıdır.

"""
a kişiyele dosya yazmak:
    "append" kelimesinin kısaltması olan "a" kipiyle dosya açıldığında dosya eğer yoksa oluşturulur. Dosya varsa tekrar
     oluşturulmaz.
    Dosya imleci dosyanın sonuna giderek ekleme yapmamızı sağlar. 
"""
file2 = open("Bilgiler.txt","a")
file2.write("Selam")
file2.close()
file2 = open("Bilgiler.txt","a")
file2.write(" nasılsın?")
file2.close()

