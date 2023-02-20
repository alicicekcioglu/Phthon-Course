"""
upper() metodu stringin tüm karakterlerini büyük yapar.
lower() metodu stringin tüm karakterlerini küçük ypar.
"""
print("pyThon".upper()) #PYTHON büyük harfi büyük bıraktı.
print("PytHON".lower()) #python küçük harfi küçük bıraktı.

"""
replace("x","y") stringlerdeki x değerin y değeri ile değiştirir. 
"""

print("selam".replace("e","a")) #salam
print("Kurt".replace("Ku","Ka")) #Kart x değeri için büyük küçük harf aynı olmalı!
print("Python programlama dili".replace(" ","\n")) # boşluğa tire vs. getirilebilir.

"""
startswitzh(x) string x ile başlıyor ise True, başlamıyor ise False döndürür. 
endswith(x) string x ile biliyorsa True, bitmiyor ise False döndürür. 
"""

"Python".startswith("py") # False çünkü Py ile başlıyor py ile değil.
"Python".startswith("Py") # True

"""
split(a) değerine göre string parçalara ayrılarak her bir parça listeye alınır. 
"""
liste = "Python programlama dili".split(" ") #boşluktan bölündür
print(liste) # ['Python', 'programlama', 'dili']

liste2 = "Pyhont-Java-Php".split("-")
print(liste2) #['Pyhont', 'Java', 'Php']

"""
strip(x) stringin başında bulunan ve sonunda bulunan x değerlerini siler.  
lstrip(x) stringin sadece başında bulunan x değerlerini siler.  
rstrip(x) stringin sadece sonunda bulunan x değerlerini siler. 
"""
print("              Python   ".strip()) # Python değer girilmez ise varsayılan olalrak boşluk karakterini siler.
print("aaaaaaaaaaaPythonaaaa".strip("a")) # Python
print("aaaaaaaaaaaPythonaaaa".lstrip("a")) # Pythonaaaa
print("aaaaaaaaaaaPythonaaaa".rstrip("a")) # aaaaaaaaaaaPython

"""
join() listenin elemanlarını bir string değeriyle birleştirmeyi sağlar. 
"""
liste3 = ["21","02","2014"]
print("/".join(liste3)) # 21/02/2014
a = ["T","B","M","M"]
print(".".join(a)) # T.B.M.M

"""
count(x) string içerisindeki x değerini sayar.
count(x,index) stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar. 
"""

print("ada kapısı yandan çarklı".count("a")) #6
print("ada kapısı yandan çarklı".count("a",2)) #5 2. index sayıma dahil.
print("ada kapısı yandan çarklı".count(" ")) #3

"""
find(x) x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indexi döndürür.
    Bulamaz ise -1 değerini döndürür. 
rfind(x) x değerini sonran itibaren string içinde arar ve bulursa ilk bulduğu indexi döndürür. 
    Bulamaz ise -1 değerini döndürür. 
"""
print("araba".find("a")) #0
print("araba".find("s")) #-1
print("araba".rfind("a")) #4
print("araba".rfind("s")) #-1






































