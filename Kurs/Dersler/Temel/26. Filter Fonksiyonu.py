#filter fonksiyonuna girilen değer boelan tipinde olmak zorunda
# fonksiyonu her elemna uygular ve sadece true olanları döner

print(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8]))# <filter object at 0x0000014A5CBD7250>
print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8]))) #sadece çift olanları yazdırdı.

def asal_mi(x):
    i = 2

    if (x == 1):
        return False
    elif (x==2):
        return True
    else:
        while(i < x):
            if x % 2 == 0:
                return False
            i += 1
        return True

print(asal_mi(7))
print(list(filter(asal_mi,range(1,100)))) #1'den 100'e kadar olan asal sayıları döndü.