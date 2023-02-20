# Bir sayının tam bölenlerini listeye ekleyeceğiz.

def bolen(a):
    liste = []
    for i in range(1,a+1):
        if(a%i==0):
            liste.append(i)
    return liste

while True:
    a = input("Sayi: ")
    if(a=="q"):
        break
    else:
        a = int(a)
        print(f"Bölenler: {bolen(a)}")
