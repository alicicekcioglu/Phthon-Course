"""
Kümeler, matematikte olduğu gibi bir elemandan sadece bir adet tutan bir veri tipidir. Bu açıdan kullanıldıkları
yerde çok önemli ber veri tipi olmaktadırlar.
"""

# Küme Oluşturma

x = set() # boş küme
c = {1,2,3}
print(type(x)) #<class 'set'>

liste =[1,2,3,4,1,1,2,2,2] #aynı elemanı çok defa barındıran bir liste
x = set(liste) # veri tipi dönüşümü
print(x) # {1, 2, 3, 4} aynı elemanlar tek bir elemana indirgendi.

a = set("Python Programlama Dili")
print(a) #{'t', 'y', 'D', 'h', 'a', 'o', 'l', 'm', 'g', 'i', 'P', ' ', 'n', 'r'}

b = {"Python","Python","Java"}
print(b) # {'Java', 'Python'}

"""
For döngüsüyle gezinmek. 
"""
x = {"Python","Java","Php","Java","C","Javascript"}
for i in x:
    print(i)

"""
Kümelerin değerlerine doğrudan ulaşılamaz örneğin x[0] x["Python"] gibi denemeler hata verir.
İlla bastırmak istersek yukarıdaki gibi for döngüsü ile ya da listeye çevirerek ulaşabiliriz. 
"""
liste = list(x)

"""
Kümelerin metodları
"""

# Eleman eklemek için add() kullanılır. Aynı elemanı eklersek eklemez.

x = {1,2,3}
x.add(4)
x.add(4) # Tekrar eklemedi.

# İki kümenin farkını alma. # kume1.difference(kume2) # kume1'in küme2'den farkı

kume1 = {1,2,4,10,34,100,-2}
kume2 = {1,2,23,34,-1}

print(kume1.difference(kume2)) # {10, 100, 4, -2}
print(kume2.difference(kume1)) # {-1, 23}

# İki kümenin farkını güncelleme #kume1.difference_update(kume2) #

print(kume1) # {1, 2, 34, 100, 4, 10, -2}
print(kume2) # {1,2,23,34,-1}
kume1.difference_update(kume2)
print(kume1) # {100, 4, 10, -2} ortak olanlar silindi sadece farklı olanlar kaldı.

# Kümeden eleman çıkarmak için discard() metodu kullanılır. Değer yoksa hiç bir şey yapmaz.

kume1 = {1,2,3,4}
kume1.discard(2)
print(kume1) # {1,3,4}

# Küme kesişimleri intersection() metodu ile alınır.

k1 = {1,2,3,4,5}
k2 = {2,3,7,8,9}
print(k1.intersection(k2)) #{2, 3}

# Küme kesişimleri ve güncelleme : intersection_update()

k1 = {1,2,3,4,5}
k2 = {2,3,7,8,9}
k1.intersection_update(k2)
print(k1) #{2, 3}

# isdisjoint() metodu iki kümenin kesişim kümesi boş ise True, değilse False döner.

k1 = {1,2,3,10,34,100,-2}
k2 = {1,2,23,34,-1}
k3 = {30,40,50}

print(k1.isdisjoint(k2)) #False kesişen değerler olduğu için False döndü.
print(k1.isdisjoint(k3)) # True kesişen değer olmadığı için yani boş küme olduğu için False döndü.

# .issubset() birinci küme ikinci kümenin alt kümesiyse True değilse False döner.

k1 = {1,2,3}
k2 = {1,2,3,4}
k3 = {5,6,7}

print(k1.issubset(k2)) #True # küme1 küme2 nin alt kümsidir.
print(k1.issubset(k3)) #False # küme1 küme3'ün alt kümesi değildir.

# union() iki kümenin birleşim kümesini döner

print(k1.union(k2)) #{1, 2, 3, 4} // ortak değerleri almaz.

# birleşim kümesi update için update() metodu kullanılır.
k1.update(k2)

print(k1) # {1, 2, 3, 4}