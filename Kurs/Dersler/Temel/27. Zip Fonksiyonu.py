liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
liste3 = ["Python","Java","JavaScript"]

i = 0
sonuc = list()
while (i < len(liste1) and i < len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i +=1

print(sonuc)

# zip fonksiyonu iki liste elemanını demet şeklinde sırasıyla gruplayarak tek bir liste oluşturur.

print(list(zip(liste1,liste2)))
print(list(zip(liste1,liste2,liste3)))

# aynı anda iki liste üzerinde gezinmek için çok yararlı bir fonksiyon

liste4 = ["Türkiye","Almana","Fransa","İngiltere"]
liste5 = ["Ankara","Berlin","Paris","Londra"]

for i,j in zip(liste4,liste5):
    print("Ülke:",i,"---->","Başkent:",j)

sozluk1 = {"Elma":1,"Armut":2,"Kiraz":3}
sozluk2 = {"Sıfır":1,"Bir":1,"İki":2}

print(list(zip(sozluk1,sozluk2))) # sadece anahtarları gruplar
print(list(zip(sozluk1,sozluk2.values()))) #değerleri ve anahtarı gruplama
print(list(zip(sozluk1.values(),sozluk2.values()))) #anahtar ve anahtarı gruplama
