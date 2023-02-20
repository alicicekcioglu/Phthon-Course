import random
names = ["Zeynep", "Elif", "Hiranur", "Defne", "Miray", "Azra", "Zehra", "Ecrin", "Yağmur", "Eylül", "Nisanur", "Ela",
         "Belinay", "Nehir", "Meryem", "Asya", "Esila", "Rabia", "Buğlem", "Hira", "Yusuf", "Eymen", "Ömer", "Mustafa",
         "Miraç", "Berat", "Ahmet", "Hamza", "Mehmet", "Emir", "Muhammed Ali", "Muhammed", "Ali", "Çınar", "Kerem",
         "Yiğit", "Ayaz", "Ertuğrul", "Ömer", "Asaf", "Yunus Emre"]
surname = ["Yıldız", "Yıldırım", "Öztürk", "Aydın", "Özdemir", "Arslan", "Doğan", "Kılıç", "Aslan", "Çetin", "Kara",
           "Koç",
           "Kurt", "Özkan", "Şimşek"]

group = []
x = []
def name_generator():
    while True:
        full_name = random.choice(names) + " " + random.choice(surname)
        group.append(full_name)
        for i in group:
            if i not in x:
                x.append(i)
        if len(x) == 200: #You can change the name number
            x.sort()
            print(x)
            #or
            with open("names.txt","w",encoding="utf-8") as file:
                for i in x:
                    file.write(i) + file.write("\n")
            break
name_generator()















