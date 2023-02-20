"""
İçindekiler:

1- Tamsayı (integer) ve Ondalıklı Sayı (float)
2- Basit matemetik işlemleri
3- Değişken tanımlama
"""
"""
# Toplama, çıkarma, bölme, çarpma

3+4
3-4
3*4
3/4

"""

# Değişken tanımlama

a = 1
print(a)
b = 3
print(b)
c = a*3+5

pi_sayisi = 3.14
cap = 4
cevre = pi_sayisi*cap
print(cevre)

"""
Değişken ismi verirken dikkat edilmesi gerekenler.

1- Değişken isimleri bir sayı ile başlayamaz.
2- Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
3- Semboller değiken isminde kullanılamaz ("_" hariç)
4- Python'da tanımlı anahtar kelimeler değişken ismi olarak kullanılmaz. 
"""

# değerlerin yerini değiştirme
a,b = b,a
print(a,b)

# değerin kendisini değiştirme

a = a+1
a += 1
a -= 1
a *= 3
a /= 5

print(a)