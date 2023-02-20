user1 = {"ad": "Ferhat",
         "soyad": "Ibrik",
         "uzmanlık": "Front-End"
}
user2 = {"ad": "Gokce",
         "soyad": "Gun",
         "uzmanlık": "Tasarım"
}
user3 = {"ad": "Mesut",
         "soyad": "Gun",
         "uzmanlık": "Front-End"
}
# Ferhat ıbrik kullanıcısinin uzmanlık alanını döndür.
print(user1.get("uzmanlık"))
print(user1["uzmanlık"])

#front-end alanındaki uzmanların isimlerini döndür.
userlist = [user2, user3, user1]
for i in userlist:
    if i.get("uzmanlık") == ["Front-End"]:
        print(i.get("ad"))

# Mesut kullanıcısı yazılım öğrendi bilgilerini güncelle.
user3["uzmanlık"].append("Yazılım")