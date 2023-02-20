file = open("Bilgiler.txt","r") #r olan dosyayı açar ve işlem yapmayı sağlar.
#eğer r ile olmayan bir dosya açmaya çalışırsan FileNotFoundError hatası alırsın.
file.close()
try:
    file = open("Bilgiler1.txt","r")
except FileNotFoundError:
    print("Dosya bulunamadı.")

file = open("Bilgiler.txt","r")
for i in file:
    print(i, end = "")
file.close()

# read() fonsionu eğer içine bir değer verilmez ise tüm dosyayı okur. Eğer değer verilirse bir kısmını okur.

file = open("Bilgiler.txt","r")
icerik = file.read()
print("Dosya içeriği:\n",icerik,sep="")
file.close()

# readline() fonksiyonu her çağrıldığında dosyanın sadece bir satırını okur. Her seferinde dosya imlecimiz bir satır
# atlayarak devam eder.

file = open("Bilgiler.txt","r")
print(file.readline())
print(file.readline())
file.close()


# readlines() dosyanın bütün satırları bir liste şekline döner.
file = open("Bilgiler.txt","r")
print(file.readlines())

