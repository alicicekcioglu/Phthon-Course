# Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True



liste = [True,False,True,False,True]

hepsi(liste) #En az birisi False bu yüzden çıktı False

liste1 = [1,2,3,4,5] # 0 haricinde bütün sayırlar True sayılmaktadır.

print(hepsi(liste1))

# Herhangi bir değer True ise True, tüm değerler False ise False döndürmek istiyoruz.

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False


print(herhangi([True,False,True,False,True]))# en az bir tane True olduğu için True döndü
print(herhangi([0,0,0,0,0])) # sıfır false değerdir. Hepsi false olduğu için false döndürdü.

# all() fonksiyonu bütün değerler True ise True döndürür. En az bir değer False ise False döndürür.

liste = [True,False,True,False,True]
print(all(liste)) #False
liste = [True,True,True]
print(all(liste)) #True

# any fonksiyonu bütün değerler False ise False en az bir değer True ise True döndürür.

liste = [True,False,True,False,True]
print(any(liste)) #True
liste = [False]
print(any(liste)) #False
