# Pythonda tanımlanan değişkenler yerel (local) değişken olarak oluşturulur.
# Yerel fonksiyon çalışmayı bitirdikten sonra bellekten silinir.
# Bu sebeple fonksiyon içine tanımlanmış bir yerel değişkene başka bir yerden erişilmez.

# Global değişlkenler ise tanımlandıktan sonra programın her yerinde kullanılabilir.

def function():
    a = 5
    print(a)

function() # Çıktı: 5
print(a)
# a'yı sadece fonksiyon içinde tanımladık
# Bu yüzden fonksiyon dışında çalıştırırsak hata alırız.NameError: name 'a' is not defined

b = 5 #global alanda
def function():
    print(b)

function() #b global alanda olduğu için kullanıldı. Çıktı: 5

a = 2
def function():
    a = 1
    print(a)
function() # Fonksiyon içindeki yerel değer. Çıktı: 1
print(a) # Global değer Çıktı: 2

# Fonksiyon içerisinde, Globaldeki değeri kullanma ve değiştirme

x = 100
def function():
    global x
    x = 3
    print(x)

function() #Globaldeki x'i kullanmak istediğimizi belirterek değiştirdik. Çıktı: 3
print(x) # Fonksiyon içerisinde global değeri değiştirdik. Çıktı: 3

# if ve while döngüleri içerisindeki değerler global olarak tanımlanır.