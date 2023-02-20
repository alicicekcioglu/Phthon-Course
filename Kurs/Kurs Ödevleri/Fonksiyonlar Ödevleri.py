"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının tam bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""
def mug_sayi(a):
    toplam = 0
    for i in range(1,a):
        if(a % i == 0):
            toplam += i
    return toplam == a

for i in range(1,1000):
    if(mug_sayi(i)):
        print("S:",i )


"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""

def ebob_bulucu(num1,num2):
    kucuksayi = min(num1,num2)
    ortakbolenler = []
    for i in range(1,kucuksayi+1):
        if (num1 % i == 0 and num2 % i == 0):
            ortakbolenler.append(i)
    ortakbolenler.sort(reverse=True)
    return ortakbolenler[0]

print(ebob_bulucu(40,60))

"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
"""

def ekok(num1, num2):
    carpim = num1 * num2
    num1kume = set()
    num2kume = set()
    for i in range(1, carpim):
        if (num1 * i != carpim):
            num1kume.add(num1 * i)
        else:
            break
    for x in range(1, carpim):
        if (num2 * x != carpim):
            num2kume.add(num2 + i)
        else:
            break

    katlar = num1kume.intersection(num2kume)
    y = list(katlar)
    y.sort()
    return y[0]

print(ekok(100,200))

"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi

"""
birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10
    return onlar[ikinci] + " " + birler[birinci]

sayi = int(input("Sayı: "))
print(okunus(sayi))





































