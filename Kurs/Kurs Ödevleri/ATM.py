bakiye = 0
islem = int(input("ATM'ye hoşgeldiniz.\n\t"
                      "1- Bakiye sorgulama\n\t"
                      "2- Bakiye yükleme\n\t"
                      "3- Bakiye çekme\n\t"
                      "Çıkmak için (0) tuşlayınız.\n\t"
                      "Yapmak istediğiniz işlemi seçiniz: "))
while True:
    if (islem == 1):
        print("Güncel bakiyeniz {} TL'dir.".format(bakiye))
        islem = int(input("Yapmak istediğiniz farklı bir işlem var mı?: "))
    elif (islem == 2):
        print("Bakiye: {}".format(bakiye))
        yukleme = int(input("Lütfen yatırmak istediğiniz tutarı giriniz:"))
        bakiye += yukleme
        print("Güncel bakiyeniz {} TL'dir.".format(bakiye))
        islem = int(input("Yapmak istediğiniz farklı bir işlem var mı?: "))
    elif (islem == 3):
        print("Bakiye: {}".format(bakiye))
        para_cekme = int(input("Lütfen çekmek istediğiniz tutarı giriniz:"))
        if (bakiye - para_cekme < 0):
            print("Çekmek istediğiniz tutar bakiyenizden daha yüksek olamaz!")
            islem = int(input("Yapmak istediğiniz farklı bir işlem var mı?: "))
            continue
        print("Güncel bakiyeniz {} TL'dir.".format(bakiye - para_cekme))
        islem = int(input("Yapmak istediğiniz farklı bir işlem var mı?: "))
    elif (islem == 0):
        print("Çıkış işlemi başarılı.")
        break
    else:
        print("Lütfen geçerli bir işlem giriniz!")
        islem = int(input("Yapmak istediğiniz işlem nedir?: "))