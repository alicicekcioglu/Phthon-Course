"""
Problem 1
Elinizde uzunca bir string olsun.
            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
"""

a = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
b = dict()

for i in a:
    if i in b:
        b[i] +=1
    else:
        b[i] = 1

for p,y in b.items():
    print(f"{p} : {y}")


"""
"şiir.txt" dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun 
ve bu string'i ekrana yazdırın.
"""

a = ""

with open("şiir.txt","r",encoding="utf-8") as file:
    for i in file:
        a += i[0]
print(a)


"""
Problem 3
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir 
satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
"""


with open("mailler.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i[:-1]
        if i.endswith(".com") and i.find("@") != -1:
            print(i)


"""
Problem 4
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve 
soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
"""

isim = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisim = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

a = list(zip(isim,soyisim))
for i,y in a:
    print(i,y)