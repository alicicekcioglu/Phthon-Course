# 1 ve kendisinden başka sayıya bölünemeyen sayılara Asal Sayı denir. Örn: 5

# Önce 2 den başlayarak o sayıya kadar olan sayıları oluşturacağız. Sayının kendisi dahil olmayacak.
# Listedeki herhangi bir sayıya tam bölünürse asal değildir.

def asalsayi(a):
    if(a == 1):
        return False
    elif(a == 2):
        return True
    else:
        for i in range(2,a):
            if(a % i == 0):
                return False
            else:
                return True

while True:
    a = input("Sayı: ")
    if (a == "q"):
        break
    else:
        a = int(a)
        if(asalsayi(a)):
            print(f"{a} asal bir sayıdır.")
        else:
            print(f"{a} asal bir sayı değildir.")