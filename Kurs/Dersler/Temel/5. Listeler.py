"""
Listeler
Şimdi de yeni bir veritipimiz olan listeleri öğrenmeye çalışalım. Listeler yapıları gereği stringlere oldukça benzerler
ve kullanıldıkları yerler de çok yararlı olan bir veritipidir. Tıpkı stringler gibi ,indekslenirler,parçalanırlar ve
üzerinde değişik işlemler yapabildiğimiz metodlar bulunur. Ancak listelerin stringlerden önemli farkları da
bulunmaktadır. Stringler konusundan bildiğimiz kadarıyla stringler değiştirilemez bir veri tipidir. Ancak, listelerimiz
değiştirilebilir bir veritipidir.

Bir listede her veritipinden elemanı saklayabiliriz. Bu anlamda sıralı bir diziye benzer. Peki bu konuda ne öğreneceğiz?

       1.Liste oluşturma
       2.Indeksleme ve Parçalama
       3.Temel Liste Metodları ve İşlemleri
       4.İç içe Listeler
"""

# Listeler bir [] köşeli parantez içine veriler veya değerler konarak oluşturulabilir

liste = ["elma", 35, "merhaba", 3.14, 5]
print(type(liste))

liste = []
print(liste)

# Boş liste . list() fonksiyonuyla da oluşturulabilir.
bos_liste = list()

# len fonksiyonu listeler üzerinde de kullanılabilir.
liste3 = [3,4,5,6,6,7,8,9,0,0,0]
len(liste3)

# Bir string list() fonksiyonu yardımıyla listeye dönüştürülebilir.
s =  "Merhaba"
list =  list(s)

# Listeleri indeksleme ve parçalama stringlerle birebir olarak aynıdır.


# Bir listeyi birbirine toplama işlemini stringlerdeki gibi yapabiliriz.
liste1 =  [1,2,3,4,5]
liste2 =  [6,7,8,9,10]
liste1 + liste2

# Bir listeye bir tane eleman eklemek içinse aşağıdaki işlemi uygulayabiliriz.
liste = [1,2,3,4]
liste =  liste + ["Murat"]

# Listeler direk olarak değiştirilebilirler.
liste[0] = 10
