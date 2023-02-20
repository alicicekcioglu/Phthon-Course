def int():
    num = float(input("Number: "))
    try:
        # Olası hatalar buraya girilir.
        # Bir hata oluşursa, uygun bir except bloğuna girer
        # Bir hata oluşması durumunda bloğun kalanı çalışmaz.
        print(f"Number: {round(num)}")
    except SyntaxError: #Hata1
        print("Syntax error. Lütfen girdinizi kontrol ediniz.")
    except ValueError: #Hata2
        print("Value error. Lütfen girdinizi kontrol ediniz.")
    except: #Hata3
        print("Bir hata oluştu.")
    finally: # Her koşulda çalışacak.
        print(f"Program sonlandı.")

"""Bazen kendi yazdığımız fonksiyonlar yanlış kullanılırsa kendi hatalarımız üretip Pythonda hataları fırlatabiliriz.
Bunun için raise anahtar kelimesi kullanılır.
            raise HataAdı(Mesaj)
"""

def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen string bir ifade giriniz.")
    else:
        return s[::-1]

