"""
Özel metodlar bizim özel olarak çağırmadığımız fakat her class'a ait olan metodlarıdır.
Çoğunu biz tanımlamasak bile Python tarafından varsıyılan olarak tanımlanır.
Bazılarının özel olarak tanımlamamız gerekiyor. Örneğin: init
"""

"""
class Book():
    pass

book = Book() #Phyton burada init metodunu otomatik olarak çağrıyor.

print(book) # Yine python burada __str__ metodunu tanımlıyor.

# print(len(book))    # Python burada __len__ metodunu çağırmak istiyor. Ama nasıl tanımlanması gerektiğini bilmediği için bizden istiyor ve hata veriyor.

del book # del objeyi silmeye yarar __del__ metodunu çağırıyor biz tanımlamadığımız için kendisi tanımlıyor.
"""

class Book():
    def __init__(self,name,writer,page,category):
        print("init function")
        self.name = name
        self.writer = writer
        self.page = page
        self.category = category

book = Book("Suç ve Ceza", "Dostoyevski", 650, "Roman")

class Book():
    def __init__(self,name,writer,page,category):
        print("init function")
        self.name = name
        self.writer = writer
        self.page = page
        self.category = category
    def __str__(self): # return ile string döndürmesi gerekir. Print içine stringi yazdırabiliriz.
        return f"Name: {self.name}\nWriter: {self.writer}\nPage: {self.page}\nCategory: {self.category}"

book2 = Book("Suç ve Ceza", "Dostoyevski", 650, "Roman")
print(book2)

class Book():
    def __init__(self,name,writer,page,category):
        print("init function")
        self.name = name
        self.writer = writer
        self.page = page
        self.category = category
    def __str__(self):
        return f"Name: {self.name}\nWriter: {self.writer}\nPage: {self.page}\nCategory: {self.category}"
    def __len__(self):
        return self.page

book3 = Book("Suç ve Ceza", "Dostoyevski", 650, "Roman")
print(len(book3))

class Book():
    def __init__(self,name,writer,page,category):
        print("init function")
        self.name = name
        self.writer = writer
        self.page = page
        self.category = category
    def __str__(self):
        return f"Name: {self.name}\nWriter: {self.writer}\nPage: {self.page}\nCategory: {self.category}"
    def __len__(self):
        return self.page
    def __del__(self): #doğrudan del yazarsam kitabı silerim. Burada default olan def'e override etmiyor. Yeni özellik ekliyor.
        print("Kitap objesi silindi.")


book = Book("Suç ve Ceza", "Dostoyevski", 650, "Roman")
del book
print(book) # NameError: name 'book' is not defined

