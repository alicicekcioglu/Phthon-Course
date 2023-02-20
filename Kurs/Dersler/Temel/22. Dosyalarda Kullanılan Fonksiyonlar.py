# Dosyaları otomatik kapatma
with open("bigiler.txt","r") as file: #bu blok bitince dosya otomatik kapanır. File değişkeni yerine isteğişini yaz.
    for i in file:
        print(i)

"""
Dosyaları ileri geri sarmak
    Python'daki seek() fonksiyonunu kullanacağız. Anck ondan önce dosya imlecinin hangi byteda olduğunu söyleyen 
    tell() fonkisyonuna bakalım.
"""

with open("Bilgiler.txt","r") as file:
    print(file.tell())

# Hiç bir işlem yapmadığımız için tell() fonksiyonu dosyanın en başında (0. bytreda) olduğumuzu söyledi.
# İmleci dosyanın 20. byteına götürmek için seek() fonksiyonu kullanılır.

with open ("Bilgiler.txt","r") as file:
    file.seek(9)
    print(file.tell())

with open ("Bilgiler.txt","r") as file:
    file.seek(0)
    icerik = file.read(7)
    print(file.tell())
    print(icerik)
    icerik2 = file.read(9)
    print(icerik2)