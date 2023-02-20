# Main class ortak bir noktası bulunan sınıflar için ortak özellikleri miras alan class'tır.
# Örneğin bir şirkette resepsiyonist,yönetici,IT vs farklı sınıflardır.
# Ama hepsi çalışandır ve isimleri maaşları ve departman isimleri vardır.

class Worker():
    def __init__(self,name, salary, department):
        self.name = name
        self. salary = salary
        self.department = department
    def worker_info(self):
        print(f"""
        Name: {self.name}
        Salary: {self.salary}
        Department: {self.department}
        """)
    def chanching_department(self,new_department):
        self.department = new_department

class Manager(Worker):
    def change_salary(self,newsalary):
        self.salary = newsalary

manager1 = Manager("Ali Çiçekçioğlu",1200,"Management")
manager2 = Manager("Murat Çiçekçioğlu",1200,"Management")
print(manager1.worker_info())
manager1.chanching_department("IT")
print(manager1.worker_info())
manager2.change_salary(5000)
print(manager2.worker_info())
