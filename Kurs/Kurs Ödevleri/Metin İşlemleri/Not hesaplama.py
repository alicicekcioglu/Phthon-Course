def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    isim = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])

    son_not = vize1 * (3/10) + vize2 * (3/10) + final * (4/10)

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return isim + ": "+harf+"\n"

with open("Notlar.txt", "r", encoding="utf-8") as file:

    eklenecekler_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("notlar.txt","w",encoding="utf-8")as file2:
        for i in eklenecekler_listesi:
            file2.write(i)