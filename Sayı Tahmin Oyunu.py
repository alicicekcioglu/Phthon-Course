import random
import time

print("""******************
Sayı Tahmin Oyunu
1- Bilgisayarın 1 ile 1000 arasında seçtiği sayıyı tahmin edersen kazanırsın.
2- 7 tahmin hakkın var :) 
******************""")
rastgele_sayi = random.randint(1,1000)
tahmin_hakki = 0

while True:
    tahmin = int(input("Sayı: "))
    if tahmin < rastgele_sayi:
        time.sleep(0.5)
        print("Hmmm, bir bakalım...")
        time.sleep(0.3)
        print("Daha büyük bir sayı denemelisin.\n******************")
        tahmin_hakki += 1
        print(f"{tahmin_hakki}. turdasın. Dikkat!")
    elif tahmin > rastgele_sayi:
        time.sleep(0.5)
        print("Hmmm, bir bakalım...")
        time.sleep(0.3)
        print("Daha küçük bir sayı denemelisin.\n******************")
        tahmin_hakki += 1
        print(f"{tahmin_hakki}. turdasın. Dikkat!")
    else:
        time.sleep(0.5)
        x = input("Ah! Evet evet, buldun işte bu! Tebrikler.\n******************Tekrar oynamak ister misin?\n(y/n): ")
        if x == "y":
            continue
        else:
            break
    if tahmin_hakki == 10:
        time.sleep(0.3)
        x = input("Şanssızlık belki bir daha denersen bulabilirsin.\n******************Tekrar oynamak ister misin?\n(y/n): ")
        print(f"Bilgisayarın tahmini: {rastgele_sayi}")
        if x == "y":
            continue
        else:
            break