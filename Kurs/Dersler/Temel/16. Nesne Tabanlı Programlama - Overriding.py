"""
Eğer miras alınan metodlar aynı isimle kendi sınıfına tekrar tanımlanırsa, tekrar çağırıldığında miras alınan değil
kendi metodumuz çalışır.
Örneğin Worker sınıfının init metodunu kullanmak yerine Manager sınıfının init metodunu override edebiliriz.
Böylece Manager sınıfına eksta attribute ekleyebiliriz. Yani bir metod iptal edilmiş (override) olur.
"""


class Worker():
    def __init__(self, name, salary,
                 department):  # Burada 3 adet metod tanımladık. Ama ben yönetici sınıfı için bir metod daha tanımmlamak istiyorum.
        self.name = name
        self.salary = salary
        self.department = department

    def worker_info(self):
        print(f"""
        Name: {self.name}
        Salary: {self.salary}
        Department: {self.department}
        """)

    def chanching_department(self, new_department):
        self.department = new_department


class Manager(Worker):
    def __init__(self, name, salary, department,
                 nmbofmanaged):  # Burada tekrar tanımlamasaydım, yöneticiye yeni bir şey eklerken hata alırdık.
        self.name = name
        self.salary = salary
        self.department = department
        self.nmbofmanaged = nmbofmanaged

    def worker_info(self):
        print(f"""
        Name: {self.name}
        Salary: {self.salary}
        Department: {self.department}
        Number of Managed: {self.nmbofmanaged}""")

    def change_salary(self, newsalary):
        self.salary = newsalary


manager1 = Manager("Ali Çiçekçioğlu", 4000, "Manager", 12)
print(manager1.worker_info())
