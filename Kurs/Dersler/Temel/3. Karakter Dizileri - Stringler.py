"""
Stringler gerçek yaşamda kullandığımız yazıların aynısıdır. Bu veri tipi aslında her biri bir karakterolan bir dizindir. 
Örnek olarak, "ali" string sırasıyla a,l,i stringi sırasıyla a,l,i harflerinden veya karakterlerden oluşmaktadır. Bu 
konuda strinleri ve stringlerin özelliklerin görmeye çalışacağız. 
"""

# String oluşturmanın farklı olları vardır bunlar:

# 1- Tek tırnak ile: 'Ali Çiçekçioğlu'
# 2- Çift tırnak ile: "Ali Çiçekçioğlu"
# 3- Üç tırnak ile: """Ali Çiçekçioğlu""""

""""
Stringler birer karakter dizileri oldukları için her bir karakterin aslında string içinde bir yer vardık. Örnek olarak 
"ali" stringinde a,l,i karakterilerinin yerleri indeks olarak adlandırılır. Pythonda ve genellikle çou programlama
dilinde stringlerin indekslemesi "0" dan başlamaktadır. 
"""
# 0. elemana ulaşalım. Bunun için [] operatörünü kullanacağız.

a = "ali"
print(a[0])
print(a[1])
print(a[2])

# stringler sondan da indekslenebilir. Sondan başlayarak -1, -2 şeklinde gidir.

print(a[-1])

# String parçalama: [başlama indeksi : bitiş indeksi : atlama değeri]
b = "Python Programlama Dili"

# 4. indexten başla 10. indekse kadar (dahil değil) al. Atlama değeri girilmeyebilir. 10. index dahil değil.
print(b[4:10])

# Baştan 10. indekse git ama 10. indeksi dahil etme.
print(b[:10])

# Baştan 4. den başla sonuna kadar git.
print(b[3:])

# Baştan sona iki değer atlaya atlaya git.
print(b[::2])

# 4. den 12. indekse iki atlayarak git.
print(b[3:12:2])

# Terten yazdırma.
print(b[::-1])

# String uzunluğu bulma.
string = "Merhaba"
print(len(string))

# Stringler toplanabilir.

c = "Python "
d = "Programlama "
e = "Dili "

print(c + d + e)
print("Selam, " * 3)

# !!!!!Stringler doğrudan değiştirilemez fakat aşağıdaki işlem yapılabilir. (Mülakatta sorulabilecek bir soru.)

f = "Ali "
f = f + "Çiçekçioğlu."
print(f)