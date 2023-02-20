liste = ["Elma","Armut","Muz","Kiraz"]

#Sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuc = list()
a = 0
for i in liste:
    sonuc.append((a,i))
    a += 1
print(sonuc)

# enumerate her bir elamanı indexler ile numaralandırıyor ve demet çiftleri oluşturuyor.

print(list(enumerate(liste)))

for i,j in enumerate(liste):
    print(i,j)

liste1 = ["a","b","c","d","e","f","g"]
for i,j in enumerate(liste1):
    if (i %2 == 0):
        print(j)

