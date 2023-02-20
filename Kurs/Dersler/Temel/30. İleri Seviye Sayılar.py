"""
Bazen programlarmada sayıların 10'luk taban haricinde 2'lik (binary) ve 16'lık (hexadecimal) tabanda kullanmak
isteyebiliriz.
"""

print(bin(4)) # bin fonksiyonu ile sayımız 2'lik sistemde yazıldı.
print(bin(24)) # 0b11000 0b ikilik sistemde oluğunu gösteriyor.
print(bin(156))
print(bin(999))

print(hex(20)) # hex fonksiyonu ile sayımız 16'lik sistemde yazıldı.
print(hex(34))# 0x22 0x on altılık sistemde oluğunu gösteriyor.

"""
abs() fonksiyonu sayının mutlak değerini almamızı sağlar.
Mutlak değer; bir sayının 0'a olan uzaklığıdır.
"""

print(abs(-4))
print(abs(4.5))

"""
round() fonksiyonu sayıları alta ve üste yuvarlar. 
"""

round(3.7) #4
round(3.2) #3
round(3) #3
round(3.342342345234,235233) #3.342342345234 ondalık sistemi sayının 4. hanesine göre yavarlar.

"""
max ve min fonksiyonu
    max() fonksiyonu verdiğimiz değerlerin en büyüğünü döndürür.
    min() fonskiyonu verdiğimiz değerlerin en küçüğünü döndürür. 
"""
max(3,4,6,6,234,2,3,6,6) # istediğimiz kadar değer verebiliriz. # 234
max([3,4,6,6,234,2,3,6,6])  # liste şeklinde verebiliriz
max((3,4,6,6,234,2,3,6,6)) # sayıları demek şeklinde verebiliriz.

"""
sum() fonksiyonuu verilen değerleri toplayarak döndürür. 
Değerlerin liste ya da demet şeklinde girilmesi gerekir. 
"""

# sum(3,4) TypeError: "int" object not iterable
# sum((2,3,4,"python")) içeride str değer olduğu için yine hata verir.

sum([3,4,5])
sum((3,4,5))
sum((3,4.3,5))

"""
pow() fonksiyonu üs alma işleminde kullanılır.
"""

pow(2,4) #2 üzeri 4







