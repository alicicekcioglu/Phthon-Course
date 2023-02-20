sys_kullanici_adi = "rKENSHIN"
sys_sifre = "asd123asd"
giris_hakki = 3
while True:
    kullanici_adi = input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")

    if (sys_kullanici_adi == kullanici_adi and
        sys_sifre == sifre):
        print("İşlem başarılı.")
        break

    if (sys_kullanici_adi != kullanici_adi or
        sys_sifre != sifre):
        giris_hakki -= 1
        print("Kullanıcı adı ya da şifre hatalı. Lütfen bilgilerinizi kontlor ederek tekrar deneyiniz.")
    if (giris_hakki == 0):
        print("Giriş hakkınınız doldu!")
        break
