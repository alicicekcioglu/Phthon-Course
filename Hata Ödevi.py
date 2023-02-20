liste = ["345","sadas","324a","14","kemal",95]
yeni_liste = []
def str_findir():
    try:
        for i in liste:
            if type(i) == str:
                yeni_liste.append(i)
        print(yeni_liste)
    except ValueError:
        print("Please check the input.")
    finally:
        print("İşlem tamamlandı.")

def ciftsayibulma():
    sayi : int(input("Sayı: "))
    if sayi % 2 == 0:
        return sayi()
    try:
        print(f"{sayi} bir çift sayıdır.")
        if type(sayi) != int:
            raise ValueError("Lütfen bir tamsayı giriniz.")
    finally:
        print("Program sona erdi.")

    Liste = [2,42,64,34,9,72,4547,12,4,54,6,65,65,45,7,3,48,79,3]
    ciftsayilar = []
    for i in liste:
        if i % 2 == 0:
            ciftsayilar.append(i)
        print(ciftsayilar)