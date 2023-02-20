"""eğer bir dosyanınbelli bir yerine seek() fonksiyonun ile gidip write() fonksiyonunu kullanırsak yazdığımız değerler
öncesnde bulunan değerlerin üzerine yazılacaktır. BUnu niçin hem okuma hem de yazma işlemmimizi yapmamızı sağlayan "r+"
kipini kullanacağız. İlk önce sdosyamıza bilgileri görelim.
"""
with open("Bilgiler.txt","r+") as file:
    file.seek(0)
    file.write("Deneme")
    print(file.read())

"""
Dosyanın sonunda değişiklik yapmak

    Dosyaların sonunda değişiklik yapmak için dosyamızı "a" kipiyle açalım ve sadece dosyanın sonuan write() 
    ile ekleme yapalım.
"""
with open("Bilgiler.txt","a")as file:
    file.write("Selam ne haber bebiş.\n")
    print(file.read())
"""
    Dosyanın başında değişiklik yapmak için seek() fonksiyonu ile dosyanın başına giderek write() fonksiyonu ile 
    yapmak istedğim değişikliği yapabilirim.
"""
with open("Bilgiler.txt","r+") as file:
    icerik  = file.read()
    icerik = "Merhaba zayıf yürekli insan\n" + icerik
    print(icerik)
    file.seek(0)
    file.write(icerik)

"""
    Dosyanın ortasında değişiklik yapmak için ilk olarak her bir satırı liste halinde almamızı sağlayan readlines()
    fonsiyonunu kullanacağız. Daha sonra bu listenin herhangi bir yerinde bir eleman ekleyerek bu listeyi 
    for dönüsü ile dosyaya yazacağız. 
"""
with open("Bilgiler.txt","r") as file:
    print(file.readlines)

"""
    Örneğin Merhaba satırının altına bir tane daha satır eklemek istiyoruz. Bunun için bu listenin 3. indeksine insert()
    metodunuyla bir satır ekleyeceğz. Daha sonra dosyanın başına giderek bu listeyi tek tek for döngüsü ile yazacağız. 
"""

with open("Bilgiler.txt","r") as file:
    liste = file.readlines()
    liste.insert(3,"Dünya gelip geçici, sen de öylesin. Bu yüzden BOŞVER!\n")
    print(liste)
    file.seek(0)
    for i in liste:
        file.write(i)

    # ya da

with open("Bilgiler.txt","r") as file:
    liste = file.readlines()
    liste.insert(3,"Dünya gelip geçici, sen de öylesin. Bu yüzden BOŞVER!\n")
    print(liste)
    file.seek(0)
    file.writelines(liste)