class student():
    matematik = 100
    cografya = 55
    tarih = 67
    turkce = 47
    fizik = 85
    isim = "mehmet demircan"

ogrenci1 = student()
ogrenci2 = student()

print(ogrenci1.fizik)
print(ogrenci2.fizik)
print(student.fizik)

# Yukarıdaki tüm objelerin özellikleri aslında aynı. Bizim faklı objeleri farklı özellikle oluşturmamız gerekiyor.
# Bunun için init fonksiyonu kullanılır.

print(dir(ogrenci1))

#init metodu Pythonda yapıcı(constructor) bir fonksiyondur. Objeleri oluşturuken otomatik olarak ilk çağrılan fonksiyondur.
# Bu metodu özel olarak tanımlayarak objeleri farklı değerlerle oluşturabiliriz.

class student():
    math = 100
    art = 55
    history = 67
    language = 47
    physic = 85
    name = "mehmet demircan"
    def __init__(self):
        print("init function called")

student1 = student()
print(student1)


class computer():
    def __init__(self, model, colour, ram, ssd):
        print("init function called")
        self.model = model
        self.colour = colour
        self.ram = ram
        self.ssd = ssd


computer1 = computer("lenovo", "black", "8 gb", "512gb")
computer2 = computer("asus", "gray", "32 gb", "120gb")

print(computer1.ssd)  # 512gb
print(computer2.ssd)  # 120gb


class computer():
    def __init__(self, model="None", colour="None", ram="8gb", ssd="1tb"):  # defauld value
        print("init function called")
        self.model = model
        self.colour = colour
        self.ram = ram
        self.ssd = ssd


computer3 = computer(ram="512gb")
print(computer3.model)  # None
print(computer3.ram)  # 512gb

class bird():
    print("init function is called")
    def __init__(self,type = "None",
                 colour = "None",
                 gender = "None"):
        self.type = type
        self.colour = colour
        self.gender = gender

eagle = bird("eagle", "black", "male")
print(eagle.gender) # male
eagle = bird(gender="female")
print(eagle.gender) # female

class makarna():
    def __init__(self,cinsi = "None", marka = "None"):
        self.cinsi = cinsi
        self.marka = marka

makarna1 = makarna(marka = "oba")
print(makarna1.cinsi)
print(makarna1.marka)

