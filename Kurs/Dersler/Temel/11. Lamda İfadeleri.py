# list comprehension'ı hatırlayalım.

liste1 = [1,2,3,4,5]
liste2 = [i *2 for i in liste1] # [2, 4, 6, 8, 10]
print(liste2)

# Lamda ifadeleri (expression) list comprehension ile benzer mantıktadır.

# Lamda yazımı:
# etiket = lamda parametre1, paramatre 2... : işlem

# Klasik fonksiyon tanımlama:
def ikiyebol(x):
    return x/2

ikiyebol = lambda x : x/2
print(ikiyebol(20)) # 10.0

carpma = lambda a,b,c : a * b * c
print(carpma(3,4,5)) # 60

def terscevir(s):
    return s[::-1]
print(terscevir("abc")) #cba

terscevir = lambda x : x [::-1]
print(terscevir("abc"))  #cba

def ciftdegerbulma(a):
    return a % 2 == 0

print(ciftdegerbulma(2)) #True
print(ciftdegerbulma(3)) #False

ciftdegerbulma = lambda a : a % 2 == 0

print(ciftdegerbulma(44)) #True
print(ciftdegerbulma(571)) #False