# append() liste sonuna eleman ekler.

liste =  [1,2,4,5,6]
# liste.append(6,"Pytyon") # TypeError: list.append() takes exactly one argument (2 given)
liste.append(7)
print(liste) #[1, 2, 4, 5, 6, 7]

# extend() bir listeye başka bir listenin elemanlarını eklemeyi sağlar.

liste =  [1,2,4,5,6,7]
liste.extend([1,2,3,4,5,6,7,8,9,10])
print(liste)#[1, 2, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # sonuna ekler.
liste.sort()
print(liste) #[1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 10]

# insert() listeninbelli bir indeksine eleman ekler.

liste =  [1,2,3,4,5,6,7]
liste.insert(2,"Python") # ikinci index'e "Python" stringini ekleyecek.
print(liste) #[1, 2, 'Python', 3, 4, 5, 6, 7]

# pop() içine değer verilmezse listenin son elemanını silerek ekrana basar.
# İndex verilirse index'i silerek ekrana basar.

liste = [1,2,3,4,5]
print(liste.pop()) #5
print(liste.pop(0)) #1

#remove() verilen değeri listeden çıkarır.

liste = ["Python","Java","Armut","Elma"]
liste.remove("Elma")
print(liste) #['Python', 'Java', 'Armut']
# liste.remove("Kayısı") #ValueError: list.remove(x): x not in list

"""
index() verilen bir değerin baştan başlayarak hangi indekste olduğunu söyler. 
Değer listede yoksa hata döner #ValueError
Eğer ekstra indez değeri belirtilirse değeri girilen index'ten sonra aramaya başlar. 
"""
liste = [1,2,3,4,5,6,7,8,9]
print(liste.index(3)) #3 elemanını baştan başlayarak arar. 2. indexte.
print(liste.index(8,6)) # 8 elemanını 6. index'ten sonra aramaya başlar. 7. index'te

#count() metdu verilen bir değerin istede kaç defa geçtiğini sayar.

liste = [1,3,5,6,2,6,7,2,12,5,6,1,3,6,23]
print(liste.count(1)) # liste içinde 2 adet 1 değeri varmış.

#sort() metodu küçükten büyüğe ya da alfabetik olarak sıralar. Eğer özellikle içine "reverse = True" değeri
#verilirse değerleri büyükten küçüğe ya da ters alfabetik sıralar.

liste.sort()
print(liste) #[1, 1, 2, 2, 3, 3, 5, 5, 6, 6, 6, 6, 7, 12, 23]
liste.sort(reverse= True)
print(liste) #[23, 12, 7, 6, 6, 6, 6, 5, 5, 3, 3, 2, 2, 1, 1]

a = ["a","c","g","h"]
a.sort()
print(a) # ['a', 'c', 'g', 'h']
a.sort(reverse=True)
print(a) # ['h', 'g', 'c', 'a']






















