#Return değer döndürür. Eğer aşağıdaki gibi değer vermeden işlem yaparsak nonetype olur ve işlemde kullanılmaz.
def toplama(a,b,c):
    print("Toplamları", a + b + c)

def ikiylecarp(a):
    print("Çarpımları: ", a*2)

toplam = toplama(3,4,5)
# ikiylecarp(toplam) #nonetype olduğu için hata verir.
print(type(toplam)) # <class 'NoneType'>

def toplama(a,b,c):
    return a+b+c
def ikiylecarp(a):
    return a*2

toplam = toplama(1,1,1)
print(ikiylecarp(toplam))

####
def uclecarp(a):
    print("Birinci fonksiyon çalıştı.")
    return (a*3) # return sonrası işlemler çalışmaz bu sebeple parametrede en altta olmalı. Print altta olsa çalışmazdı.
def ikiyletopla(a):
    print("İkinci fonksiyon çalıştı.")
    return (a+2)
def dordebol(a):
    print("Üçüncü fonksiyon çalıştı.")
    return(a/4)

print(dordebol(ikiyletopla(uclecarp(5))))

# değer döndürmeyen fonksiyonlara void fonksiyon denir.