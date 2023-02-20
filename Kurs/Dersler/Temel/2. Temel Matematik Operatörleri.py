# Tamsayı bölmesi operatörü (//)
# Bu operatör, bir sayının başka bir sayıya bölümünden ortaya çıkan bölüm sonucunu vermektedir.
a = 22.7/11.4
print(a)

b = 22.7//11.4
print(b)

# Kalanı Bulma (%)
# Bu operatör bir sayının başka bir sayıya bölümünden kalan sonucu bulmaya olanak tanır.
# Bir sayının çiftmi tekmi olduğunu bulmak için kullanılabilir.
a = 13 % 4
print(a)

b = 4 % 2
print(b)

# üs bulma (**)
# Bir sayının üssünü bulmaya yarar. Örneğin operatörün solundaki sayının sağındaki sayıya göre üssüne ekrana basar.
a = 4 ** 3
print(a)

b = 2 ** 3
print(b)

c = 9 ** 9
print(c)

# bu operatör ile karekök bulunabilir.
# bir sayının 1/2 (0.5) üssüdür. Yani 3 ** 0.5 yazarsak 3'ün karekökünü buluruz.
a = 64 ** 0.5
print(a)

# Küp kök almak için 1/3
a = 8 ** (1/3)
print(a)

# İşaret değiştirme
a = -4
a = -a
print(a)

"""
Operatörleri beraber kullanma ve işlem sırası

1- Parantez içi her zaman önce yapılır. 
2- Çarpma ve bölme her zaman toplama ve çıkarma işleminden önce yapılır.
3- İşlem soldan sağa belirlenir. 

"""

print(8 + 4 * 3 / 2 - 18)
print(8 + ((4 * 3) / 2) - 18)
print((8 + 4) * 3 / 2 - 18)
print(((10 ** 2) // 3) / 3)