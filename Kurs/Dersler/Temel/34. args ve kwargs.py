# *args ve **kwargs

def fonksiyon(*args): #istediğimiz sayıda argüman gönderebiliyoruz.
    print(args)
    for i in args:
        print(i)
def fonksiyon(isim, *args):
    print("isim: ",isim)
    print("------------")
    for i in args:
        print(i)

# **kwargs argümanları isim vererek göndermeyi sağlar. 

def fonksiyon(**kwargs): #argümanlardan sözlük oluşturuyor.
    print(kwargs)

fonksiyon(isim = "ali", soyisim = "çiçekçioğlu", numara = 123)
# {'isim': 'ali', 'soyisim': 'çiçekçioğlu', 'numara': 123}

def fonksiyon(**kwargs): 
    print(kwargs)
    for i,j in kwargs.items():
        print("Argüman ismi: ",i,"Argüman Değeri: ",j)
fonksiyon(isim = "ali", soyisim = "çiçekçioğlu", numara = 123)
    
"""
Argüman ismi:  isim Argüman Değeri:  ali
Argüman ismi:  soyisim Argüman Değeri:  çiçekçioğlu
Argüman ismi:  numara Argüman Değeri:  123
"""

def fonksiyon(*args, **kwargs):
    for i in args:
        print(i)
    print("---------")
    for i,j in kwargs.items():
        print(i,j)
fonksiyon(1,2,4,5,6,isim = "ali", soyisim = "çiçekçioğlu", numara = 123)


